from apscheduler.schedulers.background import BackgroundScheduler
from app.database import SessionLocal
from app.crud import update_station_status

def toggle_station():
    db = SessionLocal()
    stations = db.query(models.Station).all()
    for s in stations:
        s.is_active = not s.is_active
    db.commit()
    db.close()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(toggle_station, "interval", minutes=5)
    scheduler.start()
