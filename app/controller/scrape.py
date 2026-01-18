from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.scraper import scrape_and_save
from app.schemas.scrape import ScrapeResponse

router = APIRouter()

@router.get("/scrape", response_model=ScrapeResponse)
async def scrape(
    url: str,
    db: AsyncSession = Depends(get_db)
):
    return await scrape_and_save(url, db)
