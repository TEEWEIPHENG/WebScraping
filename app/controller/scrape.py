from fastapi import APIRouter, HTTPException, Query
from app.services.scraper import scrape_url_async
from app.schemas.scrape import ScrapeResponse

router = APIRouter()

@router.get("/scrape", response_model=ScrapeResponse)
async def scrape_endpoint(
    url: str = Query(..., description="Public URL to scrape")
):
    try:
        return await scrape_url_async(url)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
