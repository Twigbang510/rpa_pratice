# Chapter 14: Working with google sheets (NEED MORE PRATICE WITH MORE METHODS)
import ezsheets

# 1. Authenticating and Connecting to Google Sheets
def connect_to_google_sheet(sheet_id=None, sheet_name=None):
    try:
        if sheet_id:
            sheet = ezsheets.Spreadsheet(sheet_id)
        elif sheet_name:
            sheet = ezsheets.createSpreadsheet(sheet_name)
        else:
            print("Please provide either a sheet ID or a sheet name.")
            return None
        print(f"Connected to Google Sheet: {sheet.title}")
        return sheet
    except Exception as e:
        print(f"Error connecting to Google Sheet: {e}")
        return None

# 2. Listing All Google Sheets in the Account
def list_all_sheets():
    sheets = ezsheets.listSpreadsheets()
    print("List of Google Sheets:")
    for sheet_id, title in sheets.items():
        print(f"Title: {title}, ID: {sheet_id}")
    return sheets

# 3. Reading Data from a Worksheet
def read_gsheet_data(sheet, sheet_title=None):
    try:
        if sheet_title:
            worksheet = sheet[sheet_title]
        else:
            worksheet = sheet[0]  # Default to the first sheet
        data = worksheet.getRows()
        print(f"Data in worksheet '{worksheet.title}':")
        for row in data:
            print(row)
        return data
    except Exception as e:
        print(f"Error reading data from worksheet: {e}")
        return None

# 4. Writing Data to a Cell in the Worksheet
def write_gsheet_data(sheet, row, column, value, sheet_title=None):
    try:
        if sheet_title:
            worksheet = sheet[sheet_title]
        else:
            worksheet = sheet[0]
        worksheet.updateRow(row, [value] if isinstance(value, str) else value)
        print(f"Updated row {row} in '{worksheet.title}' with '{value}'.")
    except Exception as e:
        print(f"Error writing data to worksheet: {e}")

# 5. Adding New Rows to the Worksheet
def append_row(sheet, data, sheet_title=None):
    try:
        if sheet_title:
            worksheet = sheet[sheet_title]
        else:
            worksheet = sheet[0]
        worksheet.appendRow(data)
        print(f"Appended row: {data} to worksheet '{worksheet.title}'.")
    except Exception as e:
        print(f"Error appending row: {e}")

# 6. Deleting Rows in the Worksheet
def delete_row(sheet, row_number, sheet_title=None):
    try:
        if sheet_title:
            worksheet = sheet[sheet_title]
        else:
            worksheet = sheet[0]
        worksheet.deleteRow(row_number)
        print(f"Deleted row {row_number} in '{worksheet.title}'.")
    except Exception as e:
        print(f"Error deleting row: {e}")

# 7. Downloading Google Sheet as a File
def download_as_excel(sheet, file_name):
    try:
        sheet.downloadAsExcel(file_name)
        print(f"Downloaded Google Sheet as '{file_name}'.")
    except Exception as e:
        print(f"Error downloading sheet as Excel: {e}")

# 8. Creating a New Google Sheet
def create_new_google_sheet(sheet_name):
    try:
        new_sheet = ezsheets.createSpreadsheet(sheet_name)
        print(f"Created new Google Sheet: '{new_sheet.title}'.")
        return new_sheet
    except Exception as e:
        print(f"Error creating new Google Sheet: {e}")
        return None

# 9. Deleting a Google Sheet
def delete_google_sheet(sheet):
    try:
        sheet.delete()
        print(f"Deleted Google Sheet: '{sheet.title}'.")
    except Exception as e:
        print(f"Error deleting Google Sheet: {e}")

