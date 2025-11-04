# Copyright (c) 2025 Ben Fisher
""" 
This module provides utilities parsing an .sec file (a type of .xml file) into an
.html file for review outside SpecsIntact.

It includes functions for:
- XXX

Example usage:
    >>> XXX
"""


from defusedxml import ElementTree as ET
from xml.etree.ElementTree import Element


test_file = './specs/cleaned_sec/05 12 00.sec'

tree = ET.parse(test_file)
root = tree.getroot()

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
    
number_sections_recursively(root)

for element in root.iter():
    if element.get('outline'):
        print(element.tag, element.get('outline'))


