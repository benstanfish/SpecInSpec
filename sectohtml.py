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

def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def remove_declaration(xml_string: str) -> str:
    declaration_pattern = r'<\?xml[^>]*\?>'
    return re.sub(declaration_pattern, '', xml_string, count=1).strip()

def clean_sec_string(xml_string:str, 
                     spaces_reduced:bool=True, 
                     brk_replaced:bool=True, 
                     ast_removed:bool=False, 
                     ast_character:str='*', 
                     ast_count:int=100) -> str:
    temp = remove_declaration(xml_string)
    if spaces_reduced:
        temp = re.sub(' +', ' ', temp)
    temp = re.sub(r'<BRK />\s+?<BRK />', '<BRK />', temp)
    if brk_replaced:
        temp = re.sub('<BRK />', '<br/>', temp)
    if not ast_removed:
        # temp = temp.replace('<AST />', f"<AST>{ast_character * ast_count}</AST>")
        temp = temp.replace('<AST />', f'<AST><hr></AST>')
    else:
        temp = temp.replaced('<AST />', '')
    return temp

def get_all_tags(file_path:str) -> list:
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        raw_tags = []
        raw_tags.append(root.tag)
        for elem in root.iter():
            if elem.tag not in raw_tags:
                raw_tags.append(elem.tag)
        sorted_tags = sorted(raw_tags)
        return sorted_tags
    except Exception as e:
        print(f'An exception occurred: {e}')
    return []

def add_display_tags(tag_name: str, all_text: str) -> str:
    start_tag = f'<{tag_name}>'
    end_tag = f'</{tag_name}>'
    new_start_tag = f'<{tag_name}><pre class="display_{tag_name}">&lt;{tag_name}&gt;</pre>'
    new_end_tag = f'<pre class="display_{tag_name}">&lt;/{tag_name.upper()}&gt;</pre></{tag_name}>'
    temp = all_text.replace(end_tag, new_end_tag)
    temp = temp.replace(start_tag, new_start_tag)
    return temp

def wrap_brackets_in_span(html_string:str) -> str:
    temp = html_string.replace(r'[', r'<div class="brackets">[')
    return temp.replace(r']', r']</div>')

def number_sections_recursively(element:Element, prefix:str='', attrib_name:str='outline'):
    """Recursively add outline number to PRT and SPT tags in XML file.

    Args:
        element (Element): _description_
        prefix (str, optional): _description_. Defaults to ''.
        attrib_name (str, optional): _description_. Defaults to 'outline'.
    """
    part_counter = 0
    current_counter = 0
    for child in element:
        if child.tag == 'PRT':
            part_counter += 1
            child.set(attrib_name, f'{part_counter}')
            number_sections_recursively(child, prefix=f'{part_counter}.')
        elif child.tag == 'SPT':
            current_counter += 1
            child.set(attrib_name, f'{prefix}{current_counter}')
            number_sections_recursively(child, prefix=f'{prefix}{current_counter}.')

def update_html_outline(soup: BeautifulSoup) -> BeautifulSoup:
    for element in soup.find_all():
        if 'outline' in element.attrs and element.name == 'spt':
            title_element = element.find('ttl')
            title_element.string = element.attrs['outline'] + ' ' + title_element.text
    return soup


test_file = './specs/cleaned_sec/03 30 00.sec'

tree = ET.parse(test_file)
root = tree.getroot()

number_sections_recursively(root)

with open(test_file, 'wb') as file:
    file.write(ET.tostring(root))

# The following can be used for initial validation:
# print(root.tag == 'SEC')  

section_info = {
    'section': root.find('SCN').text.replace('SECTION ', '').strip(),
    'title': root.find('STL').text.title().strip(),
    'date': root.find('DTE').text.strip()
}

with open(test_file, 'r') as file:
    content = file.read()

display_tags = ['NTE', 'NPR', 'ENG', 'MET', 'RID', 'RTL', 'ADD', 'DEL', 'SRF', 'STL', 'SUB']
for display_tag in display_tags:
    content = add_display_tags(tag_name=display_tag, all_text=content)
content = wrap_brackets_in_span(content)
content = clean_sec_string(content, brk_replaced=False)

html_fragment = BeautifulSoup(content, 'html.parser')

html_template = './src/html/template.html'
html_path = f"./specs/html/{section_info['section']}.html"

html_file = shutil.copy(html_template, html_path)

with open(html_file, 'r') as file:
    html_content = file.read()



soup = BeautifulSoup(html_content, 'html.parser')
soup.find('title').string = section_info['section'] + '.sec Viewer'
soup.find('main').append(html_fragment)

soup.find('span', class_='this_section_number').append(section_info['section'])
soup.find('span', class_='create_date').append(get_timestamp())



with open('./src/html/reboot.css', 'r') as file:
    css_reboot = file.read()

with open('./src/html/style.css', 'r') as file:
    css_styles = file.read()

with open('./src/html/scripts.js', 'r') as file:
    js_scripts = file.read()

# soup.find(id='reboot').append(css_reboot)
# soup.find(id='styles').append(css_styles)
# soup.find(id='scripts').append(js_scripts)

soup = update_html_outline(soup)
soup.prettify()

with open(html_file, 'w', encoding='utf-8') as file:
    file.write(str(soup))