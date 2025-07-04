# models/urlSchemas.py
from pydantic import BaseModel, Field

# ✅ Request schema (only `url` expected from user)
class URLCheckRequest(BaseModel):
    url: str

# ✅ Response schema (what the API returns)
class URLCheckResponse(BaseModel):
    url: str
    status: int
    checked_at: str
    id: str | None = Field(default=None, alias="_id")  # use alias for MongoDB's _id

    class Config:
        populate_by_name = True  # ✅ Pydantic v2 fix
        from_attributes = True   # ✅ Pydantic v2 fix
