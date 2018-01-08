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
    'Skilled Nursing Facility RIF': 'https://www.resdac.org/cms-data/files/snf-rif/data-documentation'}

url = 'https://www.resdac.org/cms-data/files/op-rif/data-documentation'
page = requests.get(url)
links = LH.fromstring(page.content).xpath('//tr/td/a/@href')
dfs = pd.read_html(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
table_titles = [x.get_text() for x in soup.find_all('h3')[:-1]]
table_titles.insert(0, 'Outpatient RIF')

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
mdfile = open(os.path.join('docs', 'resdac', 'outpatient_rif.md'), 'r')
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

mdfile = open(os.path.join('docs', 'resdac', 'outpatient_rif.md'), 'w')
mdfile.writelines(lines)
mdfile.close()



