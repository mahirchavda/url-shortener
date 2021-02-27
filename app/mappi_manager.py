import json


class MappiManager:
    def __init__(self, mappi_file):
        self.mappi_file = mappi_file
        self.reload_mappi_dict()

    def _load_mappi_json(self):
        with open(self.mappi_file) as fp:
            data = json.load(fp)
        return data

    def build_mappi(self, data):
        temp_mappi = {}
        for keys, val in data.items():
            for key in map(lambda x: x.strip(), keys.split(',')):
                temp_mappi[key] = val
        return temp_mappi

    def reload_mappi_dict(self):
        self._original_mappi = self._load_mappi_json()
        self._mappi = self.build_mappi(self._original_mappi)


