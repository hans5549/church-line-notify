import json
import requests
from pathlib import Path


class LineNotifySetting:
    def __init__(self, room1_token: str, notify_url: str):
        self.room1_token = room1_token
        self.notify_url = notify_url

    @property
    def get_room1_token(self):
        return self.room1_token

    @property
    def get_notify_url(self):
        return self.notify_url


def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading '{file_path}': {str(e)}")

    return {}  # Return an empty dictionary (empty JSON object) in case of any error


def init_line_notify_setting():
    setting_path = Path(__file__).parent.parent / "config" / "app_setting.json"
    setting = load_config(setting_path)
    if setting:
        room1_token = setting["Line"]["Notify"]["Token"]["room01"]
        notify_url = setting["Line"]["Notify"]["Url"]
        return LineNotifySetting(room1_token, notify_url)
    else:
        return None


def send_line_notify(message):
    line_notify_setting = init_line_notify_setting()
    if line_notify_setting is not None:
        try:
            line_notify_url = line_notify_setting.notify_url

            headers = {
                'Authorization': 'Bearer ' + line_notify_setting.room1_token
            }

            data = {
                'message': message
            }

            requests.post(line_notify_url, headers=headers, data=data)
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
