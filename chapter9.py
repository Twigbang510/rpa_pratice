# Chapter 9: Reading and Writing Files (Extended and Enhanced)
import os
import shutil
from pathlib import Path

# 1. Opening Files with `open()`
# Use `open()` to open a file and get a file object.
# Default mode is 'r' (read mode).
def open_file(file_path):
    try:
        return open(file_path, 'r')
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# 2. Reading Files
# - `read()`: Reads the entire content of the file as a string.
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Using `readlines()` to read the file as a list of lines.
def read_file_as_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# 3. Writing to Files
# - Use mode 'w' to write to a file. This will overwrite the existing file or create a new one if it doesn't exist.
def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file: {e}")

# - Use mode 'a' to append to the file without overwriting its content.
def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
    except Exception as e:
        print(f"Error appending to file: {e}")

# 4. Reading Files Line by Line
# Use a `for` loop to iterate over each line in the file.
def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')  # `end=''` prevents adding an extra newline
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# 5. Using `with` Statements to Open Files
# The `with` statement automatically closes the file after the nested block of code runs.
def read_file_with(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# 6. Writing List of Lines to a File
# Writes a list of lines to the specified file.
def write_lines_to_file(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            file.writelines(lines)
    except Exception as e:
        print(f"Error writing lines to file: {e}")

# 7. File Paths
# Returns the absolute path of the given file path.
def print_absolute_path(file_path):
    return os.path.abspath(file_path)

# 8. Working with Different File Modes
# Example using 'r+' to read and write to a file.
def read_and_write(file_path, additional_content):
    try:
        with open(file_path, 'r+') as file:
            content = file.read()
            print(f"Original content:\n{content}")
            file.write(additional_content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# Using `seek()` and `tell()` to navigate within a file.
def read_with_seek(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"Initial position: {file.tell()}")
            content = file.read(10)  # Read the first 10 characters
            print(f"After reading 10 characters: {file.tell()}")
            file.seek(0)  # Go back to the beginning
            print(f"After seek to start: {file.tell()}")
            print(file.read())  # Read the entire file again
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# 9. Checking If a File or Directory Exists
# Returns True if the specified file exists.
def check_file_exists(file_path):
    return os.path.exists(file_path)

# Returns True if the specified directory exists.
def check_directory_exists(directory_path):
    return os.path.isdir(directory_path)

# 10. Creating and Deleting Files and Directories
# Creates a new directory, if it does not already exist.
def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)

# Deletes the specified file if it exists.
def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"'{file_path}' has been deleted.")
        else:
            print(f"Error: File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# 11. Copying and Moving Files
# Copies a file from the source to the destination path.
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
    except FileNotFoundError:
        print(f"Error: File '{src}' not found.")

# Moves a file from the source to the destination path.
def move_file(src, dest):
    try:
        shutil.move(src, dest)
    except FileNotFoundError:
        print(f"Error: File '{src}' not found.")


# 12. Using `pathlib` for Path Operations
# Returns various information about the file path using `pathlib`.
def get_path_info(file_path):
    path = Path(file_path)
    exactly_path = {
        'absolute_path': path.resolve(),
        'name': path.name,
        'stem': path.stem,
        'suffix': path.suffix,
        'parent': path.parent,
        'exists': path.exists()
    }
    print(exactly_path)
    
