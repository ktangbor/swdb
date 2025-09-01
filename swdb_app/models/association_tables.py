from sqlalchemy import (Column, Integer, Table, ForeignKey)

from swdb_app.db.session import Base


film_character = Table(
    "film_character",
    Base.metadata,
    Column("film_id", Integer, ForeignKey("films.id"),
           primary_key=True),
    Column("character_id", ForeignKey("characters.id"),
           primary_key=True)
)

film_starship = Table(
    "film_starship",
    Base.metadata,
    Column("film_id", Integer, ForeignKey("films.id"),
           primary_key=True),
    Column("starship_id", ForeignKey("starships.id"),
           primary_key=True)
)

character_starship = Table(
    "character_starship",
    Base.metadata,
    Column("character_id", Integer, ForeignKey("characters.id"),
           primary_key=True),
    Column("starship_id", ForeignKey("starships.id"),
           primary_key=True)
)
