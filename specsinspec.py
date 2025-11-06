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

sec_folder = './specs/cleaned_sec'


def create_html_reports(folder_path:str) -> None:

    sec_files = [file for file in os.listdir(folder_path) if Path(file).suffix == '.sec']
    for sec_file in sec_files:
        print(sec_file)


create_html_reports(sec_folder)