#! /usr/bin/env python3
"""
---------------------------------------------------------------------
Project: medicare-documentation
Program: 01download.py
Author:  Kyle Barron <barronk@mit.edu>
Created: 1/18/2018, 5:13:44 PM
Updated: 1/18/2018, 5:13:44 PM
Purpose: Download html pages from ResDAC's site once, so that I don't have
         to load their pages every time I change something
Output:
    ../data/resdac/html/variables/*
    ../data/resdac/html/rif/*
"""

import re
import os
import requests
import lxml.html as LH
from time import sleep

urls_dict = {
    'Beneficiary Summary File':
        'https://www.resdac.org/cms-data/files/mbsf/data-documentation',
    'Carrier RIF':
        'https://www.resdac.org/cms-data/files/carrier-rif/data-documentation',
    'Durable Medical Equipment RIF':
        'https://www.resdac.org/cms-data/files/dme-rif/data-documentation',
    'Home Health Agency RIF':
        'https://www.resdac.org/cms-data/files/hha-rif/data-documentation',
    'Hospice RIF':
        'https://www.resdac.org/cms-data/files/hospice-rif/data-documentation',
    'Inpatient RIF':
        'https://www.resdac.org/cms-data/files/ip-rif/data-documentation',
    'MedPAR RIF':
        'https://www.resdac.org/cms-data/files/medpar-rif/data-documentation',
    'Outpatient RIF':
        'https://www.resdac.org/cms-data/files/op-rif/data-documentation',
    'Skilled Nursing Facility RIF':
        'https://www.resdac.org/cms-data/files/snf-rif/data-documentation'
}

# Download top-level documentation pages, and get links to variables
all_links = []
for page_title, url in urls_dict.items():
    sleep(10)
    page = requests.get(url)

    stub = re.search(r'([\w-]+)/data-documentation', url)[1]
    path = os.path.join('..', 'data', 'resdac', 'html', 'rif', stub + '.html')

    with open(path, 'w') as text_file:
        text_file.write(page.content.decode('utf-8'))

    links = LH.fromstring(page.content).xpath('//tr/td/a/@href')
    all_links.extend(links)

# Download variable pages
all_links = sorted(list(set(all_links)))
for url in all_links:
    sleep(10)
    page = requests.get('http://www.resdac.org' + url)

    folder = re.search(r'^/([\w/-]+)/[\w/-]', url)[1]
    folder_path = os.path.join(
        '..', 'data', 'resdac', 'html', 'variables', folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    html_path = os.path.join(
        '..', 'data', 'resdac', 'html', 'variables', url[1:] + '.html')
    with open(html_path, 'w') as text_file:
        text_file.write(page.content.decode('utf-8'))
