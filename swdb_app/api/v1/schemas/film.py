from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, date


class FilmBase(BaseModel):
    title: str = Field(..., description="The title of this film")
    episode_id: str = Field(..., description="The episode number of this film.")
    release_date: date = Field(...)
    url: str = Field(...)
    opening_crawl: str | None = Field(...)
    director: str | None = Field(...)
    producer: str | None = Field(...)
    species: list[str] = Field(default_factory=list)
    vehicles: list[str] = Field(default_factory=list)
    planets: list[str] = Field(default_factory=list)


class FilmCreate(FilmBase):
    pass


class FilmRead(FilmBase):
    id: int
    created: datetime
    edited: datetime
    model_config = ConfigDict(from_attributes=True)


class FilmPublic(FilmRead):
    created: datetime
    edited: datetime


class FilmFilter(BaseModel):
    name: str | None = None
