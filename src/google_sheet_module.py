import pandas as pd
import pygsheets
import datetime
from pathlib import Path


class ActiveInformation:
    def __init__(self, date: str, time: str, processor_01: str, processor_02: str, processor_03: str, processor_04: str):
        self.date = date
        self.time = time
        self.processor_01 = processor_01
        self.processor_02 = processor_02
        self.processor_03 = processor_03
        self.processor_04 = processor_04

    @property
    def get_date(self):
        return self.date

    @property
    def get_time(self):
        return self.time

    @property
    def get_processor(self):
        return ', '.join([self.processor_01, self.processor_02, self.processor_03, self.processor_04])



def authorize_google_sheet(credentials_path):
    return pygsheets.authorize(service_file=credentials_path)


def get_cell_value(client, sheet_url, cell):
    spreadsheet = client.open_by_url(sheet_url)
    worksheet = spreadsheet.sheet1
    return worksheet.get_value(cell)


def get_all_records(client, sheet_url):
    spreadsheet = client.open_by_url(sheet_url)
    worksheet = spreadsheet.sheet1
    return worksheet.get_all_records()


def get_target_row_index_list(df, target_column_name, target_value):
    return df[df[target_column_name] == target_value].index


def get_sheet_data():
    credentials_path = Path(__file__).parent.parent / "config" / "credentials.json"
    sheet_url = 'https://docs.google.com/spreadsheets/d/1IjQF2g7e58uf5vaNxy4cuXjhoNX8zzfKxjFCqVoWgAs/edit?usp=sharing'
    now_date = datetime.datetime.now().strftime('%Y-%m-%d')

    gc_client = authorize_google_sheet(credentials_path)
    df = pd.DataFrame(get_all_records(gc_client, sheet_url))
    target_row_row_index_list = get_target_row_index_list(df, '日期', now_date)

    return target_row_row_index_list
