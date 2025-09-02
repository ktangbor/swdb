from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from swdb_app.db.session import AsyncSessionLocal


async def get_async_session() -> AsyncGenerator[AsyncSession ,None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
