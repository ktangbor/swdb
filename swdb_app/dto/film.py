from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class FilmBaseDTO:
    title: str
    episode_id: str
    release_date: date
    url: str
    opening_crawl: str | None
    director: str | None
    producer: str | None
    species: list | None
    vehicles: list | None
    planets: list | None

    @staticmethod
    def model_to_dto(model_data) -> "FilmDTO":
        fields = {f.name for f in
                  FilmBaseDTO.__dataclass_fields__.values()}
        data = {k: getattr(model_data, k) for k in fields if
                hasattr(model_data, k)}
        return FilmBaseDTO(**data)


@dataclass
class FilmCreate(FilmBaseDTO):
    pass


@dataclass
class FilmInDB(FilmBaseDTO):
    id: int
    created: datetime
    edited: datetime

    @staticmethod
    def model_to_dto(model_data) -> "FilmInDB":
        fields = {f.name for f in
                  FilmInDB.__dataclass_fields__.values()}
        data = {k: getattr(model_data, k) for k in fields if
                hasattr(model_data, k)}
        return FilmInDB(**data)


@dataclass
class FilmPublic(FilmInDB):
    created: datetime
    edited: datetime

    @staticmethod
    def model_to_dto(model_data) -> "FilmPublic":
        fields = {f.name for f in
                  FilmPublic.__dataclass_fields__.values()}
        data = {k: getattr(model_data, k) for k in fields if
                hasattr(model_data, k)}
        return FilmPublic(**data)
