from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from motor import motor_asyncio
from app.cores.config import settings


mysql_engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=mysql_engine)

mongodb_engine = motor_asyncio.AsyncIOMotorClient(settings.MONGO_DATABASE_URL)
mongodb_session = mongodb_engine.city



Base = declarative_base()
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_mongo_db():
    collection = mongodb_session.get_collection("programs")
    try:
        yield collection
    finally:
        collection