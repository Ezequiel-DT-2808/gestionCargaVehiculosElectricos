# Usa una imagen oficial de Python como base
FROM python:3.11-slim
# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app
# Copia los archivos de dependencias
COPY requirements.txt .
# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Copia el resto del código fuente
COPY ./app ./app
# Expone el puerto donde se ejecutará FastAPI
EXPOSE 8000
# Comando para iniciar el servidor con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
