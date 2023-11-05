from sqlalchemy.orm import Session
from .import models, schemas

def get_passenger(db: Session, passenger_id: int):
    return db.query(models.Passenger).filter(models.Passenger.id == passenger_id).first()


def get_passengers(db: Session):
    return db.query(models.Passenger).all()


def create_passenger(db: Session, passenger: schemas.PassengerCreate):
    db_passenger = models.Passenger(**passenger.model_dump())
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger


def get_menu_items(db: Session):
    return db.query(models.MenuItems).all()


def create_menu_item(db: Session, menuItem: schemas.MenuItemCreate):
    db_menu_item = models.MenuItems(**menuItem.model_dump())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item
