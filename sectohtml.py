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
from bs4 import BeautifulSoup

from defusedxml import ElementTree as ET


def remove_declaration(xml_string: str) -> str:
    declaration_pattern = r'<\?xml[^>]*\?>'
    return re.sub(declaration_pattern, '', xml_string, count=1).strip()

def clean_sec_string(xml_string:str, multiples:int=100) -> str:
    temp = remove_declaration(xml_string)
    temp = re.sub(' +', ' ', temp)
    temp = re.sub(r'<BRK />\s+?<BRK />', '<BRK />', temp)
    temp = re.sub('<BRK />', '<br/>', temp)
    temp = temp.replace('<AST />', f"<AST>{'*' * multiples}</AST>")
    return temp


test_file = './specs/cleaned_sec/05 12 00.sec'

tree = ET.parse(test_file)
root = tree.getroot()
# print(root.tag == 'SEC')

section_info = {
    'section': root.find('SCN').text.replace('SECTION ', '').strip(),
    'title': root.find('STL').text.title().strip(),
    'date': root.find('DTE').text.strip()
}

# for key, value in section_info.items():
#     print(f'{key.title()}:', value)

with open(test_file, 'r') as file:
    content = file.read()
    
content = clean_sec_string(content)


html_fragment = BeautifulSoup(content, 'html.parser')

html_template = './src/html/template.html'
html_path = f'./src/html/{section_info['section']}.html'

html_file = shutil.copy(html_template, html_path)

with open(html_file, 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
soup.find('title').string = section_info['section'] + '.sec Viewer'
soup.find('body').append(html_fragment)

soup.prettify()

with open(html_file, 'w') as file:
    file.write(str(soup))
