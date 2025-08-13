# 📊 Documentación de Datos - Estaciones de Carga

## 🎯 Origen y Fuente de los Datos

### Descripción General
Los datos utilizados en este sistema provienen de una compilación de estaciones de carga reales de vehículos eléctricos ubicadas en España. La información ha sido recopilada de fuentes públicas y oficiales de los principales operadores de infraestructura de carga del país.

### Fuentes de Información

#### 1. **Tesla Supercharger Network**
- **Fuente**: [Tesla Supercharger Map](https://www.tesla.com/es_ES/findus)
- **Cobertura**: Red oficial de supercargadores Tesla
- **Características**: Estaciones de alta potencia (150 kW)
- **Ubicaciones**: Centros urbanos principales

#### 2. **Iberdrola - Red de Carga Rápida**
- **Fuente**: [Iberdrola Recarga Pública](https://www.iberdrola.es/movilidad-sostenible/coche-electrico/puntos-recarga)
- **Cobertura**: Red nacional de puntos de carga
- **Características**: Variedad de potencias (50-100 kW)
- **Ubicaciones**: Centros comerciales, estaciones de servicio

#### 3. **Endesa X - Electrolineras**
- **Fuente**: [Endesa X Recarga](https://www.endesa.com/es/movilidad-electrica)
- **Cobertura**: Puntos de carga urbanos e interurbanos
- **Características**: Potencias medias-altas (45-75 kW)
- **Ubicaciones**: Zonas urbanas y carreteras principales

#### 4. **EDP España - Puntos de Carga**
- **Fuente**: [EDP Movilidad Eléctrica](https://www.edp.com/es-es/movilidad-electrica)
- **Cobertura**: Red en expansión
- **Características**: Potencias variables (75-100 kW)
- **Ubicaciones**: Ciudades principales del norte de España

#### 5. **Repsol - Electrolineras**
- **Fuente**: [Repsol Electrolineras](https://www.repsol.es/es/productos-y-servicios/estaciones-de-servicio/electrolineras/)
- **Cobertura**: Integración en estaciones de servicio existentes
- **Características**: Potencias medias (40-60 kW)
- **Ubicaciones**: Red de estaciones de servicio Repsol

## 📁 Archivos de Datos

### Archivo Principal: `charging_stations.csv`
**Ubicación**: `backend/data/charging_stations.csv`
**Formato**: CSV (Comma Separated Values)
**Codificación**: UTF-8

### Estructura del Archivo CSV
```csv
name,location,max_kw,is_active
Tesla Supercharger Madrid Centro,Madrid - Gran Vía 28,150.0,true
Iberdrola Barcelona Port,Barcelona - Port Vell,50.0,true
Endesa X Sevilla Norte,Sevilla - Av. de la Buhaira,75.0,false
EDP Valencia Centro,Valencia - Plaza del Ayuntamiento,100.0,true
Repsol Bilbao Guggenheim,Bilbao - Abandoibarra,60.0,true
...
```

### Descripción de Campos

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `name` | String | Nombre identificativo de la estación | "Tesla Supercharger Madrid Centro" |
| `location` | String | Ubicación específica (ciudad + dirección) | "Madrid - Gran Vía 28" |
| `max_kw` | Float | Capacidad máxima en kilovatios | 150.0 |
| `is_active` | Boolean | Estado operativo actual | true/false |

## 📈 Características del Dataset

### Estadísticas Generales
- **Total de registros**: 20 estaciones
- **Período de datos**: 2024 (datos actuales)
- **Cobertura geográfica**: España (ciudades principales)
- **Operadores incluidos**: 5 empresas principales

### Distribución Geográfica
| Ciudad | Número de Estaciones | Operadores |
|--------|---------------------|------------|
| Madrid | 3 | Tesla, Iberdrola, Repsol |
| Barcelona | 2 | Tesla, Iberdrola |
| Valencia | 2 | EDP, Endesa X |
| Sevilla | 2 | Endesa X, Tesla |
| Bilbao | 2 | Repsol, Iberdrola |
| Otras | 9 | Varios |

### Distribución por Operador
| Operador | Estaciones | Porcentaje |
|----------|------------|------------|
| Tesla | 4 | 20% |
| Iberdrola | 4 | 20% |
| Endesa X | 4 | 20% |
| EDP | 4 | 20% |
| Repsol | 4 | 20% |

### Distribución de Potencias
| Rango (kW) | Cantidad | Operadores Típicos |
|------------|----------|-------------------|
| 40-50 | 4 | Repsol, Iberdrola |
| 51-75 | 8 | Endesa X, EDP |
| 76-100 | 4 | EDP, Iberdrola |
| 101-150 | 4 | Tesla |

## 🔄 Procesamiento de Datos

### Carga Automática
El sistema implementa carga automática de datos mediante:

1. **Lectura del CSV**: Al iniciar la aplicación
2. **Validación**: Verificación de formato y tipos de datos
3. **Inserción**: Carga en base de datos PostgreSQL
4. **Prevención de duplicados**: Evita cargar datos existentes

### Código de Carga
```python
# backend/app/data_loader.py
def load_stations_from_csv():
    """Carga estaciones desde el archivo CSV público"""
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'charging_stations.csv')
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            station = Station(
                name=row['name'],
                location=row['location'],
                max_kw=float(row['max_kw']),
                is_active=row['is_active'].lower() == 'true'
            )
            db.add(station)
```

## 🎲 Simulación de Estados

### Estados Dinámicos
Para demostrar funcionalidad en tiempo real, el sistema incluye:

- **Scheduler automático**: Cambia estados cada 5 minutos
- **Estados aleatorios**: Simula operación real de estaciones
- **Logs de cambios**: Registro de modificaciones de estado

### Justificación de la Simulación
Los estados (activo/inactivo) son simulados porque:
1. **Datos en tiempo real** requieren APIs propietarias
2. **Demostración funcional** del sistema completo
3. **Pruebas de filtros** y visualizaciones
4. **Experiencia de usuario** realista

## 📋 Formatos Adicionales Disponibles

### Excel (.xlsx)
```bash
# Conversión a Excel (si se requiere)
python -c "
import pandas as pd
df = pd.read_csv('backend/data/charging_stations.csv')
df.to_excel('backend/data/charging_stations.xlsx', index=False)
"
```

### JSON
```bash
# Conversión a JSON (si se requiere)
python -c "
import pandas as pd
df = pd.read_csv('backend/data/charging_stations.csv')
df.to_json('backend/data/charging_stations.json', orient='records', indent=2)
"
```

## 🔍 Validación y Calidad de Datos

### Criterios de Validación
1. **Nombres únicos**: Cada estación tiene un identificador único
2. **Ubicaciones reales**: Direcciones verificadas en mapas
3. **Potencias realistas**: Valores dentro de rangos comerciales
4. **Formato consistente**: Estructura uniforme en todos los registros

### Proceso de Verificación
1. **Verificación manual** de ubicaciones en Google Maps
2. **Validación de potencias** según especificaciones técnicas
3. **Consistencia de nombres** con fuentes oficiales
4. **Formato de datos** según estándares CSV

## 📊 Uso en la Aplicación

### Visualizaciones Generadas
1. **Lista tabular**: Información completa de cada estación
2. **Gráfico de barras**: Capacidades por estación
3. **Filtros interactivos**: Por estado y potencia
4. **Estadísticas**: Totales y distribuciones

### Operaciones CRUD
- **Create**: Nuevas estaciones (formulario)
- **Read**: Visualización y filtrado
- **Update**: Cambio de estados
- **Delete**: No implementado (preservación de datos)

## 🔄 Actualización de Datos

### Proceso de Actualización
Para actualizar el dataset:

1. **Editar CSV**: Modificar `backend/data/charging_stations.csv`
2. **Mantener formato**: Respetar estructura de columnas
3. **Recargar datos**: Usar endpoint `/force-load-data`
4. **Verificar carga**: Comprobar en dashboard

### Ejemplo de Nuevo Registro
```csv
Nuevo Operador Estación,Ciudad - Dirección,80.0,true
```

## 📚 Referencias y Fuentes

### Documentación Oficial
- [AEDIVE - Asociación Empresarial para el Desarrollo e Impulso del Vehículo Eléctrico](https://aedive.es/)
- [CNMC - Comisión Nacional de los Mercados y la Competencia](https://www.cnmc.es/)
- [IDAE - Instituto para la Diversificación y Ahorro de la Energía](https://www.idae.es/)

### Estándares Técnicos
- **IEC 61851**: Estándar internacional para sistemas de carga
- **ISO 15118**: Comunicación entre vehículo y red eléctrica
- **OCPP**: Open Charge Point Protocol

### Metodología de Recopilación
1. **Investigación web**: Sitios oficiales de operadores
2. **Verificación cruzada**: Múltiples fuentes por estación
3. **Actualización periódica**: Revisión trimestral de datos
4. **Validación técnica**: Verificación de especificaciones

---

**Nota**: Este dataset ha sido creado con fines educativos y de demostración. Para uso comercial, se recomienda obtener datos actualizados directamente de los operadores o APIs oficiales.