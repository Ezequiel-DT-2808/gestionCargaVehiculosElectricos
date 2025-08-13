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

def get_filtered_stations(db: Session, status: str = None, min_kw: float = None, max_kw: float = None):
    query = db.query(models.Station)
    
    if status == "active":
        query = query.filter(models.Station.is_active == True)
    elif status == "inactive":
        query = query.filter(models.Station.is_active == False)
    
    if min_kw is not None:
        query = query.filter(models.Station.max_kw >= min_kw)
    
    if max_kw is not None:
        query = query.filter(models.Station.max_kw <= max_kw)
    
    return query.all()
