from fastapi import FastAPI
from scraper.runner import runner
app = FastAPI()

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