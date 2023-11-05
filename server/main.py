from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Allows all origins from localhost port 5500
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/passengers/", response_model=schemas.Passenger)
def create_passenger(passenger: schemas.PassengerCreate, db: Session = Depends(get_db)):
    return crud.create_passenger(db=db, passenger=passenger)

@app.get("/passengers/", response_model=list[schemas.Passenger])
def read_passengers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    passengers = crud.get_passengers(db, skip=skip, limit=limit)
    return passengers

@app.get("/passengers/{passenger_id}", response_model=schemas.Passenger)
def read_passenger(passenger_id: int, db: Session = Depends(get_db)):
    passenger = crud.get_passenger(db, passenger_id=passenger_id)
    if passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return passenger

# Add endpoints for updating and deleting passengers if needed