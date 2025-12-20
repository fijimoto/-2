import json
from pathlib import Path


class ConfigReader:
    _config = None

    @staticmethod
    def get_config():
        if ConfigReader._config is None:
            config_path = Path(__file__).parent / "config.json"
            with open(config_path, "r", encoding="utf-8") as f:
                ConfigReader._config = json.load(f)
        return ConfigReader._config

    @staticmethod
    def get(key: str):
        """Получить значение по ключу"""
        return ConfigReader.get_config().get(key)
