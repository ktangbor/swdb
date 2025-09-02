from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from swdb_app.dto.film import FilmCreate
from swdb_app.models.film import Film


class FilmRepository:

    @staticmethod
    async def get_all(session: AsyncSession,
                      offset: int = 0,
                      limit: int = 100) -> list[Film]:
        result = await session.execute(select(Film)
                                       .offset(offset)
                                       .limit(limit))
        return result.scalars().all()

    @staticmethod
    async def create(session: AsyncSession,
                     char_dto: FilmCreate) -> Film:
        char_db = Film(**char_dto.__dict__)
        session.add(char_db)
        await session.flush()
        return char_db

    @staticmethod
    async def get_filtered(session: AsyncSession,
                           filters: dict) -> list[Film]:
        query = select(Film)
        for field, value in filters.items():
            if hasattr(Film, field) and value is not None:
                query = query.where(
                    getattr(Film, field) == value)
        result = await session.execute(query)
        return result.scalars().all()
