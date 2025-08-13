#!/usr/bin/env python3
"""Script para limpiar BD y cargar datos desde CSV"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from app.database import SessionLocal
from app.models import Station
from app.data_loader import load_stations_from_csv, get_stations_count

def reset_and_load():
    db = SessionLocal()
    try:
        # Limpiar datos existentes
        deleted = db.query(Station).delete()
        db.commit()
        print(f"🗑️ Eliminadas {deleted} estaciones existentes")
        
        # Cargar datos desde CSV
        load_stations_from_csv()
        count = get_stations_count()
        print(f"📊 Total de estaciones cargadas: {count}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    reset_and_load()