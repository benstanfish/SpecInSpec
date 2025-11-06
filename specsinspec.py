# Copyright (c) 2025 Ben Fisher
""" 
XXX

It includes functions for:
- XXX

Example usage:
    >>> XXX
"""
import os
from pathlib import Path

from src.process.clean0x81 import clean_0x81_files
from src.process.sectohtml import process_sec_file
from src.process.createhtmltoc import create_error_html, create_index

sec_folder = './specs/sec'

def create_html_reports(folder_path:str) -> None:
    source_basename = os.path.basename(folder_path)
    parent_folder = Path(folder_path).parent.resolve()

    cleaned_path = os.path.join(parent_folder, f'cleaned_{source_basename}')
    if not os.path.exists(cleaned_path):
        os.mkdir(cleaned_path)

    os.path.abspath(clean_0x81_files(orig_dir=os.path.abspath(folder_path), 
                                     new_dir=cleaned_path, 
                                     file_type='.sec'))
    
    cleaned_sec_files = [file for file in os.listdir(cleaned_path) \
                         if Path(file).suffix == '.sec']
    
    all_file_data = []
    error_files = {}

    for sec_file in cleaned_sec_files:
        try:
            sec_file_data = process_sec_file(os.path.join(cleaned_path, sec_file))
            all_file_data.append(sec_file_data)
        except Exception as e:
            error_files[sec_file] = f'{e}'

    html_dir = os.path.join(cleaned_path, 'html')
    with open(os.path.join(html_dir, 'errors.txt'), 'w') as file:
        file.write(f'<div class="error-row"><div class="error-section">Section</div><div class="error-section">Error</div></div>')
        file.write(f'<br />')
        for key, value in error_files.items():
            file.write(f'<div class="error-row"><div class="error-section">{key}</div><div class="error-value">{value}</div></div>')

    create_error_html(os.path.join(cleaned_path, 'html'))
    create_index(os.path.join(cleaned_path, 'html'))


create_html_reports(sec_folder)