import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html as LH
from tabulate import tabulate
import re

urls_dict = {
    'Carrier RIF': 'https://www.resdac.org/cms-data/files/carrier-rif/data-documentation',
    'Durable Medical Equipment RIF': 'https://www.resdac.org/cms-data/files/dme-rif/data-documentation',
    'Home Health Agency RIF': 'https://www.resdac.org/cms-data/files/hha-rif/data-documentation',
    'Hospice RIF': 'https://www.resdac.org/cms-data/files/hospice-rif/data-documentation',
    'Inpatient RIF': 'https://www.resdac.org/cms-data/files/ip-rif/data-documentation',
    'Outpatient RIF': 'https://www.resdac.org/cms-data/files/op-rif/data-documentation',
    'Skilled Nursing Facility RIF': 'https://www.resdac.org/cms-data/files/snf-rif/data-documentation',
    'Beneficiary Summary File': 'https://www.resdac.org/cms-data/files/mbsf/data-documentation',
    'MedPAR RIF': 'https://www.resdac.org/cms-data/files/medpar-rif/data-documentation'}

all_links = []
for page_title, url in urls_dict.items():
    page = requests.get(url)
    links = LH.fromstring(page.content).xpath('//tr/td/a/@href')
    all_links.extend(links)
    dfs = pd.read_html(page.content)

    soup = BeautifulSoup(page.content, 'html.parser')
    if page_title != 'Master Beneficiary Summary File':
        table_titles = [x.get_text() for x in soup.find_all('h3')[:-1]]
        table_titles.insert(0, page_title)
    else:
        table_titles = [x.get_text() for x in soup.find_all('h3')]

    all_tables = []
    for i in range(len(dfs)):
        df = dfs[i]
        
        # Remove phantom 6th column:
        df = df.iloc[:,:5]
        
        # Add links
        df['refname'] = links[:len(df)]
        links = links[len(df):]
        
        # Replace NaN with blank string
        df = df.fillna('')
        
        # Make Variable Name column a Markdown link
        df.iloc[:, 2] = '[' + df.iloc[:, 2] + '](https://www.resdac.org' + df['refname'] + ')'
        df = df.drop(columns=['refname'])
        
        # Make Short SAS Name code style
        df.iloc[:, 1] = '`' + df.iloc[:, 1] + '`'
        
        # Write to file
        text = tabulate(df, headers = ['Index', 'SAS Name', 'Variable Name', 'Limitation', 'Code Table'], tablefmt = 'pipe', showindex = False)
        
        all_tables.append('\n### {}\n\n'.format(table_titles[i]))
        all_tables.append(text)
        all_tables.append('\n')


    # Read in Markdown file
    fname = re.search(r'/([\w-]+)/data-documentation', url)[1]
    mdfile = open(os.path.join('docs', 'resdac', fname + '.md'), 'r')
    lines = mdfile.readlines()
    mdfile.close()

    # Find the line that says "Data Documentation"
    re_text = r'(?i)\#+\s*data\s+documentation'
    line_num = [ind for ind, x in enumerate(lines) if re.search(re_text, x)]
    if line_num:
        line_num = line_num[0]
    else:
        raise ValueError('Didn\'t match any line of file')

    lines = lines[:line_num + 1]
    lines.extend(all_tables)

    mdfile = open(os.path.join('docs', 'resdac', fname + '.md'), 'w')
    mdfile.writelines(lines)
    mdfile.close()


all_links = sorted(list(set(all_links)))
all_links = ['http://www.resdac.org' + x for x in all_links]

url = 'http://www.resdac.org' + '/cms-data/variables/Beneficiary-LRD-Used-Count'
url = 'https://www.resdac.org/cms-data/variables/Claim-Query-Code'
url = 'https://www.resdac.org/cms-data/variables/Claim-Payment-Amount-0'
all_text = []
all_text.append('# Variable Definitions\n\n')

for url in all_links[:25]:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    short_name = soup.find(class_='field-name-field-short-sas-name').find(class_='field-item').get_text()
    long_name = soup.find(class_='field-name-field-long-sas-name').find(class_='field-item').get_text()
    
    found_in_files = soup.find(class_='view-content').get_text()
    
    main_text = soup.find_all(id = ['block-system-main', 'region-content'])
    p_text = main_text[0].find_all('p')
    len(p_text)
    text_list = []
    for i in range(len(p_text) - 1):
        text_list.append(p_text[i].get_text())
    
    text = '\n\n'.join(text_list)
    
    # Format as inline code any text within '' that has at least one digit
    text = re.sub(r"'(\w*\d\w*)'", r"`\1`", text)
    
    try:
        values = pd.read_html(page.content)
    except:
        pass
    
    section = soup.find(id = 'page-title').get_text()
    # NOTE! If I use the actual page title, I can't assume the header anchors will use the text in the tables in the documentation. I.e. in the first step, I'd need to get the links that each variable links to, grab the title off of that page, and then generate what the anchor would be.

    # section = re.search(r'/([^/]+)$', url)[1]
    # section = section.replace('-', ' ')
    # if not True in [x.isupper() for x in section]:
    #     section = section.title()
    
    section = '\n\n#### [' + section + '](' + url + ')\n\n'
    
    all_text.append(section)
    all_text.append(text)

mdfile = open(os.path.join('docs', 'resdac', 'variables.md'), 'w')
mdfile.writelines(all_text)
mdfile.close()

all_text




