# 🍽️ MIDAS Demo API

> **API de demostración** para sistema de predicción de restaurante deployada en Railway.app

## 🚀 **URLs en vivo:**
- **📊 API Principal**: [Ver demo](/)
- **📚 Documentación interactiva**: [/docs](/docs) ← **PRUEBA AQUÍ** 
- **💓 Health Check**: [/health](/health)
- **🎯 Predicción completa**: [/predict/full](/predict/full)

## ⚡ **Endpoints principales:**
- `GET /predict/sales` - Predicción de ventas
- `GET /predict/staff` - Personal necesario  
- `GET /predict/perishables` - Productos perecederos
- `GET /predict/full` - Predicción completa
- `GET /models` - Información de modelos

## 📊 **Escenarios disponibles:**
- **quiet**: Día tranquilo (75% ventas base)
- **normal**: Operación estándar (100% ventas base) 
- **busy**: Día ocupado (135% ventas base)

## 💡 **Ejemplo de uso:**
```bash
# Predicción para día ocupado
curl "https://tu-domain.railway.app/predict/full?scenario=busy"
```

## ⚠️ **Nota importante:**
Esta es una **API de demostración** con datos simulados. El código completo, modelos de Machine Learning y lógica de negocio están protegidos por **propiedad intelectual**.

---

**💼 Desarrollado por:** [Tu Nombre]  
**🎯 Propósito:** Presentación técnica  
**⚡ Stack:** FastAPI + Python + Railway.app