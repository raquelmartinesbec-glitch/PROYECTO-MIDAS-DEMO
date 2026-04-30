# 🚀 Deploy en Railway — MIDAS Dashboard Independiente

## Arquitectura desplegada

```
GitHub Repo (PROYECTO-MIDAS-DEMO)
└── Servicio único: midas-dashboard → railway.dashboard.toml → :PORT → Dashboard Streamlit
```

El dashboard es completamente independiente y no requiere APIs externas ni servicios adicionales.

---

## Prerrequisitos

- Cuenta en [railway.app](https://railway.app) (registrar con GitHub)
- Fork de este repositorio en tu cuenta de GitHub

---

## PASO 1 — Fork del repositorio

1. Ir a: https://github.com/raquelmartinesbec-glitch/PROYECTO-MIDAS-DEMO
2. Hacer clic en **Fork** (esquina superior derecha)
3. Elegir tu cuenta personal de GitHub
4. Esperar a que se complete el fork

---

## PASO 2 — Crear el Proyecto en Railway

1. Ir a [railway.app](https://railway.app) → **New Project**
2. Seleccionar **Deploy from GitHub repo**
3. Autorizar Railway en GitHub si es necesario
4. Seleccionar tu repositorio forked: `<tu-usuario>/PROYECTO-MIDAS-DEMO`
5. Railway crea automáticamente el servicio

---

## PASO 3 — Configurar el Servicio Dashboard

Railway usará automáticamente `railway.dashboard.toml` que ya está configurado correctamente.

### Verificar configuración:

1. Una vez creado el servicio, ir a **Settings → Source**
2. En **Config file path** debe estar: `railway.dashboard.toml`
3. Si no está, añadirlo manualmente y hacer redeploy

### Verificar variables de entorno:

- **No necesitas configurar variables adicionales**
- El dashboard es completamente autosuficiente
- Railway detecta automáticamente el puerto desde el código

---

## PASO 4 — Obtener la URL pública

1. Ir a **Settings → Networking → Generate Domain** 
2. Railway generará una URL como: `https://tu-proyecto-production.up.railway.app`
3. **¡Listo!** El dashboard estará disponible en esa URL

---

## URLs finales para la demo

| Componente | URL | Descripción |
|------------|-----|-------------|
| **Dashboard completo** | `https://<tu-url>.up.railway.app` | Interfaz principal autosuficiente |

---

## Comandos útiles en Railway CLI (opcional)

```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login
railway login

# Ver logs del servicio
railway logs

# Redeploy manual
railway redeploy
```

---

## Solución de problemas

| Síntoma | Causa probable | Solución |
|---------|---------------|----------|
| Build falla con `ModuleNotFoundError` | Dependencias no encontradas | Verificar `requirements/dashboard.txt` |
| Dashboard no carga | App tarda en arrancar | Esperar ~1-2 minutos después del deploy |
| Página en blanco | Puerto incorrecto | Verificar que `railway.dashboard.toml` esté configurado |
| Error 503 | Servicio no iniciado | Ver logs: `railway logs` |

---

## Checklist antes de la demostración

- [ ] `https://<tu-url>` → Dashboard carga correctamente
- [ ] Controls sidebar funcionan (fecha, clima, reservas, etc.)
- [ ] Predicciones cambian al modificar parámetros
- [ ] Gráficos comparativos se muestran correctamente  
- [ ] Información del sistema aparece en expandibles

---

## Características del Sistema Desplegado

### ✅ **Lo que incluye:**
- **Dashboard completo** con interfaz Streamlit
- **Cálculos de predicción** integrados localmente
- **Visualizaciones interactivas** con Plotly
- **Sin dependencias externas** - completamente autosuficiente
- **Responsive design** - funciona en móvil y desktop

### ⚡ **Beneficios:**
- **Despliegue simple:** Solo un servicio
- **Sin configuración:** No requiere variables de entorno
- **Alta disponibilidad:** Sin puntos de falla externos
- **Rendimiento óptimo:** Sin latencia de APIs externas
- **Mantenimiento mínimo:** Sin servicios adicionales que gestionar

---

## Personalización Post-Despliegue

Si quieres personalizar el sistema después del despliegue:

1. Hacer cambios en tu fork del repositorio
2. Hacer commit y push a GitHub
3. Railway automáticamente detecta los cambios y redespliega
4. No requiere configuración adicional

---

**🎯 El dashboard estará completamente funcional y listo para usar con una sola URL.**
