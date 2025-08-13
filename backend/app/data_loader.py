import csv
import os
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Station

def load_stations_from_csv():
    """Carga estaciones desde el archivo CSV público"""
    db = SessionLocal()
    
    try:
        # Verificar si ya hay datos
        existing_count = db.query(Station).count()
        print(f"📊 Estaciones existentes en BD: {existing_count}")
        
        if existing_count > 0:
            print("⚠️ Base de datos ya contiene estaciones")
            db.close()
            return
        
        # Buscar el archivo CSV
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'charging_stations.csv')
        csv_path = os.path.abspath(csv_path)
        print(f"🔍 Buscando CSV en: {csv_path}")
        
        if not os.path.exists(csv_path):
            print(f"❌ Archivo CSV no encontrado: {csv_path}")
            db.close()
            return
        
        print(f"✅ Archivo CSV encontrado, cargando datos...")
        
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            stations_created = 0
            
            for row in reader:
                print(f"📝 Procesando: {row['name']}")
                station = Station(
                    name=row['name'],
                    location=row['location'],
                    max_kw=float(row['max_kw']),
                    is_active=row['is_active'].lower() == 'true'
                )
                db.add(station)
                stations_created += 1
            
            db.commit()
            print(f"✅ {stations_created} estaciones cargadas desde CSV")
            
    except Exception as e:
        print(f"❌ Error cargando datos: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

def get_stations_count():
    """Obtiene el número de estaciones en la base de datos"""
    db = SessionLocal()
    count = db.query(Station).count()
    db.close()
    return count