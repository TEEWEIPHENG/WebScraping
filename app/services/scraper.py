import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import socket
import ipaddress

def _is_valid_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError("Invalid URL format")

def _is_public_ip(url: str) -> None:
    hostname = urlparse(url).hostname
    ip = socket.gethostbyname(hostname)
    if ipaddress.ip_address(ip).is_private:
        raise ValueError("Private or internal IP not allowed")

def scrape_url(url: str) -> dict:
    _is_valid_url(url)
    _is_public_ip(url)

    #send request to the url
    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "FastAPI-Scraper/1.0"
        }
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    return {
        "url": url,
        "title": soup.title.string.strip() if soup.title else None,
        "total_links": len(soup.find_all("a"))
    }
