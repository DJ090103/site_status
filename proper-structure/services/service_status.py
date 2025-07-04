# services/service_status.py

import requests
from datetime import datetime
from bson import ObjectId
from connections.shared import submitted_urls_collection, failed_checks_collection
from models.urlSchemas import URLCheckResponse  # ✅ Import the schema

def check_site_status(url: str) -> URLCheckResponse:
    try:
        response = requests.get(url)
        status_code = response.status_code
    except requests.RequestException:
        status_code = 0

    result = {
        "url": url,
        "status": status_code,
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    insert_result = submitted_urls_collection.insert_one(result)
    result["_id"] = str(insert_result.inserted_id)  # Convert ObjectId to str

    if status_code != 200:
        failed_checks_collection.insert_one(result)

    return URLCheckResponse(**result)  # ✅ Return Pydantic response
