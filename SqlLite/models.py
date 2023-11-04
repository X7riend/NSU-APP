from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class Passenger(Base):
    __tablename__ =  "passengers"

    id = Column(Integer, primary_key=True, index=True)
    aaNumber = Column(String, index=True)
    seatNumber = Column(String)
    drinkPreference = Column(String)
    wakeUp = Column(Boolean)


class MenuItems(Base): 
    __tablename__ = "menuItems"

    id = Column(Integer, primary_key=True)
    name = Column(String)
