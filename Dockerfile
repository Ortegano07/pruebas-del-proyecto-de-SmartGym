FROM python:3.12-slim

WORKDIR /app

# Actualiza pip
RUN pip install --upgrade pip

# Instalar dependencias del sistema para psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias Python
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Para produccion, empaquetar dentro de la imagen
COPY . .

# Copiar el resto del código
#COPY ./app /app/app
#COPY .env /app/.env     <- Para eso esta env_file en el .yml


# Puerto de la API
EXPOSE 8000

# Comando para ejecutar
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]