#!/usr/bin/env python3
"""Script para cargar datos iniciales desde CSV"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from app.data_loader import load_stations_from_csv, get_stations_count

if __name__ == "__main__":
    print("🚀 Iniciando carga de datos...")
    load_stations_from_csv()
    count = get_stations_count()
    print(f"📊 Total de estaciones en BD: {count}")