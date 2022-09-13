from http.client import HTTPException
from sqlalchemy.orm import Session
import models, schemas

def get_cafe(db: Session, cafe_id: int):
    return db.query(models.Cafe).filter(models.Cafe.id == cafe_id).first()

def get_cafes(db: Session):
    return db.query(models.Cafe).all()

def create_cafe(db: Session, cafe: schemas.CafeCreate):
    db_cafe = models.Cafe(name = cafe.name, address = cafe.address, features = cafe.features)
    db.add(db_cafe)
    db.commit()
    db.refresh(db_cafe)
    return db_cafe

def update_cafe(db: Session, cafe: schemas.CafeUpdate):
    fetched_cafe = db.query(models.Cafe).get(cafe.id)
    if fetched_cafe:
        db_cafe = models.Cafe(id = cafe.id, name = cafe.name, address = cafe.address, features = cafe.features)
        db.add(db_cafe)
        db.commit()
        db.refresh(db_cafe)
        return db_cafe

    raise HTTPException(status_code=404, detail =f"cafe {cafe.name} not found")
