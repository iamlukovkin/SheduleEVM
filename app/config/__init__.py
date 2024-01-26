"""All configurations of application."""
import json


json_path: str = 'config/settings.json'

with open(json_path, "r", encoding='utf-8') as json_file:
    configurations: dict = json.load(json_file)
    json_file.close()

APP_NAME: str = configurations['APP']['Name']
APP_SHORT_NAME: str = configurations['APP']['ShortName']
APP_RESOLUTION: dict = configurations['APP']['Window']
APP_ICON: str = configurations['APP']['Icon']

FOLDERS: dict = configurations['Folders']
DATABASE: dict[str, str] = configurations['Database']