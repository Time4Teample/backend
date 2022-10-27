from fastapi import FastAPI

from app.apis.api import router
from app.cores.config import settings
from app.db.session import SessionLocal
from app.db.database import init_db
from scraper.runner import runner

def init() -> None:
    database = SessionLocal()
    init_db(database)

app = FastAPI()
app.include_router(router, prefix=settings.API_V1_STR)


@app.get("/")
async def main():
    return {"Hello": "Scraper"}

@app.get("/scrape")
async def scrape():
    return {"Start": "Scraper"}

@app.get("/run")
async def run():
    runner()
    return {"Status": "Running"}

init()