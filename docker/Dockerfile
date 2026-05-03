# ══════════════════════════════════════════════════════════════════════════════
# Dockerfile - MIDAS Dashboard RAILWAY OPTIMIZED
# VERSION 5.0.0 - RAILWAY CRASH FIX - USER ROOT SIMPLIFIED
# SIMPLIFIED: No user creation, direct port binding, streamlined
# ══════════════════════════════════════════════════════════════════════════════

FROM python:3.11-slim

# Metadata
LABEL maintainer="MIDAS Dashboard" \
      version="5.0.0" \
      description="Dashboard independiente Railway optimizado"

# Variables de entorno esenciales
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema mínimas
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copiar requirements e instalar dependencias Python
COPY requirements/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY dashboard/ ./dashboard/
COPY docker/streamlit_config.toml ~/.streamlit/config.toml

# Railway dynamic port exposure
EXPOSE 8501

# Comando optimizado para Railway (sin usuario, directo)
CMD ["streamlit", "run", "dashboard/app.py", "--server.address", "0.0.0.0", "--server.port", "8501", "--server.headless", "true"]