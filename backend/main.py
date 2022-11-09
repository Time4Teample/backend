from fastapi import FastAPI

from app.apis import router
from app.cores.config import settings
from app.db.session import SessionLocal
from app.db.database import init_db

def init() -> None:
    database = SessionLocal()
    init_db(database)

app = FastAPI()
app.include_router(router.router, prefix=settings.API_V1_STR)


@app.get("/")
async def main():
    return {"Hello": "Scraper"}

@app.get("/scrape")
async def scrape():
    return {"Start": "Scraper"}

@app.get("/run")
async def run():
    return {"Status": "Running"}

init()