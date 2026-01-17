from fastapi import FastAPI
from app.controller.scrape import router as scrape_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Web Scraper Service",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # Register routers
    app.include_router(
        scrape_router,
        prefix="/api/v1",
        tags=["Scraping"]
    )

    return app

app = create_app()
