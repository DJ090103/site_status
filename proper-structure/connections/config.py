# connection/config.py
import json
import logging
import os

logger = logging.getLogger(__name__)

class Config:
    def __init__(self):
        self.mongo_url = None

    def reload_from_secrets_file(self):
        secrets_file_path = os.environ.get("SECRETS_FILE")
        if not secrets_file_path or not os.path.exists(secrets_file_path):
            logger.error("SECRETS_FILE env var missing or file not found")
            raise FileNotFoundError("Secrets file path is invalid")

        try:
            with open(secrets_file_path, "r") as f:
                config_data = json.load(f)
        except Exception as e:
            logger.error("FAILED to load Secrets file: %s", e)
            raise

        self.mongo_url = config_data.get(
            "MONGODB_CONNECTION_STRING", "mongodb://localhost:27017"
        )

# Global config object
config = Config()
config.reload_from_secrets_file()