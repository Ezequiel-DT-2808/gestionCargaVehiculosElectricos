# Backend - Sistema de Gestión de Estaciones de Carga

## 📋 Descripción
API REST desarrollada con FastAPI para la gestión de estaciones de carga de vehículos eléctricos. Incluye autenticación JWT, operaciones CRUD, filtros avanzados y carga automática de datos desde archivos CSV.

## 🛠️ Tecnologías Utilizadas
- **FastAPI** - Framework web moderno y rápido
- **SQLAlchemy** - ORM para Python
- **PostgreSQL** - Base de datos relacional
- **JWT** - Autenticación con tokens
- **APScheduler** - Tareas programadas
- **Pydantic** - Validación de datos
- **Uvicorn** - Servidor ASGI

## 📁 Estructura del Proyecto
```
backend/
├── app/
│   ├── main.py          # Aplicación principal FastAPI
│   ├── auth.py          # Sistema de autenticación JWT
│   ├── models.py        # Modelos de base de datos (SQLAlchemy)
│   ├── schemas.py       # Esquemas de validación (Pydantic)
│   ├── crud.py          # Operaciones CRUD
│   ├── database.py      # Configuración de base de datos
│   ├── config.py        # Configuración general
│   ├── scheduler.py     # Tareas programadas
│   └── data_loader.py   # Carga de datos desde CSV
├── data/
│   └── charging_stations.csv  # Datos de estaciones de carga
├── requirements.txt     # Dependencias Python
├── Dockerfile          # Imagen Docker
└── README.md           # Esta documentación
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.11 o superior
- PostgreSQL 15 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd estaciones_de_carga/backend
```

### 2. Crear entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En macOS/Linux:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos PostgreSQL
```bash
# Crear base de datos
createdb evdb

# O usando psql:
psql -c "CREATE DATABASE evdb;"
```

### 5. Configurar variables de entorno (opcional)
```bash
# Crear archivo .env (opcional)
echo "DATABASE_URL=postgresql://postgres:tu_password@localhost:5432/evdb" > .env
```

## ▶️ Ejecución

### Desarrollo local
```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar servidor de desarrollo
uvicorn app.main:app --reload --port 9010
```

### Producción
```bash
uvicorn app.main:app --host 0.0.0.0 --port 9010
```

### Con Docker
```bash
# Construir imagen
docker build -t estaciones-backend .

# Ejecutar contenedor
docker run -p 9010:8000 estaciones-backend
```

## 🔐 Autenticación

### Credenciales por defecto
- **Usuario**: `admin`
- **Contraseña**: `admin123`

### Obtener token JWT
```bash
curl -X POST "http://localhost:9010/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"
```

### Usar token en requests
```bash
curl -X GET "http://localhost:9010/stations/" \
  -H "Authorization: Bearer <tu_token_jwt>"
```

## 📊 Endpoints de la API

### Autenticación
- `POST /token` - Obtener token JWT
- `GET /me` - Información del usuario actual
- `GET /test-auth` - Verificar credenciales válidas

### Estaciones de Carga
- `GET /stations/` - Listar todas las estaciones
- `POST /stations/` - Crear nueva estación
- `PUT /stations/{id}` - Actualizar estado de estación
- `GET /stations/filtered` - Obtener estaciones filtradas

### Datos y Estadísticas
- `GET /stats` - Estadísticas generales
- `POST /load-initial-data` - Cargar datos desde CSV
- `POST /force-load-data` - Forzar recarga de datos

### Documentación Interactiva
- `GET /docs` - Swagger UI (Documentación interactiva)
- `GET /redoc` - ReDoc (Documentación alternativa)

## 📈 Datos Utilizados

### Origen de los Datos
Los datos de estaciones de carga provienen de una compilación de estaciones reales de España, basadas en:

1. **Tesla Supercharger Network** - Ubicaciones oficiales de Tesla
2. **Iberdrola** - Red de carga rápida de Iberdrola
3. **Endesa X** - Puntos de carga de Endesa
4. **EDP** - Estaciones de EDP España
5. **Repsol** - Red de electrolineras Repsol

### Archivo de Datos: `data/charging_stations.csv`
```csv
name,location,max_kw,is_active
Tesla Supercharger Madrid Centro,Madrid - Gran Vía 28,150.0,true
Iberdrola Barcelona Port,Barcelona - Port Vell,50.0,true
Endesa X Sevilla Norte,Sevilla - Av. de la Buhaira,75.0,false
...
```

### Campos del Dataset
- **name**: Nombre de la estación de carga
- **location**: Ubicación específica (ciudad y dirección)
- **max_kw**: Capacidad máxima en kilovatios
- **is_active**: Estado actual (activo/inactivo)

### Características del Dataset
- **Total de registros**: 20 estaciones
- **Cobertura geográfica**: Principales ciudades de España
- **Tipos de operadores**: 5 operadores principales
- **Rango de potencia**: 40-150 kW
- **Estados**: Activo/Inactivo (simulado para demostración)

## ⚙️ Funcionalidades Especiales

### Carga Automática de Datos
- Los datos se cargan automáticamente al iniciar la aplicación
- Prevención de duplicados
- Logs detallados del proceso de carga

### Scheduler Automático
- Cambio automático de estados cada 5 minutos
- Simula el comportamiento real de las estaciones
- Ejecuta en segundo plano

### Filtros Avanzados
- Filtro por estado (activo/inactivo)
- Filtro por rango de potencia (kW mínimo/máximo)
- Combinación de múltiples filtros

## 🧪 Testing

### Verificar funcionamiento
```bash
# Verificar que el servidor está corriendo
curl http://localhost:9010/test-auth

# Probar autenticación
curl -X POST "http://localhost:9010/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"

# Listar estaciones (requiere token)
curl -X GET "http://localhost:9010/stations/" \
  -H "Authorization: Bearer <token>"
```

## 🐛 Troubleshooting

### Problemas Comunes

1. **Error de conexión a PostgreSQL**
   ```bash
   # Verificar que PostgreSQL está corriendo
   pg_isready
   
   # Verificar conexión
   psql -d evdb -c "SELECT 1;"
   ```

2. **Puerto ocupado**
   ```bash
   # Cambiar puerto
   uvicorn app.main:app --reload --port 8001
   ```

3. **Dependencias faltantes**
   ```bash
   # Reinstalar dependencias
   pip install -r requirements.txt --force-reinstall
   ```

4. **Datos no se cargan**
   ```bash
   # Forzar recarga de datos
   curl -X POST "http://localhost:9010/force-load-data" \
     -H "Authorization: Bearer <token>"
   ```

## 📝 Logs y Debugging

### Logs de la aplicación
- Los logs se muestran en la consola durante la ejecución
- Incluyen información de autenticación, carga de datos y errores

### Habilitar logs detallados
```bash
# Ejecutar con logs de debug
uvicorn app.main:app --reload --log-level debug
```

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/evdb
SECRET_KEY=tu_clave_secreta_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Configuración de Base de Datos
- Por defecto usa PostgreSQL local
- Configurable mediante `DATABASE_URL`
- Creación automática de tablas

## 📚 Recursos Adicionales

- [Documentación FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [JWT.io](https://jwt.io/) - Para decodificar tokens JWT

## 👥 Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Ejecuta las pruebas
5. Envía un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo LICENSE para más detalles.