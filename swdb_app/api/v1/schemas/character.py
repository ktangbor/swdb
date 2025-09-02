from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class CharacterBase(BaseModel):
    name: str = Field(..., description="The name of this person")
    birth_year: str = Field(..., description="The birth year of the person, using the in-universe standard of BBY or ABY - Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin is a battle that occurs at the end of Star Wars episode IV: A New Hope.")
    gender: str = Field(...)
    url: str = Field(...)
    eye_color: str | None = Field(...)
    hair_color: str | None = Field(...)
    height: str | None = Field(...)
    mass: str | None = Field(...)
    skin_color: str | None = Field(...)
    homeworld: list | None = Field(...)
    species: list | None = Field(...)
    vehicles: list | None = Field(...)


class CharacterCreate(CharacterBase):
    pass


class CharacterRead(CharacterBase):
    id: int
    created: datetime
    edited: datetime
    model_config = ConfigDict(from_attributes=True)


class CharacterPublic(CharacterRead):
    created: datetime
    edited: datetime


class CharacterFilter(BaseModel):
    name: str | None = None
