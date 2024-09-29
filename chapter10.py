# Chapter 10: Organizing Files
import os
import shutil
import send2trash
import zipfile
from pathlib import Path
# 1. Copying Files and Folders
# - Copies a file from source to destination
def copy_file(source, destination):
    try:
        p = Path.home()
        print(p)
        shutil.copy(source, destination)
        print(f"Copied '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found.")

# - Copies an entire folder and its contents
def copy_folder(source, destination):
    try:
        shutil.copytree(source, destination)
        print(f"Copied folder '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: Source folder '{source}' not found.")
    except FileExistsError:
        print(f"Error: Destination folder '{destination}' already exists.")

# 2. Moving and Renaming Files and Folders
# - Moves a file or folder to a new location (can also rename)
def move_file_or_folder(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: Source '{source}' not found.")

# 3. Deleting Files and Folders
# - Deletes a single file
def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.unlink(file_path)
            print(f"'{file_path}' has been deleted.")
        else:
            print(f"Error: File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# - Deletes an empty directory
def delete_empty_directory(directory_path):
    try:
        if os.path.exists(directory_path):
            os.rmdir(directory_path)
            print(f"'{directory_path}' has been deleted.")
        else:
            print(f"Error: Directory '{directory_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting directory: {e}")

# - Deletes a directory and its contents
def delete_directory_and_contents(directory_path):
    try:
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            print(f"'{directory_path}' and its contents have been deleted.")
        else:
            print(f"Error: Directory '{directory_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting directory: {e}")

# 4. Sending Files to the Trash with `send2trash`
# - Moves files and folders to the recycle bin/trash
def send_to_trash(file_path):
    try:
        if os.path.exists(file_path):
            send2trash.send2trash(file_path)
            print(f"'{file_path}' has been moved to the trash.")
        else:
            print(f"Error: File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error sending file to trash: {e}")

# 5. Walking a Directory Tree with `os.walk()`
# - Prints the directory tree starting from the given folder
def walk_directory_tree(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'The current folder is: {foldername}')
        for subfolder in subfolders:
            print(f'SUBFOLDER OF {foldername}: {subfolder}')
        for filename in filenames:
            print(f'FILE INSIDE {foldername}: {filename}')
        print('')

# 6. Compressing Files with `zipfile` Module
# - Creates a ZIP file
def create_zip(zip_name, files_to_compress):
    try:
        with zipfile.ZipFile(zip_name , 'w') as new_zip:
            for file in files_to_compress:
                new_zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
        print(f"Created ZIP file '{zip_name}' containing specified files.")
    except Exception as e:
        print(f"Error creating ZIP file: {e}")

# - Adds files to an existing ZIP file
def add_to_zip(zip_name, files_to_add):
    try:
        with zipfile.ZipFile(zip_name, 'a') as existing_zip:
            for file in files_to_add:
                existing_zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
        print(f"Added files to '{zip_name}'.")
    except Exception as e:
        print(f"Error adding to ZIP file: {e}")

# - Extracts files from a ZIP archive
def extract_zip(zip_name, extract_to):
    try:
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted '{zip_name}' to '{extract_to}'.")
    except Exception as e:
        print(f"Error extracting ZIP file: {e}")

# - Lists files in a ZIP archive
def list_zip_contents(zip_name):
    try:
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            print(zip_ref.namelist()) 
            return zip_ref.namelist()
    except Exception as e:
        print(f"Error listing ZIP file contents: {e}")
        return []

