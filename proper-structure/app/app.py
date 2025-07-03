from fastapi import FastAPI, Request
from services.service_status import check_site_status
from models.urlSchemas import URLCheckResponse

app = FastAPI()

@app.post("/check-url", response_model=URLCheckResponse)
async def check_url(request: Request):
    data = await request.json()
    url = data.get("url")
    return check_site_status(url)
