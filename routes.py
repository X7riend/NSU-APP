from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from SqlLite import models, crud
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
    

#@app.post("/passenger")
#def add_passenger():
#   return  


   

@app.delete("/passenger/{id}")
def delete_passenger(id: int):
  SessionLocal().query(models.Passenger).filter(models.Passenger.id == id).delete(synchronize_session=False)

@app.put("/passenger/{id}")
def update_passenger(id: int, passenger: Passenger):
    index = next((i for i, p in enumerate(data) if p['id'] == id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    if any(p['seat'] == passenger.seat and p['id'] != id for p in data):
        raise HTTPException(status_code=400, detail="Seat already taken")
    data[index] = passenger.dict()
    return data