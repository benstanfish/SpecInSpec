import os
from pathlib import Path
from defusedxml import ElementTree as ET

from src.console.escapes import Escapes



def clean_0x81_file(file_path: str, 
                    new_path: str='') -> None:
    """Replaces the 0x81 byte (all occurances) and saves to file.

    Args:
        file_path (str): Path to .xml, .sec or other file.
        new_path (str, optional): Write to new_path if provided, else overwrite existing. Defaults to overwrite.
    """
    find_text = b'\x81'
    replace_text = b''
    with open(file_path, 'rb') as file:
        content = file.read()
    content = content.replace(find_text, replace_text)
    try:
        if new_path:
            with open(new_path, 'wb') as file:
                file.write(content)
        else:
            with open(file_path, 'wb') as file:
                file.write(content)
    except Exception as e:
        print(f'An error occured when trying to write the file to {'new file' if new_path else 'existing path'}: {e}')
    print(f'Cleaned file written {'new file' if new_path else 'existing path'}: {new_path if new_path else file_path}')

def file_has_0x81(file_path: str) -> bool:
    """Determine if the file contains occurances of the 0x81 character.

    Args:
        file_path (str): Path to .xml, .sec or other file.

    Returns:
        bool: True if file contains 0x81.
    """
    try: 
        with open(file_path, 'r') as file:
            content = file.read()
        return False
    except:
        return True

def get_file_dict(parent_dir: str=r'./specs/sec',
                  extension: str='.sec') -> dict:
    """Creates dictionary of file stems and absolute paths that match the file extension condition.

    Args:
        parent_dir (str, optional): Path to directory (parent) of files to be included. Defaults to r'./specs/sec'.
        extension (str, optional): File extension to be matched. Defaults to '.sec' (a type of .xml).

    Returns:
        dict: Dictionary with keys = file name stem and value = absolute path to file.
    """
    file_list = [os.path.abspath(os.path.join(parent_dir, file)) for \
                file in os.listdir(parent_dir) \
                    if Path(file).suffix.lower() == extension]
    return {Path(file_path).stem: file_path for file_path in file_list}





sec_files = get_file_dict()
for section, path in sec_files.items():
    print(f'{section}: {Escapes.Red + Escapes.Bold if file_has_0x81(path) \
                         else Escapes.Green}{file_has_0x81(path)}{Escapes.Reset}')