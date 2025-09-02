from swdb_app.dto.character import CharacterCreate
from swdb_app.dto.film import FilmCreate


def character_swapi_to_dto(data: dict) -> CharacterCreate:
    return CharacterCreate(
        **{k: data.get(k)
           for k in CharacterCreate.__dataclass_fields__.keys()}
    )


def film_swapi_to_dto(data: dict) -> FilmCreate:
    return FilmCreate(
        **{k: data.get(k)
           for k in FilmCreate.__dataclass_fields__.keys()}
    )
