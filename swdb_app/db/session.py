from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (AsyncSession, create_async_engine,
                                    async_sessionmaker)
from swdb_app.core.config import settings


engine = create_async_engine(settings.ASYNC_DB_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, autoflush=False)
Base = declarative_base()
