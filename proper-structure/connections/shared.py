from pymongo import MongoClient
from connections.config import config  # Global Config instance

# ✅ Use the correct attribute name
client = MongoClient(config.mongo_url, tls=False)

db = client["site_status"]

submitted_urls_collection = db["submitted_urls"]
failed_checks_collection = db["failed_checks"]
