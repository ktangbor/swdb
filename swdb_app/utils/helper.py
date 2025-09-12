from swdb_app.dto.character import CharacterCreate
from swdb_app.dto.film import FilmCreate
from swdb_app.integrations.SWAPI.schemas import FilmIngest

def character_swapi_to_dto(data: dict) -> CharacterCreate:
    return CharacterCreate(
        **{k: data.get(k)
           for k in CharacterCreate.__dataclass_fields__.keys()}
    )


def film_swapi_to_dto(data: dict) -> FilmCreate:
    parsed_data = FilmIngest.model_validate(data)
    serialized_data = parsed_data.model_dump()
    return FilmCreate(**serialized_data)
