from pydantic import BaseModel
from typing import Optional

class ScrapeResponse(BaseModel):
    url: str
    title: Optional[str]
    total_links: int
