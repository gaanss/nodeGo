import yaml
from typing import Dict
from loguru import logger

class ConfigLoader:
    @staticmethod
    def load_config(config_path: str = "settings.yaml") -> Dict:
        try:
            with open(config_path, "r") as file:
                config = yaml.safe_load(file)
            logger.info("Конфігурацію успішно завантажено")
            return config
        except Exception as e:
            logger.error(f"Помилка завантаження конфігурації: {e}")
            raise 