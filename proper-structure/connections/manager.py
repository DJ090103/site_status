import sys
from loguru import logger
from pymongo import MongoClient
from connections.config import Config

class Manager:
    SERVICE_NAME = "site_status_check"

    def __init__(self):
        self.config = Config()

        # Setup custom loguru logging
        for handler in list(logger._core.handlers):
            logger.remove(handler)

        log_level = "INFO"
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | "
            "<level>{level: <8}</level> | "
            "<yellow>Line {line: >4} ({file}):</yellow> {message}"
        )
        logger.add(
            sys.stdout,
            level=log_level,
            format=log_format,
            colorize=True,
            backtrace=True,
            diagnose=True,
        )

        logger.info(f"{self.SERVICE_NAME} initialized")

        # ❗️Fix: Call this BEFORE using connection string
        self.reestablish_connections()

        # ✅ Now safe to use connection string
        self.client = MongoClient(
            self.config.mongodb_connection_string,
            tls=False  # Set True if needed
        )

        self.db = self.client["w3status"]

        # Import after client setup to avoid circular import
        from services.service_status import ServiceStatus
        self.service_status = ServiceStatus()

    def reestablish_connections(self):
        self.config.reload_from_secrets_file()
