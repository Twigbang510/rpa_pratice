# Chapter 16: Working with CSV files amd json data
import csv
import json

# 1. Reading a CSV File
def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            print(f"Data from CSV '{file_path}':")
            for row in data:
                print(row)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# 2. Writing to a CSV File
def write_csv(file_path, data):
    try:
        with open(file_path, mode='w+', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
            print(f"Data written to CSV '{file_path}' successfully.")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

# 3. Reading a CSV File with DictReader
def read_csv_as_dict(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            print(f"Data from CSV '{file_path}' using DictReader:")
            for row in data:
                print(row)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# 4. Writing to a CSV File with DictWriter
def write_csv_as_dict(file_path, fieldnames, data):
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames,delimiter=';')
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            print(f"Data written to CSV '{file_path}' using DictWriter successfully.")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")


# 5. Reading a JSON File
def read_json(file_path):
    try:
        with open(file_path, mode='r') as file:
            data = json.load(file)
            print(f"Data from JSON '{file_path}':")
            print(json.dumps(data, indent=4))
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# 6. Writing to a JSON File
def write_json(file_path, data):
    try:
        with open(file_path, mode='w') as file:
            json.dump(data, file, indent=4)
            print(f"Data written to JSON '{file_path}' successfully.")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")

# 7. Updating JSON Data
def update_json(file_path, key, value):
    try:
        data = read_json(file_path)
        if data is not None:
            data[key] = value
            write_json(file_path, data)
            print(f"Updated key '{key}' in JSON '{file_path}' to '{value}'.")
    except Exception as e:
        print(f"Error updating JSON file: {e}")
