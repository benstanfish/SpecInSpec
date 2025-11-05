# Copyright (c) 2025 Ben Fisher
""" 
This module provides utilities parsing an .sec file (a type of .xml file) into an
.html file for review outside SpecsIntact.

It includes functions for:
- XXX

Example usage:
    >>> XXX
"""

import os, shutil, re
from datetime import datetime
from bs4 import BeautifulSoup

from defusedxml import ElementTree as ET
from xml.etree.ElementTree import Element

from pathlib import Path


html_dir = './specs/html'

html_files = []
for file_name in os.listdir(html_dir):
    if Path(file_name).suffix == '.html':
        html_files.append(file_name)


html_template = './src/html/index_template.html'
index_path = os.path.join(html_dir, 'index.html')
index_file = shutil.copy(html_template, index_path)

with open(index_file, 'r') as file:
    index_content = file.read()

soup = BeautifulSoup(index_content, 'html.parser')
ul = soup.find('ul', class_='page_list')

for file in html_files:
    if file != 'index.html':
        new_li = soup.new_tag('li')
        ul.append(new_li)

        new_anchor = soup.new_tag('a')
        new_anchor.append(Path(file).stem)
        new_anchor['href'] = file
        new_anchor['target'] = '_blank'
        new_li.append(new_anchor)

with open(index_file, 'w') as file:
    file.write(str(soup))