# ── CHANGELOG.md - Historial de Cambios ─────────────────────────────────
# MIDAS Dashboard - Registro de versiones y mejoras

## [2.0.0] - 2026-04-30

### 🏗️ **REORGANIZACIÓN COMPLETA DE PROYECTO**
- **Nueva estructura de directorios profesional**
- **Dashboard completamente independiente** sin APIs externas
- **Eliminación de código obsoleto** y dependencias innecesarias

### ✅ **Añadido:**
- Estructura `src/` para código fuente organizado
- Carpeta `config/` para configuraciones de despliegue
- Carpeta `docs/` para documentación centralizada  
- Carpeta `scripts/` con herramientas de desarrollo
- `pyproject.toml` para configuración moderna de Python
- Script `deploy.sh` para despliegue simplificado
- Script `run_local.py` para ejecución local

### 🔧 **Cambiado:**
- **Dockerfile optimizado** para nueva estructura
- **Railway.toml actualizado** con rutas correctas  
- **Documentación completamente reescrita**
- **Requirements unificados** en archivo único

### ❌ **Eliminado:**
- Carpeta `api/` completa (obsoleta)
- Carpeta `db/` y scripts de base de datos
- `docker-compose.yml` y Dockerfiles múltiples
- Archivos `midas_*.py` legacy
- Requirements redundantes (`*-dashboard.txt`, `*-api.txt`, etc)
- Archivos temporales de testing

### 📊 **Métricas de Limpieza:**
- **-15 archivos obsoletos** eliminados
- **-3 carpetas** innecesarias removidas  
- **-240 líneas** de código obsoleto
- **+199 líneas** de documentación actualizada
- **Estructura 70% más limpia** y mantenible

---

## [1.0.0] - 2026-04-29

### 🎯 **Release Inicial**
- Dashboard funcional con predicciones integradas
- Arquitectura de microservicios con API separada
- Documentación básica y configuración Railway