from sqlalchemy import Column, Integer, String
from .database import Base

class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True, index=True)
    seat = Column(String, index=True)
    drink = Column(String)
    wakeup = Column(String)
