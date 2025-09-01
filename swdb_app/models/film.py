from sqlalchemy import (Column, Integer, String, Date, DateTime,
                        ARRAY)
from sqlalchemy.orm import relationship

from swdb_app.db.session import Base
from swdb_app.models.association_tables import (
    film_character, film_starship)


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String, nullable=False)
    director = Column(String, nullable=False)
    producer = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    url = Column(String, unique=True, nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    species = Column(ARRAY(String))
    vehicles = Column(ARRAY(String))
    planets = Column(ARRAY(String))

    characters = relationship("Character",
                              secondary=film_character,
                              back_populates="films",
                              lazy="selectin"
                              )
    starships = relationship("Starship",
                             secondary=film_starship,
                             back_populates="films",
                             lazy="selectin")
