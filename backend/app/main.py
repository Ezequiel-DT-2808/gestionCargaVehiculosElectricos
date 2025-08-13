from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from app import models, schemas, crud, auth, scheduler
from app.database import engine, SessionLocal
from app.data_loader import load_stations_from_csv, get_stations_count
import traceback
from sqlalchemy.orm import Session

# Crear tablas
models.Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI(title="Estaciones de Carga API", version="1.0.0")

# Cargar datos iniciales desde CSV
load_stations_from_csv()

# Iniciar el scheduler
scheduler.start_scheduler()

# Habilitar CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:9010",
    "http://127.0.0.1:9010",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint de login
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(f"🔑 Solicitud de login recibida para: {form_data.username}")
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = auth.create_access_token({"sub": user["username"]})
    print(f"✅ Token generado exitosamente para: {form_data.username}")
    return {"access_token": token, "token_type": "bearer"}

# Crear estación
@app.post("/stations/", response_model=schemas.StationOut)
def create_station(station: schemas.StationCreate, db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    return crud.create_station(db, station)

# Listar estaciones
@app.get("/stations/", response_model=list[schemas.StationOut])
def list_stations(db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    return crud.get_stations(db)

# Actualizar estación
@app.put("/stations/{station_id}", response_model=schemas.StationOut)
def update_station(station_id: int, update: schemas.StationUpdate, db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    return crud.update_station_status(db, station_id, update.is_active)

# Endpoint para cargar datos iniciales
@app.post("/load-initial-data")
def load_initial_data(user: str = Depends(auth.get_current_user)):
    load_stations_from_csv()
    count = get_stations_count()
    return {"message": f"Datos cargados. Total de estaciones: {count}"}

# Endpoint para forzar carga de datos (limpia y recarga)
@app.post("/force-load-data")
def force_load_data(db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    # Limpiar datos existentes
    db.query(models.Station).delete()
    db.commit()
    
    # Cargar datos desde CSV
    load_stations_from_csv()
    count = get_stations_count()
    return {"message": f"Datos recargados. Total de estaciones: {count}"}

# Endpoint para obtener estadísticas
@app.get("/stats")
def get_stats(db: Session = Depends(get_db), user: str = Depends(auth.get_current_user)):
    total = db.query(models.Station).count()
    active = db.query(models.Station).filter(models.Station.is_active == True).count()
    inactive = total - active
    return {
        "total_stations": total,
        "active_stations": active,
        "inactive_stations": inactive
    }

# Endpoint para obtener estaciones filtradas
@app.get("/stations/filtered", response_model=list[schemas.StationOut])
def get_filtered_stations(
    status: str = None,
    min_kw: float = None,
    max_kw: float = None,
    db: Session = Depends(get_db),
    user: str = Depends(auth.get_current_user)
):
    return crud.get_filtered_stations(db, status, min_kw, max_kw)

# Endpoint de prueba para verificar credenciales
@app.get("/test-auth")
def test_auth():
    return {
        "message": "Credenciales válidas:",
        "username": "admin",
        "password": "admin123",
        "endpoint": "POST /token"
    }

# Endpoint para verificar si el usuario está autenticado
@app.get("/me")
def get_current_user_info(user: str = Depends(auth.get_current_user)):
    return {"username": user, "message": "Usuario autenticado correctamente"}