from pydantic import BaseModel

class PassengerBase(BaseModel):
    seat: str
    drink: str
    wakeup: str

class PassengerCreate(PassengerBase):
    pass

class Passenger(PassengerBase):
    id: int

    class Config:
        orm_mode = True




