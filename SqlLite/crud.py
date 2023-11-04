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

'''def populate_database(db, menu_items):
    menu_items = [
    {"id": 1, "name": "Biscoff cookies", "Type": "snack"},
    {"id": 2, "name": "Pretzels", "Type": "snack"},
    {"id": 3, "name": "Coke", "Type": "drink"},
    {"id": 4, "name": "Diet Coke", "Type": "drink"},
    {"id": 5, "name": "Coke Zero", "Type": "drink"},
    {"id": 6, "name": "Dr. Pepper", "Type": "drink"},
    {"id": 7, "name": "Diet Dr. Pepper", "Type": "drink"},
    {"id": 8, "name": "Sprite", "Type": "drink"},
    {"id": 9, "name": "Diet Sprite", "Type": "drink"},
    {"id": 10, "name": "Aha Lime + Watermelon", "Type": "drink"},
    {"id": 11, "name": "Canada Dry Club Soda", "Type": "drink"},
    {"id": 12, "name": "Canada Dry Tonic Water", "Type": "drink"},
    {"id": 13, "name": "Canada Dry Ginger Ale", "Type": "drink"},
    {"id": 14, "name": "FreshBrew™ Coffeehouse Roast", "Type": "drink"},
    {"id": 15, "name": "FreshBrew™ Decaffeinated Coffeehouse Roast", "Type": "drink"},
    {"id": 16, "name": "Bigelow Tea", "Type": "drink"},
    {"id": 17, "name": "Mott's Tomato Juice", "Type": "drink"},
    {"id": 18, "name": "Mr. & Mrs. T Bloody Mary Mix", "Type": "drink"},
    {"id": 19, "name": "Minute Maid Apple Juice", "Type": "drink"},
    {"id": 20, "name": "Minute Maid Cranberry Apple", "Type": "drink"},
    {"id": 21, "name": "Minute Maid Orange Juice", "Type": "drink"},
    {"id": 22, "name": "Bottled Water", "Type": "drink"},
    ]

    for menu_item in menu_items:
        create_menu_item(db, MenuItemCreate(name=menu_item["name"], Type=menu_item["Type"]))
'''

def create_menu_item(db: Session, menuItem: schemas.MenuItemCreate):
    db_menu_item = models.MenuItems(**menuItem.model_dump())
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item
