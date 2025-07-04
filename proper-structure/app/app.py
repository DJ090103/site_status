# app.py
from fastapi import FastAPI
from models.urlSchemas import URLCheckRequest, URLCheckResponse
from services.service_status import check_site_status

app = FastAPI()

@app.post("/check-url", response_model=URLCheckResponse)
async def check_url(payload: URLCheckRequest):
    return check_site_status(payload.url)
