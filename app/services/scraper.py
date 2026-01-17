import httpx
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import socket
import ipaddress

def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError("Invalid URL format")

def _block_private_ip(url: str) -> None:
    hostname = urlparse(url).hostname
    ip = socket.gethostbyname(hostname)
    if ipaddress.ip_address(ip).is_private:
        raise ValueError("Private or internal IP not allowed")

async def scrape_url_async(url: str) -> dict:
    _validate_url(url)
    _block_private_ip(url)

    async with httpx.AsyncClient(
        timeout=10,
        headers={"User-Agent": "FastAPI-Scraper/1.0"}
    ) as client:
        response = await client.get(url)
        response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    return {
        "url": url,
        "title": soup.title.string.strip() if soup.title else None,
        "total_links": len(soup.find_all("a"))
    }
