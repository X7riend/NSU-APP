from sqlalchemy.orm import Session
from . import models, schemas

def get_passenger(db: Session, passenger_id: int):
    return db.query(models.Passenger).filter(models.Passenger.id == passenger_id).first()

def get_passengers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Passenger).offset(skip).limit(limit).all()

def create_passenger(db: Session, passenger: schemas.PassengerCreate):
    db_passenger = models.Passenger(**passenger.dict())
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger