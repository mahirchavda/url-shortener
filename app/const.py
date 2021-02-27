import os

PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_DIR = os.path.join(PROJECT_ROOT_DIR, "app")
CONFIG_DIR = os.path.join(PROJECT_ROOT_DIR, "config")

MAPPI_FILE = os.path.join(CONFIG_DIR, "url_mapping.regex")
NICKNAME_FILE = os.path.join(CONFIG_DIR, "nicknames.json")
LOG_FILE = os.path.join(PROJECT_ROOT_DIR, "url-shortener.log")
