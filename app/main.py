from fastapi import FastAPI
from app.controller.scrape import router as scrape_router
from app.db.session import engine
from app.models.scrape import Base

def create_app() -> FastAPI:
    app = FastAPI(
        title="Web Scraper Service",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )


    # Initialize database tables on startup
    @app.on_event("startup")
    async def startup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("✓ Database tables initialized")

    # Register routers
    app.include_router(
        scrape_router,
        prefix="/api/v1",
        tags=["Scraping"]
    )

    return app

app = create_app()
