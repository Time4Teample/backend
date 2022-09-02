from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"Hello": "Scraper"}

@app.get("/scrape")
async def scrape():
    return {"Start": "Scraper"}

