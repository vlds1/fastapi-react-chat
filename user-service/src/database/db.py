from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from src.config import DB_URL

engine = create_async_engine(DB_URL)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session
