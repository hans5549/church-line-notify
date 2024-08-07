import pygsheets
from pathlib import Path


def authorize_google_sheet(credentials_path):
    return pygsheets.authorize(service_file=credentials_path)


def get_cell_value(client, sheet_url, cell):
    spreadsheet = client.open_by_url(sheet_url)
    worksheet = spreadsheet.sheet1
    return worksheet.get_value(cell)


def get_sheet_data():
    credentials_path = Path(__file__).parent.parent / "config" / "credentials.json"
    sheet_url = 'https://docs.google.com/spreadsheets/d/1IjQF2g7e58uf5vaNxy4cuXjhoNX8zzfKxjFCqVoWgAs/edit?usp=sharing'
    target_cell = 'B169'

    gc_client = authorize_google_sheet(credentials_path)
    cell_value = get_cell_value(gc_client, sheet_url, target_cell)

    return cell_value
