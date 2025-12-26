import json
from pathlib import Path


class ConfigReader:
    CONFIG_PATH = Path(__file__).parent / "config.json"

    def __init__(self, path: Path = CONFIG_PATH):
        with open(path, "r", encoding="utf-8") as f:
            self._data = json.load(f)

    @property
    def base_urls(self) -> dict:
        return self._data["base_urls"]

    @property
    def timeouts(self) -> dict:
        return self._data["timeouts"]

    @property
    def browser(self) -> dict:
        return self._data["browser"]
