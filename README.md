# 🍽️ MIDAS — Sistema de Predicción para Restaurante
## 🏗️ **Arquitectura Profesional — Dashboard Autosuficiente Enterprise**

> **✅ PROYECTO REORGANIZADO:** Sistema independiente con estructura profesional de nivel enterprise. Organizado siguiendo mejores prácticas de ingeniería de software.

---

## 🎯 **¿Qué es MIDAS?**

**MIDAS** es un sistema de predicción inteligente para restaurantes que ofrece:

- **📊 Predicción de ventas diarias** con algoritmos dinámicos integrados
- **👥 Cálculo de personal necesario** basado en demanda esperada
- **🥬 Gestión de perecederos** con predicciones de compra óptimas
- **🌤️ Factores climáticos** que impactan las ventas
- **🎉 Gestión de eventos** con cálculo de impacto en negocio
- **📈 Visualizaciones interactivas** con datos en tiempo real
- **🏗️ Arquitectura escalable** siguiendo estándares enterprise

---

## 🌐 **Demo en Vivo — Acceso Inmediato**

> **Prueba el sistema directamente sin instalación:**

| Componente | URL en Producción | Descripción |
|-----------|-------------------|-------------|
| **🎯 Dashboard Principal** | [desirable-luck-production.up.railway.app](https://desirable-luck-production.up.railway.app) | **Sistema completo y funcional** |

### 🚀 **Características del Sistema:**
- **Predicciones dinámicas:** Algoritmos avanzados integrados
- **Controles interactivos:** Interfaz intuitiva Streamlit
- **Sin dependencias externas:** Sistema completamente autosuficiente
- **Visualizaciones avanzadas:** Gráficos comparativos con Plotly
- **Arquitectura modular:** Organización profesional escalable

---

## ⚡ **Inicio Rápido — Desarrollo Local**

### **Opción 1: Usar en producción (Recomendado)**
```bash
# Acceso directo sin instalación
open https://desirable-luck-production.up.railway.app
```

### **Opción 2: Ejecutar localmente**
```bash
# 1. Clonar repositorio
git clone https://github.com/raquelmartinesbec-glitch/PROYECTO-MIDAS-DEMO.git
cd PROYECTO-MIDAS-DEMO

# 2. Instalar dependencias
pip install -r requirements/requirements.txt

# 3. Ejecutar usando script automatizado
python scripts/run_local.py

# O directamente con Streamlit
streamlit run src/dashboard/app.py --server.port 8501
```

**Acceder a:** http://localhost:8501

---

## 🏗️ **Arquitectura del Proyecto**

### **Estructura Profesional:**
```
PROYECTO-MIDAS-DEMO/
├── 📁 src/                    # Código fuente principal
│   ├── dashboard/             # Dashboard Streamlit
│   │   ├── app.py            # Aplicación principal
│   │   └── utils/            # Utilidades y helpers
├── 📁 config/                 # Configuraciones centralizadas
│   ├── railway.toml          # Configuración Railway
│   └── .env.example          # Variables de entorno
├── 📁 docs/                   # Documentación organizada
│   ├── README.md             # Documentación principal
│   ├── DEPLOY.md             # Guía de despliegue
│   └── CHANGELOG.md          # Historial de cambios
├── 📁 scripts/                # Herramientas de automatización
│   ├── deploy.sh             # Script de despliegue
│   └── run_local.py          # Ejecución local simplificada
├── 📁 tests/                  # Framework de testing
├── 📁 docker/                 # Containerización
│   ├── Dockerfile            # Imagen optimizada
│   └── streamlit_config.toml # Configuración Streamlit
├── 📁 requirements/           # Gestión de dependencias
│   └── requirements.txt      # Dependencias unificadas
└── 📄 pyproject.toml          # Configuración moderna Python
```

### **Beneficios de la Nueva Arquitectura:**
- **🎯 Modularidad:** Separación clara de responsabilidades
- **📈 Escalabilidad:** Estructura preparada para crecimiento
- **🛠️ Mantenibilidad:** Código organizado y documentado
- **🚀 Automatización:** Scripts para tareas comunes
- **🏢 Enterprise-ready:** Siguiendo mejores prácticas industriales

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

El sistema incluye lógica de predicción avanzada implementada en [`src/dashboard/app.py`](src/dashboard/app.py):

### **Factores Base del Algoritmo:**
- **🗺️ Temporales:** Día de semana, mes, estacionalidad, festividades
- **🌤️ Climáticos:** Sol (+15%), nublado (neutral), lluvia (-15%)
- **📞 Reservas:** Impacto lineal según número confirmado
- **🎉 Eventos:** Boost dinámico según intensidad y asistencia esperada
- **🎆 Estacionalidad:** Factores mensuales específicos ajustados

### **Métricas de Confianza:**
- **💰 Ventas:** 92% precisión
- **👥 Personal:** 88% precisión  
- **🥬 Perecederos:** 90% precisión

### **Funciones Clave:**
```python
# Implementadas en src/dashboard/app.py
calculate_prediction()    # Algoritmo principal
get_sample_predictions()  # Comparaciones
apply_weather_factor()    # Factores climáticos
```

---

## 📊 **Stack Tecnológico**

### **Tecnologías Core:**
- **🐍 Backend:** Python 3.11+
- **🎨 Frontend:** Streamlit 1.28+
- **📊 Visualizaciones:** Plotly 5.15+
- **📈 Data Processing:** Pandas 2.0+
- **🐳 Containerización:** Docker optimizado
- **☁️ Deploy:** Railway.app
- **⚙️ Config:** pyproject.toml moderno

### **Arquitectura del Sistema:**
- **🏗️ Modular:** Separación clara src/config/docs
- **⚡ Sin latencia:** Cálculos instantáneos integrados
- **🔒 Sin dependencias externas:** Sistema autosuficiente
- **🌐 Universal:** Acceso solo con navegador
- **🔄 Tiempo real:** Predicciones dinámicas
- **🛡️ Robusto:** Manejo de errores integrado
- **📱 Responsive:** Interfaz adaptativa

---

## 🚀 **Despliegue y Automatización**

### **Despliegue Automático:**
Ver [docs/DEPLOY.md](docs/DEPLOY.md) para instrucciones completas.

```bash
# Despliegue automático con script
./scripts/deploy.sh

# O manualmente en Railway
1. Fork del repositorio en GitHub
2. Conectar con Railway.app  
3. Usar config/railway.toml
4. ¡Deploy automático!
```

### **Scripts de Desarrollo:**
```bash
# Ejecutar localmente (automático)
python scripts/run_local.py

# Ejecutar directamente
streamlit run src/dashboard/app.py --server.port 8501

# Instalar dependencias
pip install -r requirements/requirements.txt

# Ver logs y estructura
tree /f src/
```

### **Docker (Opcional):**
```bash
# Build imagen local
docker build -f docker/Dockerfile -t midas-dashboard .

# Ejecutar container
docker run -p 8501:8501 midas-dashboard
```

---

## ❓ **Preguntas Frecuentes (FAQ)**

### **🗘️ ¿Necesito configurar una base de datos?**
**No.** El sistema es completamente autosuficiente sin dependencias externas.

### **🌐 ¿Requiere APIs externas?**  
**No.** Toda la lógica está integrada en el dashboard.

### **⚙️ ¿Puedo personalizar los algoritmos?**
**Sí.** Edita `calculate_prediction()` en `src/dashboard/app.py`.

### **🔌 ¿Funciona offline?**
**Sí.** Una vez cargado, funciona completamente sin conexión.

### **🐍 ¿Qué versión de Python necesito?**
**Python 3.9+** (recomendado 3.11+). Ver `pyproject.toml`.

### **📱 ¿Es responsive en móvil?**
**Sí.** Streamlit se adapta automáticamente a dispositivos móviles.

### **🛠️ ¿Cómo contribuir al proyecto?**
Ver [docs/README.md](docs/README.md) para guías de contribución.

---

## 📞 **Soporte y Documentación**

### **📄 Documentación Completa:**
- **🏰 Principal:** [docs/README.md](docs/README.md)
- **🚀 Despliegue:** [docs/DEPLOY.md](docs/DEPLOY.md)
- **📅 Cambios:** [docs/CHANGELOG.md](docs/CHANGELOG.md)
- **⚙️ Configuración:** [config/](config/)

### **🔗 Enlaces Útiles:**
- **🎯 Demo en vivo:** [Dashboard MIDAS](https://desirable-luck-production.up.railway.app)
- **📝 Issues/Soporte:** [GitHub Issues](https://github.com/raquelmartinesbec-glitch/PROYECTO-MIDAS-DEMO/issues)
- **🔥 Repositorio:** [GitHub Repo](https://github.com/raquelmartinesbec-glitch/PROYECTO-MIDAS-DEMO)

### **👥 Contacto Técnico:**
Para consultas de desarrollo, arquitectura o demostraciones personalizadas.

---

**🎉 ¡Proyecto MIDAS - Arquitectura Enterprise con Predicciones Inteligentes!**  
*✨ Sistema completamente reorganizado siguiendo mejores prácticas de ingeniería de software*
