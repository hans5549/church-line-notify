import json
from line_module import send_line_notify
from pathlib import Path
from google_sheet_module import get_sheet_data


def load_config(file_path):
    with Path(file_path).open("r") as file:
        return json.load(file)


def main():
    data = get_sheet_data()
    message = 'google sheet data: ' + data

    send_line_notify(message)


if __name__ == "__main__":
    main()
