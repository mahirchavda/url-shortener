import re
import json

from errors import ShortURLNotFound
from log_manager import Logger

logger = Logger.get_logger("url-shortener")


class MappiManager:
    def __init__(self, nickname_file, mappi_file):
        self.nickname_file = nickname_file
        self.mappi_file = mappi_file
        self._build_mappi(nickname_file, mappi_file)

    @staticmethod
    def load_nickname(file):
        nickname = None
        with open(file) as fp:
            nickname = json.load(fp)
        return {key.strip(): val.strip().strip("/") for key, val in nickname.items()}

    @staticmethod
    def load_mappi(file):
        mappi = []
        with open(file) as fp:
            for line_no, line in enumerate(fp, start=1):
                line = line.strip()
                if not line:
                    continue
                if line.startswith("#"):
                    continue
                regex, url = map(lambda x: x.strip(), line.split("=>"))
                regex = regex.strip()
                url = url.strip()
                if regex and url:
                    mappi.append((regex, url))
                else:
                    logger.error(
                        "Invalid entry at (line no={}, content={})".format(
                            line_no, line
                        )
                    )
        return mappi

    def _build_mappi(self, nickname_file, mappi_file):
        self._nickname = self.load_nickname(nickname_file)
        raw_mappi = self.load_mappi(mappi_file)
        self._mappi = [
            (item1 + "(/)?$", item2.format(**self._nickname))
            for item1, item2 in raw_mappi
        ]

    def get_redirect_url(self, short_url):
        for regex, url in self._mappi:
            match = re.match(regex, short_url, re.IGNORECASE)
            if match:
                return url.format(**match.groupdict())
        else:
            raise ShortURLNotFound("{} Not found".format(short_url))
