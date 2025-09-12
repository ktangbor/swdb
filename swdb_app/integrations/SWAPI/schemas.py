from pydantic import BaseModel, Field
from datetime import date


class FilmIngest(BaseModel):
    title: str
    episode_id: int
    release_date: date
    url: str
    opening_crawl: str | None
    director: str | None
    producer: str | None
    species: list[str] = Field(default_factory=list)
    vehicles: list[str] = Field(default_factory=list)
    planets: list[str] = Field(default_factory=list)


class CharacterIngest(BaseModel):
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
