from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from app import models, schemas, crud, auth, scheduler
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session

# Crear tablas
models.Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI()

# Iniciar el scheduler
scheduler.start_scheduler()

# Habilitar CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
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
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401)
    token = auth.create_access_token({"sub": user["username"]})
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