from sqlalchemy.orm import Session
from app import models, schemas

def create_station(db: Session, station: schemas.StationCreate):
    db_station = models.Station(**station.dict())
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station

def get_stations(db: Session):
    return db.query(models.Station).all()

def update_station_status(db: Session, station_id: int, is_active: bool):
    station = db.query(models.Station).get(station_id)
    if station:
        station.is_active = is_active
        db.commit()
        db.refresh(station)
    return station
