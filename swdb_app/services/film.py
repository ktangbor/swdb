from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import httpx

from swdb_app.models.film import Film
from swdb_app.dto.film import FilmCreate, FilmInDB
from swdb_app.repos.film import FilmRepository
from swdb_app.utils.endpoints import SWAPI_FILMS_LIST_ENDPOINT
from swdb_app.utils.helper import film_swapi_to_dto


class FilmService:

    @staticmethod
    async def create_film(
            session: AsyncSession,
            film: FilmCreate) -> Film:
        return await FilmRepository.create(session, film)

    @staticmethod
    async def fetch_all(session: AsyncSession) -> (int, int):
        films = []
        async with (httpx.AsyncClient(verify=False) as client):
            url = SWAPI_FILMS_LIST_ENDPOINT
            while url:
                response = await client.get(url)
                response_dict = response.json()
                for film in response_dict["results"]:
                    try:
                        created_film = \
                            await FilmService.create_film(
                                session,
                                film_swapi_to_dto(film))
                        films.append((created_film, film.get("characters")))
                    except (IntegrityError, SQLAlchemyError) as e:
                        print(str(e))
                        continue
                url = response_dict.get("next")
        return films

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
