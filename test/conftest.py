import os
import sys
import pytest

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(CURRENT_DIR, "..", "app")
sys.path.append(os.path.join(APP_DIR))

import const
import mappi_manager


@pytest.fixture(scope="module")
def mappi_man():
    mm = mappi_manager.MappiManager(const.NICKNAME_FILE, const.MAPPI_FILE)
    return mm
