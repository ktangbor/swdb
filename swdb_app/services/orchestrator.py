from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from swdb_app.models.character import Character
from swdb_app.services.character import CharacterService
from swdb_app.services.film import FilmService
from swdb_app.utils.helper import character_swapi_to_dto
import httpx


class OrchestratorService:
    @staticmethod
    async def fetch_sync_films(session: AsyncSession):
        films = await FilmService.fetch_all(session)
        characters_count = 0

        for film, char_urls in films:
            for char_url in char_urls:
                # ideally we should check db first to avoid extra api calls
                async with (httpx.AsyncClient(verify=False) as client):
                    character_resp = await client.get(char_url)
                    character_json = character_resp.json()
                character_orm = await session.scalar(
                    select(Character).where(
                        Character.url == character_json["url"])
                )
                if character_orm is None:
                    character_dto = character_swapi_to_dto(character_json)
                    character_orm = await CharacterService.create_character(
                        session, character_dto)
                #  remove following, and replace with a repo that flushes
                #  changes and catches Integrity errors
                # if character not in film.characters:
                #     film.characters.append(character)
                #     characters_count += 1
        return characters_count, len(films)

    @staticmethod
    async def fetch_sync_characters(session: AsyncSession):
        characters = await CharacterService.fetch_all(session)
        films_count = 0

        for character, film_urls in characters:
            for film_url in film_urls:
                # ideally we should check db first to avoid extra api calls
                async with (httpx.AsyncClient(verify=False) as client):
                    film = await client.get(film_url).json()
                if film not in character.films:
                    character.films.append(film)
                    films_count += 1
        return len(characters), films_count
