from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import requests

app = FastAPI()

class Siteinfo(BaseModel):
    siteurl: str

@app.post("/siteinfo")
def siteinfo(site: Siteinfo):
    print("📦 Incoming site object:", site)
    print("🔗 Extracted URL:", site.siteurl)

    try:
        response = requests.get(site.siteurl)
        status_code = response.status_code
    except requests.exceptions.RequestException as e:
        print("❌ Error while requesting:", e)
        status_code = 0  # Use a default value on failure

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "url": site.siteurl,
        "status": status_code,
        "checked_at": current_time
    }

