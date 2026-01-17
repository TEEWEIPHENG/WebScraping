from fastapi import APIRouter, HTTPException, Query
from app.services.scraper import scrape_url
from app.schemas.scrape import ScrapeResponse

router = APIRouter()

@router.get("/scrape", response_model=ScrapeResponse)
def scrape_endpoint(
    url: str = Query(..., description="Public URL to scrape")
):
    try:
        return scrape_url(url)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
