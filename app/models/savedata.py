from pydantic import BaseModel
from typing import Optional

class SaveData(BaseModel):
    url: str
    title: Optional[str]
    total_links: int