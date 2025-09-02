from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from swdb_app.dto.character import CharacterCreate
from swdb_app.models.character import Character


class CharacterRepository:

    @staticmethod
    async def get_all(session: AsyncSession,
                      offset: int = 0,
                      limit: int = 100) -> list[Character]:
        result = await session.execute(select(Character)
                                       .offset(offset)
                                       .limit(limit))
        return result.scalars().all()

    @staticmethod
    async def create(session: AsyncSession,
                     char_dto: CharacterCreate) -> Character:
        char_db = Character(**char_dto.__dict__)
        session.add(char_db)
        await session.flush()
        return char_db

    @staticmethod
    async def get_filtered(session: AsyncSession,
                           filters: dict) -> list[Character]:
        query = select(Character)
        for field, value in filters.items():
            if hasattr(Character, field) and value is not None:
                query = query.where(
                    getattr(Character, field) == value)
        result = await session.execute(query)
        return result.scalars().all()
