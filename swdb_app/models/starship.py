from sqlalchemy import (Column, Integer, String, Date, DateTime,
                        ARRAY)
from sqlalchemy.orm import relationship

from swdb_app.db.session import Base
from swdb_app.models.association_tables import (
    film_starship, character_starship)


class Starship(Base):
    __tablename__ = "starships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    model = Column(String, nullable=False)
    starship_class = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(String)
    crew = Column(String)
    passengers = Column(String)
    max_atmosphering_speed = Column(String)
    hyperdrive_rating = Column(String)
    MGLT = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)

    films = relationship("Film",
                         secondary=film_starship,
                         back_populates="starships",
                         lazy="selectin")
    pilots = relationship("Character",
                          secondary=character_starship,
                          back_populates="starships",
                          lazy="selectin")
