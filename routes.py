from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
data = []

class Passenger(BaseModel):
    id: int
    seat: str
    drink: str
    snack: str

@app.get("/list")
def get_passengers():
    return data

@app.get("/passenger/{id}")
def get_passenger(id: int):
    passenger = next((p for p in data if p['id'] == id), None)
    if passenger is not None:
        return passenger
    raise HTTPException(status_code=404, detail="Passenger not found")

@app.post("/passenger")
def add_passenger(passenger: Passenger):
    if any(p['id'] == passenger.id for p in data):
        raise HTTPException(status_code=400, detail="Passenger ID already taken")
    if any(p['seat'] == passenger.seat for p in data):
        raise HTTPException(status_code=400, detail="Seat already taken")
    data.append(passenger.dict())
    return data

@app.delete("/passenger/{id}")
def delete_passenger(id: int):
    global data
    data = [p for p in data if p['id'] != id]
    return data

@app.put("/passenger/{id}")
def update_passenger(id: int, passenger: Passenger):
    index = next((i for i, p in enumerate(data) if p['id'] == id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    if any(p['seat'] == passenger.seat and p['id'] != id for p in data):
        raise HTTPException(status_code=400, detail="Seat already taken")
    data[index] = passenger.dict()
    return data