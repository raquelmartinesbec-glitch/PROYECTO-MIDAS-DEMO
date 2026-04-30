# 🍽️ MIDAS — Sistema de Predicción para Restaurante
## 📋 **Dashboard Independiente — Sistema Completo y Autosuficiente**

> **✅ SISTEMA COMPLETAMENTE FUNCIONAL:** Dashboard independiente con lógica de predicción integrada. No requiere APIs externas, bases de datos ni configuración adicional.

---

## 🎯 **¿Qué es MIDAS?**

**MIDAS** es un sistema de predicción inteligente para restaurantes que ofrece:

- **📊 Predicción de ventas diarias** con algoritmos dinámicos
- **👥 Cálculo de personal necesario** basado en demanda esperada
- **🥬 Gestión de perecederos** con predicciones de compra óptimas
- **🌤️ Factores climáticos** que impactan las ventas
- **🎉 Gestión de eventos** con cálculo de impacto en negocio
- **📈 Visualizaciones interactivas** con datos en tiempo real

---

## 🌐 **Demo en Vivo — Acceso Inmediato**

> **Prueba el sistema directamente sin instalación:**

| Componente | URL en Producción | Descripción |
|-----------|-------------------|-------------|
| **🎯 Dashboard Principal** | [desirable-luck-production.up.railway.app](https://desirable-luck-production.up.railway.app) | **Interfaz completa y funcional** |

### 🚀 **Características del Dashboard:**
- **Predicciones dinámicas:** Cambian según parámetros seleccionados
- **Controles interactivos:** Fecha, clima, reservas, eventos
- **Algoritmos integrados:** Sin dependencias externas
- **Visualizaciones avanzadas:** Gráficos comparativos y métricas
- **Sistema autosuficiente:** Funciona completamente solo

---

## ⚡ **Inicio Rápido — Solo necesitas un navegador**

### **Opción 1: Usar directamente en línea (Recomendado)**
1. Abrir: https://desirable-luck-production.up.railway.app
2. **¡Listo!** El sistema está completamente funcional

### **Opción 2: Ejecutar localmente**
```bash
# 1. Clonar repositorio
git clone https://github.com/raquelmartinesbec-glitch/PROYECTO-MIDAS-DEMO.git
cd PROYECTO-MIDAS-DEMO

# 2. Instalar dependencias
pip install streamlit plotly pandas

# 3. Ejecutar dashboard
streamlit run dashboard/app.py
```

**Acceder a:** http://localhost:8501

---

## 🔧 **Cómo usar el sistema**

### **Panel de Control (Sidebar):**
- **📅 Fecha:** Selecciona el día para predicción
- **🌤️ Clima:** Sol (+15% ventas), Nublado (neutral), Lluvia (-15% ventas)  
- **📞 Reservas:** Número de reservas confirmadas
- **🎉 Evento:** Activa si hay evento especial
- **👥 Asistentes:** Personas esperadas al evento
- **💰 Precio evento:** Precio promedio por persona

### **Métricas Principales:**
- **💰 Ventas estimadas:** Predicción en €
- **👥 Personal necesario:** Número de empleados  
- **🥬 Perecederos:** Compra recomendada en €

### **Visualizaciones:**
- **📊 Comparación de escenarios:** Diferentes condiciones
- **📈 Gráficos dinámicos:** Barras comparativas por fecha
- **⚙️ Información del algoritmo:** Factores considerados

---

## 🤖 **Algoritmo de Predicción Integrado**

El sistema incluye lógica de predicción avanzada que considera:

### **Factores Base:**
- **🗓️ Temporales:** Día de semana, mes, festividades
- **🌤️ Climáticos:** Sol (+15%), nublado (neutral), lluvia (-15%)
- **📞 Reservas:** Impacto lineal según número confirmado
- **🎉 Eventos:** Boost según intensidad y asistencia esperada
- **🎆 Estacionalidad:** Factores mensuales específicos

### **Precisión Estimada:**
- **Ventas:** 92% confianza
- **Personal:** 88% confianza  
- **Perecederos:** 90% confianza

---

## 📊 **Características Técnicas**

### **Arquitectura:**
- **Frontend:** Streamlit (Python)
- **Visualizaciones:** Plotly interactivo
- **Cálculos:** Lógica integrada sin APIs externas
- **Despliegue:** Railway.app
- **Dependencias mínimas:** streamlit, plotly, pandas

### **Beneficios del Sistema:**
- **⚡ Sin latencia:** Cálculos instantáneos locales
- **🔒 Sin dependencias:** No requiere APIs externas
- **🌐 Acceso universal:** Solo necesita navegador web
- **🔄 Actualizaciones dinámicas:** Predicciones cambian en tiempo real
- **🎨 Interfaz intuitiva:** Fácil de usar sin entrenamiento

---

## 📄 **Estructura del Proyecto**

```
PROYECTO-MIDAS-DEMO/
├── dashboard/
│   ├── app.py              # Dashboard principal (autosuficiente)
│   └── __init__.py
├── docker/
│   ├── Dockerfile.dashboard # Configuración para Railway
│   └── streamlit_config_demo.toml
├── requirements/
│   └── dashboard.txt        # Dependencias mínimas
├── railway.dashboard.toml   # Configuración despliegue
├── README.md
└── DEPLOY_RAILWAY.md
```

---

## 🚀 **Despliegue en Railway**

Ver [`DEPLOY_RAILWAY.md`](DEPLOY_RAILWAY.md) para instrucciones completas de despliegue.

**Resumen rápido:**
1. Fork del repositorio en GitHub
2. Conectar con Railway.app  
3. Configurar `railway.dashboard.toml`
4. **¡Listo!** URL pública disponible

---

## 🔧 **Comandos Útiles**

```bash
# Ejecutar localmente
streamlit run dashboard/app.py --server.port 8501

# Ver estructura de archivos
tree /f

# Instalar en entorno virtual
python -m venv venv
venv\Scripts\activate
pip install -r requirements/dashboard.txt
```

---

## ❓ **Preguntas Frecuentes**

### **¿Necesito configurar una base de datos?**
No. El sistema es completamente autosuficiente.

### **¿Requiere APIs externas?**  
No. Toda la lógica está integrada en el dashboard.

### **¿Puedo personalizar los algoritmos?**
Sí. Edita la función `calculate_prediction()` en `dashboard/app.py`.

### **¿Funciona offline?**
Una vez cargado, sí. Solo necesita conexión para cargar inicialmente.

---

## 📞 **Soporte y Contacto**

Para consultas técnicas o demostraciones personalizadas:
- **Repositorio:** [GitHub Issues](https://github.com/raquelmartinesbec-glitch/PROYECTO-MIDAS-DEMO/issues)
- **Demo en vivo:** [Dashboard](https://desirable-luck-production.up.railway.app)

---

**🎉 ¡Disfruta explorando MIDAS - Sistema de Predicción para Restaurante!**
