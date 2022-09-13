from typing import List
from http.client import HTTPException
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
import database
import seeds

app = FastAPI()

@app.on_event("startup")
def configure():
    database.Base.metadata.create_all(bind=database.engine)

    db = database.SessionLocal()
    for cafe in seeds.INITIAL_DATA['cafes']:
        print(cafe)
        #crud.create_cafe(db, schemas.CafeCreate(**cafe))

    db.close()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cafes/", response_model=List[schemas.Cafe])
def read_cafes(db: Session = Depends(get_db)):
    cafes = crud.get_cafes(db)
    return cafes
