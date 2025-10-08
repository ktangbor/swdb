from dataclasses import dataclass
from datetime import datetime


@dataclass
class CharacterBaseDTO:
    name: str
    birth_year: str
    gender: str
    url: str
    eye_color: str | None
    hair_color: str | None
    height: str | None
    mass: str | None
    skin_color: str | None
    homeworld: list | None
    species: list | None
    vehicles: list | None

    @staticmethod
    def model_to_dto(model_data) -> "CharacterDTO":
        fields = {f.name for f in
                  CharacterBaseDTO.__dataclass_fields__.values()}
        data = {k: getattr(model_data, k) for k in fields if
                hasattr(model_data, k)}
        return CharacterBaseDTO(**data)


@dataclass
class CharacterCreate(CharacterBaseDTO):
    pass


@dataclass
class CharacterInDB(CharacterBaseDTO):
    id: int
    created: datetime
    edited: datetime

    @staticmethod
    def model_to_dto(model_data) -> "CharacterInDB":
        fields = {f.name for f in
                  CharacterInDB.__dataclass_fields__.values()}
        data = {k: getattr(model_data, k) for k in fields if
                hasattr(model_data, k)}
        return CharacterInDB(**data)


@dataclass
class CharacterPublic(CharacterInDB):
    created: datetime
    edited: datetime

    @staticmethod
    def model_to_dto(model_data) -> "CharacterPublic":
        fields = {f.name for f in
                  CharacterPublic.__dataclass_fields__.values()}
        data = {k: getattr(model_data, k) for k in fields if
                hasattr(model_data, k)}
        return CharacterPublic(**data)
