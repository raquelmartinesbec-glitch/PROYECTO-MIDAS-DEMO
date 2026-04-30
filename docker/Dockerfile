# ══════════════════════════════════════════════════════════════════════════════
# Dockerfile - MIDAS Dashboard Independiente
# Optimizado para Railway.app con nueva estructura de directorios  
# ══════════════════════════════════════════════════════════════════════════════

FROM python:3.11-slim

# Metadata
LABEL maintainer="MIDAS Dashboard" \
      version="2.0.0" \
      description="Dashboard independiente para predicciones de restaurante"

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (mínimas)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias Python
COPY requirements/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY dashboard/ ./dashboard/
COPY docker/streamlit_config.toml ~/.streamlit/config.toml

# Crear usuario no-root para seguridad
RUN groupadd -r midas && useradd -r -g midas midas
RUN chown -R midas:midas /app
USER midas

# Exponer puerto dinámico
EXPOSE $PORT

# Comando por defecto (Railway sobreescribirá con startCommand)
CMD ["streamlit", "run", "dashboard/app.py", "--server.address", "0.0.0.0"]