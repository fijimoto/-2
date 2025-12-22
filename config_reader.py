import json
from pathlib import Path


class ConfigReader:
    _config = None

    @staticmethod
    def get_config():
        """Загружаем конфиг один раз и кэшируем"""
        if ConfigReader._config is None:
            config_path = Path(__file__).parent / "config.json"
            with open(config_path, encoding="utf-8") as file:
                ConfigReader._config = json.load(file)
        return ConfigReader._config

    @staticmethod
    def get(key):
        """Получаем значение по ключу"""
        return ConfigReader.get_config().get(key)
