# Sistema de Gestión de Estaciones de Carga

## 📋 Descripción del Proyecto
Sistema web completo para la gestión de estaciones de carga de vehículos eléctricos, desarrollado con FastAPI (backend) y Next.js (frontend). Incluye autenticación JWT, operaciones CRUD, visualizaciones interactivas y carga automática de datos desde archivos CSV.

## 🚀 Inicio Rápido con Docker

### Prerrequisitos
- Docker
- Docker Compose

### Ejecutar la aplicación completa

```bash
# Clonar y navegar al proyecto
cd estaciones_de_carga

# Construir y ejecutar todos los servicios
docker-compose up --build

# En modo detached (segundo plano)
docker-compose up -d --build
```

### Servicios disponibles
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:9010
- **Base de datos**: PostgreSQL en puerto 5432
- **Documentación API**: http://localhost:9010/docs

### Credenciales por defecto
- **Usuario**: admin
- **Contraseña**: admin123

## 📚 Documentación Completa

### 📖 Guías de Instalación y Uso
- **[Backend README](backend/README.md)** - Instalación, configuración y API del backend
- **[Frontend README](frontend/README.md)** - Instalación, configuración y componentes del frontend
- **[Documentación de Datos](DATOS_ORIGEN.md)** - Origen, estructura y características del dataset

### 🛠️ Desarrollo Local

#### Backend (Puerto 9010)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
uvicorn app.main:app --reload --port 9010
```

#### Frontend (Puerto 3000)
```bash
cd frontend
npm install
npm run dev
```

## 📊 Datos Utilizados

### Origen de los Datos
Los datos provienen de una compilación de **estaciones de carga reales** de España, basadas en información pública de:

- **Tesla Supercharger Network**
- **Iberdrola** - Red de carga rápida
- **Endesa X** - Electrolineras
- **EDP España** - Puntos de carga
- **Repsol** - Electrolineras

### Archivos de Datos Disponibles
- **CSV**: `backend/data/charging_stations.csv` (formato principal)
- **Excel**: `backend/data/charging_stations.xlsx` (formato alternativo)
- **Total**: 20 estaciones reales con ubicaciones verificadas

### Características del Dataset
- **Cobertura**: Principales ciudades de España
- **Operadores**: 5 empresas líderes del sector
- **Potencias**: Rango de 40-150 kW
- **Estados**: Activo/Inactivo (simulado para demostración)

## 🐳 Comandos Docker Útiles

```bash
# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f backend
docker-compose logs -f frontend

# Parar servicios
docker-compose down

# Limpiar volúmenes (resetear BD)
docker-compose down -v

# Reconstruir servicios
docker-compose build backend
docker-compose build frontend

# Ejecutar solo la base de datos
docker-compose up db
```

## ✨ Funcionalidades Implementadas

### Backend (FastAPI)
- ✅ **Autenticación JWT** con credenciales hardcoded
- ✅ **API REST completa** con documentación Swagger
- ✅ **CRUD de estaciones** (Crear, Leer, Actualizar)
- ✅ **Filtros avanzados** por estado y potencia
- ✅ **Scheduler automático** (cambios cada 5 minutos)
- ✅ **Carga automática** de datos desde CSV
- ✅ **Base de datos PostgreSQL** con SQLAlchemy
- ✅ **Validación de datos** con Pydantic

### Frontend (Next.js + React)
- ✅ **Interfaz moderna** con Tailwind CSS
- ✅ **Autenticación** con manejo de tokens JWT
- ✅ **Dashboard interactivo** con estadísticas
- ✅ **Gráficos dinámicos** con Chart.js
- ✅ **Filtros interactivos** que consultan el backend
- ✅ **Formularios** para gestión de estaciones
- ✅ **Responsive design** para móviles y desktop
- ✅ **TypeScript** para tipado estático

### Infraestructura
- ✅ **Contenerización completa** con Docker
- ✅ **Orquestación** con Docker Compose
- ✅ **Base de datos** PostgreSQL persistente
- ✅ **Networking** entre servicios
- ✅ **Variables de entorno** configurables

## 🎯 Experiencia de Usuario (UX)

### Flujo Principal
1. **Login** → Credenciales visibles en pantalla
2. **Dashboard** → Vista general con estadísticas
3. **Visualización** → Gráficos interactivos con filtros
4. **Gestión** → CRUD intuitivo de estaciones
5. **Datos** → Carga y recarga desde CSV

### Características UX
- **Interfaz intuitiva** y moderna
- **Feedback visual** inmediato
- **Manejo de errores** descriptivo
- **Loading states** durante operaciones
- **Responsive** para todos los dispositivos

## 🧪 Testing y Verificación

### Endpoints de Prueba
- `GET /test-auth` - Verificar credenciales válidas
- `GET /me` - Información del usuario autenticado
- `GET /docs` - Documentación interactiva Swagger

### Verificación Rápida
```bash
# Verificar backend
curl http://localhost:9010/test-auth

# Verificar frontend
open http://localhost:3000
```

## 📈 Arquitectura del Sistema

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   PostgreSQL    │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│   Database      │
│   Port: 3000    │    │   Port: 9010    │    │   Port: 5432    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   CSV Data      │
                    │   (20 stations) │
                    └─────────────────┘
```

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
# Backend
DATABASE_URL=postgresql://postgres:password@localhost:5432/evdb
SECRET_KEY=tu_clave_jwt

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:9010
```

### Puertos Utilizados
- **3000**: Frontend (Next.js)
- **9010**: Backend (FastAPI)
- **5432**: PostgreSQL Database

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo LICENSE para más detalles.

---

**Para documentación detallada de cada componente, consulta los README específicos en las carpetas `backend/` y `frontend/`.**