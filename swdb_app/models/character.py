from sqlalchemy import (Column, Integer, String, DateTime, ARRAY,
                        func)
from sqlalchemy.orm import relationship

from swdb_app.db.session import Base
from swdb_app.models.association_tables import (
    film_character, character_starship)


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    birth_year = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created = Column(DateTime(timezone=True),
                     server_default=func.now(),
                     nullable=False)
    edited = Column(DateTime(timezone=True),
                    server_default=func.now(),
                    onupdate=func.now(),
                    nullable=False)
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
    # starships = relationship("Starship",
    #                          secondary=character_starship,
    #                          back_populates="pilots",
    #                          lazy="selectin")
