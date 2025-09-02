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
        fetched_characters = 0
        fetched_films = 0
        # fetched_starships = 0
        async with httpx.AsyncClient() as client:
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
                        if created_char:
                            fetched_characters += 1
                    except (IntegrityError, SQLAlchemyError):
                        continue
                    for film_url in character["films"]:
                        film_response = await client.get(film_url)
                        film_results = film_response.json()
                        for film in film_results:
                            try:
                                created_film = \
                                    await FilmService.create_film(
                                        session,
                                        film_swapi_to_dto(film))
                                if created_film:
                                    fetched_films += 1
                                if created_film not in created_char.films:
                                    created_char.films.append(created_film)
                            except (IntegrityError, SQLAlchemyError):
                                continue
                    # for ship_url in character["starships"]:
                    #     ship_response = await client.get(ship_url)
                    #     ship_results = ship_response.json()
                    #     for starship in ship_results:
                    #         try:
                    #             created_ship = await \
                    #                 StarshipService.create_starship(
                    #                     session,
                    #                     starship_swapi_to_dto(starship))
                    #             if created_ship:
                    #                 fetched_starships += 1
                    #             if created_ship not in created_char.starships:
                    #                 created_char.starships.append(created_ship)
                    #         except (IntegrityError, SQLAlchemyError):
                    #             continue
                url = results.get("next")
        return fetched_characters, fetched_films

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
