from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import httpx

from swdb_app.models.character import Character
from swdb_app.dto.character import CharacterCreate, CharacterInDB
from swdb_app.repos.character import CharacterRepository
from swdb_app.services.film import FilmService
# from swdb_app.services.starship import StarshipService
from swdb_app.utils.endpoints import SWAPI_PEOPLE_LIST_ENDPOINT
from swdb_app.utils.helper import (character_swapi_to_dto,
                                   # starship_swapi_to_dto,
                                   film_swapi_to_dto)


class CharacterService:

    @staticmethod
    async def create_character(
            session: AsyncSession,
            character: CharacterCreate) -> Character:
        return await CharacterRepository.create(session, character)

    @staticmethod
    async def fetch_all(session: AsyncSession) -> (int, int):
        characters = []
        async with httpx.AsyncClient(verify=False) as client:
            url = SWAPI_PEOPLE_LIST_ENDPOINT
            while url:
                response = await client.get(url)
                results = response.json()
                for character in results:
                    try:
                        created_char = \
                            await CharacterService.create_character(
                                session,
                                character_swapi_to_dto(character))
                        characters.append((created_char, character["films"]))
                    except (IntegrityError, SQLAlchemyError):
                        continue
                url = results.get("next")
        return characters

    @staticmethod
    async def get_all(session: AsyncSession,
                      offset: int = 0,
                      limit: int = 100) -> list[CharacterInDB]:
        characters = await CharacterRepository.get_all(
            session, offset, limit)
        return [CharacterInDB.model_to_dto(char)
                for char in characters]

    @staticmethod
    async def search(session: AsyncSession,
                     filters: dict) -> list[CharacterInDB]:
        characters = await CharacterRepository.get_filtered(
            session, filters)
        return [CharacterInDB.model_to_dto(char)
                for char in characters]
