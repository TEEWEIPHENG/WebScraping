import httpx
from bs4 import BeautifulSoup
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.scrape import ScrapeResult

async def scrape_and_save(url: str, db: AsyncSession) -> dict:
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(url)
        r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")

    data = ScrapeResult(
        url=url,
        title=soup.title.string.strip() if soup.title else None,
        total_links=len(soup.find_all("a"))
    )

    print(f"Scraping URL: {url}")
    print(f"Database session: {db}")
    db.add(data)
    await db.commit()
    await db.refresh(data)

    return {
        "id": data.id,
        "url": data.url,
        "title": data.title,
        "total_links": data.total_links
    }
