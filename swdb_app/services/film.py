from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import httpx

from swdb_app.models.film import Film
from swdb_app.dto.film import FilmCreate, FilmInDB
from swdb_app.repos.film import FilmRepository
from swdb_app.services.character import CharacterService
from swdb_app.utils.endpoints import SWAPI_FILMS_LIST_ENDPOINT
from swdb_app.utils.helper import (film_swapi_to_dto,
                                   character_swapi_to_dto)


class FilmService:

    @staticmethod
    async def create_film(
            session: AsyncSession,
            film: FilmCreate) -> Film:
        return await FilmRepository.create(session, film)

    @staticmethod
    async def fetch_all(session: AsyncSession) -> (int, int):
        fetched_films = 0
        fetched_characters = 0
        async with (httpx.AsyncClient() as client):
            url = SWAPI_FILMS_LIST_ENDPOINT
            while url:
                response = await client.get(url)
                results = response.json()
                for film in results:
                    try:
                        created_film = \
                            await FilmService.create_film(
                                session,
                                film_swapi_to_dto(film))
                        if created_film:
                            fetched_films += 1
                    except (IntegrityError, SQLAlchemyError):
                        continue
                    for char_url in film["characters"]:
                        char_response = await client.get(char_url)
                        char_results = char_response.json()
                        for char in char_results:
                            try:
                                created_char = await \
                                    CharacterService.create_character(
                                        session,
                                        character_swapi_to_dto(char))
                                if created_char:
                                    fetched_characters += 1
                                if created_char not in \
                                        created_film.characters:
                                    created_film.characters.append(
                                        created_char)
                            except (IntegrityError, SQLAlchemyError):
                                continue
                url = results.get("next")
        return fetched_characters, fetched_films

    @staticmethod
    async def get_all(session: AsyncSession,
                      offset: int = 0,
                      limit: int = 100) -> list[FilmInDB]:
        films = await FilmRepository.get_all(
            session, offset, limit)
        return [FilmInDB.model_to_dto(film)
                for film in films]

    @staticmethod
    async def search(session: AsyncSession,
                     filters: dict) -> list[FilmInDB]:
        films = await FilmRepository.get_filtered(
            session, filters)
        return [FilmInDB.model_to_dto(film)
                for film in films]
