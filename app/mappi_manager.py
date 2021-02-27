import json


class MappiManager:
    def __init__(self, mappi_file):
        self.mappi_file = mappi_file
        self._mappi = self._load_mappi_json()

    def _load_mappi_json(self):
        with open(self.mappi_file) as fp:
            data = json.load(fp)
        return data

    def reload_mappi_dict(self):
        self._mappi = self._load_mappi_json()

    def get_long_url(self, nickname):
        url = self._mappi.get(nickname)
        return url
