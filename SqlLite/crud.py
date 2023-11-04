from sqlalchemy.orm import Session
from .import models, schemas

def get_passenger(db: Session, passenger_id: int):
    return db.query(models.Passenger).filter(models.Passenger.id == passenger_id).first()


def get_passengers(db: Session):
    return db.query(models.Passenger).all()


def create_passenger(db: Session, passenger: schemas.PassengerBase):
    db_passenger = models.Passenger(aaNumber = passenger.aaNumber, seatNumber = passenger.seatNumber, drinkPreference = passenger.drinkPreference, snackPreference = passenger.snackPreference, wakeUp = passenger.wakeUp)
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger


def get_menu_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MenuItems).offset(skip).limit(limit).all()


def create_menu_item(db: Session, menuItem: schemas.MenuItemBase):
    db_menu_item = models.MenuItems(name = menuItem.name, type = menuItem.type )
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item
