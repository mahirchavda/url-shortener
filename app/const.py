import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

MAPPI_FILE = os.path.join(CURRENT_DIR, "url_mapping.regex")
NICKNAME_FILE = os.path.join(CURRENT_DIR, "nicknames.json")
LOG_FILE = os.path.join(CURRENT_DIR, "url-shortener.log")
