from pydantic import BaseModel

class PassengerBase(BaseModel):
    id:int
    aaNumber: str
    seatNumber: str
    drinkPreference: str
    snackPrefernce: str
    wakeUp: bool


class MenuItemBase(BaseModel):

    id: int
    name:str
    type:str


