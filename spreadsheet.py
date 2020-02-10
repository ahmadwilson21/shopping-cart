
from dotenv import load_dotenv
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

#load_dotenv()


#Custom function that returns a list of dictionaries from a google sheet
def get_spreadsheet():
    
    DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
    SHEET_NAME = os.environ.get("SHEET_NAME", "Products")

    #
    # AUTHORIZATION
    #
    #json_path = os.environ.get("SHEETS_JSON","OOPS")
    CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google_api_credentials.json")

    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

    #
    # READ SHEET VALUES
    #

    client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

    doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>

    print("-----------------")
    print("SPREADSHEET:", doc.title)
    print("-----------------")

    sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

    rows = sheet.get_all_records() #> <class 'list'>
    return sheet
    """
    DOCUMENT_ID = os.environ.get("NEW_SHEET_ID", "OOPS")
    SHEET_NAME = os.environ.get("SHEET_NAME", "Products")

    #
    # AUTHORIZATION
    #

    CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "sheets-test-267401-1f8951c41319.json")

    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

    #
    # READ SHEET VALUES
    #

    client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

    doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>

    print("-----------------")
    print("SPREADSHEET:", doc.title)
    print("-----------------")

    sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

    rows = sheet.get_all_records() #> <class 'list'>

    for row in rows:
        print(row) #> <class 'dict'>

    #
    # WRITE VALUES TO SHEET
    #

    next_id = len(rows) + 1 # TODO: should change this to be one greater than the current maximum id value

    next_object = {
        "id": next_id,
        "name": f"Product {next_id}",
        "aisle": "dairy",
        "department": "snacks",
        "price": 4.99,
        #"availability_date": "2019-01-01"
    }

    next_row = list(next_object.values()) #> [13, 'Product 13', 'snacks', 4.99, '2019-01-01']

    next_row_number = len(rows) + 2 # number of records, plus a header row, plus one

    response = sheet.insert_row(next_row, next_row_number)

    print("-----------------")
    print("NEW RECORD:")
    print(next_row)
    print("-----------------")
    print("RESPONSE:")
    print(type(response)) #> dict
    print(response) #> {'spreadsheetId': '___', 'updatedRange': '___', 'updatedRows': 1, 'updatedColumns': 5, 'updatedCells': 5}

    """