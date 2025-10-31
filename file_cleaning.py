import os, shutil
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
    # print(f'Cleaned file written {'new file' if new_path else 'existing path'}: {new_path if new_path else file_path}')

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

def files_have_0x81(file_dict: dict) -> bool:
    """Loops through files in dictionary to test if each file has 0x81 character and prints color-coded results to console.

    Args:
        file_dict (dict): Dictionary with key = file stem, value = absolute path.
    
    Returns:
        bool: Result of all parsed files in supplied file dictionary.
    """
    dir_has_0x81 = False
    for file_stem, path in file_dict.items():
        file_with_0x81 = file_has_0x81(path)
        if file_with_0x81:
            dir_has_0x81 = file_with_0x81
        print(f'{file_stem}: {Escapes.Red + Escapes.Bold if file_with_0x81 \
                         else Escapes.Green}{file_with_0x81}{Escapes.Reset}')
    print(f'Directory {Escapes.Red + Escapes.Bold + 'has' if dir_has_0x81 \
                       else Escapes.Green + 'does not'}{Escapes.Reset} files with 0x81 character.')
    return dir_has_0x81




original_dir = r'./specs/sec'
original_sec_files = get_file_dict(original_dir)
files_have_0x81(original_sec_files)

new_dir = r'./specs/cleaned_sec'
if not os.path.exists(new_dir):
    os.mkdir(os.path.abspath(new_dir))

cleaned_sec_files = {}
for section, path in original_sec_files.items():
    new_path = os.path.join(os.path.abspath(new_dir), section + '.sec')
    if file_has_0x81(path):
        clean_0x81_file(path, new_path)
    else:
        shutil.copy(path, new_path)
    cleaned_sec_files[section] = new_path

files_have_0x81(cleaned_sec_files)