from sqlalchemy import (Column, Integer, String, DateTime, ARRAY)
from sqlalchemy.orm import relationship

from swdb_app.db.session import Base
from swdb_app.models.association_tables import (
    film_character, character_starship)


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    eye_color = Column(String)
    hair_color = Column(String)
    height = Column(String)
    mass = Column(String)
    skin_color = Column(String)
    homeworld = Column(ARRAY(String))
    species = Column(ARRAY(String))
    vehicles = Column(ARRAY(String))

    films = relationship("Film",
                         secondary=film_character,
                         back_populates="characters",
                         lazy="selectin")
    starships = relationship("Starship",
                             secondary=character_starship,
                             back_populates="pilots",
                             lazy="selectin")
