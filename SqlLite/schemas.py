from pydantic import BaseModel

class PassengerBase(BaseModel):
    aaNumber: str
    seatNumber: str
    drinkPreference: str
    wakeUp: bool

class PassengerCreate(PassengerBase):
    pass

class Passenger(PassengerBase):
    id:int

    class Config:
        orm_mode = True

class MenuItemBase(BaseModel):
    name:str


class MenuItemCreate(MenuItemBase):
    pass


class MenuItem(MenuItemBase):
    id:int

    class Config:
        orm_mode = True


