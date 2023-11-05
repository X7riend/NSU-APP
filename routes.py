from fastapi import FastAPI, HTTPException
from SqlLite import models, crud, schemas
from SqlLite.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

db = SessionLocal()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/passengers")
def getPassengers():
    passengerList =  crud.get_passengers(db=db)
    return passengerList

@app.get("/passenger/{passenger_id}")
def get_passenger(passenger_id: int):
    passenger = SessionLocal().query(models.Passenger).filter(models.Passenger.id == passenger_id)

    if SessionLocal().query(passenger.exists()):
        return passenger
    else:
        raise HTTPException(status_code=404, detail="Passenger not found")
    
@app.post("/passenger", response_model=schemas.Passenger)
def add_passenger(passenger: schemas.PassengerCreate):
    return  crud.create_passenger(db=db, passenger=passenger)



@app.delete("/passenger/{id}")
def delete_passenger(id: int):
  SessionLocal().query(models.Passenger).filter(models.Passenger.id == id).delete(synchronize_session=False)

'''@app.put("/passenger/{id}")
def update_passenger(id: int, passenger: Passenger):'''

@app.get("/menuItems/")
def getPassengers():
    menuList =  crud.get_menu_items(db=db)
    return menuList

@app.post("/menuItems/", response_model=schemas.MenuItem)
def add_menuItem(menuItem: schemas.MenuItemCreate):
    return  crud.create_menu_item(db=db, menuItem=menuItem)

@app.delete("/menuItems/{id}")
def delete_menuItem(id: int):
  SessionLocal().query(models.MenuItems).filter(models.MenuItems.id == id).delete(synchronize_session=False)