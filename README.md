MIDAS — Sistema de Predicción para Restaurante

Arquitectura Autosuficiente Certificada bajo OmniOps AI™

MIDAS es un sistema construido siguiendo los principios del estándar corporativo OmniOps AI™.  
Cumple los requisitos de seguridad, trazabilidad, reproducibilidad y separación de entornos exigidos por la normativa europea.  
La arquitectura está diseñada siguiendo prácticas enterprise, garantizando estabilidad, escalabilidad y gobernanza.

La demo permite verificar cómo el sistema cumple los principios fundamentales del estándar:  
- modularidad  
- trazabilidad  
- reproducibilidad  
- estabilidad operativa  
- explicabilidad  
- arquitectura autosuficiente  

---

1. ¿Qué es MIDAS?

MIDAS es un sistema de predicción inteligente para restaurantes que ofrece:

- Predicción de ventas diarias  
- Cálculo de personal necesario  
- Gestión de perecederos  
- Factores climáticos integrados  
- Gestión de eventos  
- Visualizaciones interactivas  
- Arquitectura escalable y autosuficiente  

---

2. Demo en Vivo

Acceso directo sin instalación:  
https://desirable-luck-production.up.railway.app

Características principales:  
- Predicciones dinámicas  
- Interfaz intuitiva  
- Sin dependencias externas  
- Visualizaciones avanzadas  
- Arquitectura modular  

---

3. Inicio Rápido

Opción 1: Usar en producción
https://desirable-luck-production.up.railway.app

Opción 2: Ejecutar localmente
`
git clone https://github.com/raquelmartinesbec-glitch/PROYECTO-MIDAS-DEMO.git
cd PROYECTO-MIDAS-DEMO
pip install -r requirements/requirements.txt
python scripts/run_local.py
`

Acceso local:  
http://localhost:8501

---

4. Arquitectura del Proyecto

`
PROYECTO-MIDAS-DEMO/
├── src/
│   ├── dashboard/
│   │   ├── app.py
│   │   └── utils/
├── config/
│   ├── railway.toml
│   └── .env.example
├── docs/
│   ├── README.md
│   ├── DEPLOY.md
│   └── CHANGELOG.md
├── scripts/
│   ├── deploy.sh
│   └── run_local.py
├── tests/
├── docker/
│   ├── Dockerfile
│   └── streamlit_config.toml
├── requirements/
│   └── requirements.txt
└── pyproject.toml
`

Beneficios:  
- Modularidad  
- Escalabilidad  
- Mantenibilidad  
- Automatización  
- Preparado para entornos enterprise  

---

5. Uso del Sistema

Panel lateral:  
- Fecha  
- Clima  
- Reservas  
- Evento  
- Asistentes  
- Precio medio  

Métricas principales:  
- Ventas estimadas  
- Personal necesario  
- Perecederos recomendados  

Visualizaciones:  
- Comparación de escenarios  
- Gráficos dinámicos  
- Información del algoritmo  

---

6. Algoritmo de Predicción

Factores utilizados:  
- Temporales  
- Climáticos  
- Reservas  
- Eventos  
- Estacionalidad  

Métricas de confianza:  
- Ventas: 92%  
- Personal: 88%  
- Perecederos: 90%  

Funciones clave:
`
calculate_prediction()
getsamplepredictions()
applyweatherfactor()
`

---

7. Stack Tecnológico

- Python  
- Streamlit  
- Plotly  
- Pandas  
- Docker  
- Railway  
- pyproject.toml  

Arquitectura:  
- Modular  
- Sin dependencias externas  
- Acceso universal  
- Predicciones en tiempo real  
- Manejo de errores integrado  
- Interfaz adaptable  

---

8. Despliegue y Automatización

Despliegue automático:
`
./scripts/deploy.sh
`

Ejecución local:
`
python scripts/run_local.py
streamlit run src/dashboard/app.py --server.port 8501
`

Docker:
`
docker build -f docker/Dockerfile -t midas-dashboard .
docker run -p 8501:8501 midas-dashboard
`

---

9. Mapeo a los 6 Pilares del Estándar OmniOps AI™

1. Gobernanza
Dónde se demuestra:  
- Panel lateral con parámetros controlados  
- Validaciones en cada entrada  
- Lógica centralizada en calculate_prediction()  

Artefactos visibles:  
- Controles de entrada  
- Reglas de negocio consistentes  

---

2. Seguridad y Aislamiento
Dónde se demuestra:  
- Sistema autosuficiente  
- Sin bases de datos externas  
- Sin llamadas a APIs  

Artefactos visibles:  
- Arquitectura contenida  
- Ejecución offline  

---

3. Reproducibilidad
Dónde se demuestra:  
- Predicciones deterministas  
- Código centralizado  
- Scripts estandarizados  

Artefactos visibles:  
- scripts/run_local.py  
- calculate_prediction()  

---

4. Trazabilidad
Dónde se demuestra:  
- Factores mostrados en pantalla  
- Impacto de cada parámetro visible  

Artefactos visibles:  
- Información del algoritmo  
- Comparación de escenarios  

---

5. Explicabilidad
Dónde se demuestra:  
- Factores climáticos, reservas y eventos explicados  
- Métricas de confianza visibles  

Artefactos visibles:  
- Desglose de factores  
- Métricas de precisión  

---

6. Estabilidad Operativa
Dónde se demuestra:  
- Cálculos instantáneos  
- Sin dependencias externas  
- Arquitectura modular  

Artefactos visibles:  
- Dockerfile  
- Configuración Railway  
- Scripts de despliegue  

---

10. Narrativa del Caso de Uso

Una empresa quiere desplegar una aplicación interna de predicción para mejorar la planificación diaria.  
OmniOps AI™ garantiza que:

- el sistema es seguro  
- los datos están aislados  
- las predicciones son reproducibles  
- las decisiones son trazables  
- los resultados son explicables  
- la operación es estable  

MIDAS muestra cómo se vería un módulo interno certificado bajo este estándar.

---

11. Limitaciones Intencionadas de la Demo

Esta demo está diseñada únicamente para mostrar un módulo autosuficiente bajo OmniOps AI™.  
Por motivos de seguridad y propiedad intelectual, la demo presenta las siguientes limitaciones:

- No utiliza datos reales ni históricos.  
- No incluye modelos entrenados con datos corporativos.  
- No incorpora bases vectoriales ni embeddings.  
- No muestra la arquitectura completa del estándar OmniOps AI™.  
- No expone flujos de gobernanza interna ni certificación.  
- No representa el rendimiento final en producción.  
- No permite integraciones externas.  

---

12. Qué No Incluye MIDAS

MIDAS es un módulo demostrativo.  
No incluye:

- El estándar OmniOps AI™ completo  
- Fases, criterios, patrones o artefactos del estándar  
- Documentación interna de gobernanza o auditoría  
- Procesos de despliegue corporativo  
- Modelos avanzados de IA entrenados  
- Arquitecturas multi‑entorno o multi‑tenant  
- Mecanismos de observabilidad avanzada  
- Controles normativos completos  

---

13. Documentación y Soporte

Documentación completa en /docs.  
Repositorio: GitHub.  
Demo: Railway.