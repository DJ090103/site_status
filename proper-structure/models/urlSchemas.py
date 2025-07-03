from pydantic import BaseModel, Field

class URLCheckResponse(BaseModel):
    url: str
    status: int
    checked_at: str
    id: str | None = Field(default=None, alias="_id") 

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
