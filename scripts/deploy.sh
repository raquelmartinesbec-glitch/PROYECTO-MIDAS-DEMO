#!/bin/bash
# ── deploy.sh - Script de despliegue para MIDAS ─────────────────────────
# Script para facilitar el despliegue en Railway

set -e

echo "🚀 MIDAS - Script de Despliegue"
echo "================================"

# Verificar que estamos en el directorio correcto
if [ ! -f "config/railway.toml" ]; then
    echo "❌ Error: Ejecutar desde la raíz del proyecto"
    exit 1
fi

# Verificar archivos críticos
echo "🔍 Verificando archivos críticos..."
if [ ! -f "src/dashboard/app.py" ]; then
    echo "❌ Error: src/dashboard/app.py no encontrado"
    exit 1
fi

if [ ! -f "requirements/requirements.txt" ]; then
    echo "❌ Error: requirements/requirements.txt no encontrado"
    exit 1
fi

echo "✅ Archivos verificados"

# Limpiar archivos temporales
echo "🧹 Limpiando archivos temporales..."
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
rm -f test_*.txt 2>/dev/null || true

echo "✅ Limpieza completada"

# Commit y push
echo "📦 Subiendo cambios a GitHub..."
git add .
git commit -m "deploy: preparing for Railway deployment $(date +%Y-%m-%d)"
git push origin main

echo "🎯 Despliegue iniciado"
echo "📍 URL: https://railway.app"
echo "✅ ¡Completado!"