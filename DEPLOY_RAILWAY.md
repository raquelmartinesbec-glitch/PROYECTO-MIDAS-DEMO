# 🚀 Deploy en Railway — MIDAS Demo (2 servicios)

## Arquitectura desplegada

```
GitHub Repo (midas-demo)
├── Servicio 1: midas-api        → railway.toml           → :PORT → /docs /health /predict/*
└── Servicio 2: midas-dashboard  → railway.dashboard.toml → :PORT → dashboard Streamlit
```

Los dos servicios se comunican a través de la URL pública de la API.

---

## Prerrequisitos

- Cuenta en [railway.app](https://railway.app) (registrar con GitHub)
- Repositorio en GitHub con este código

---

## PASO 1 — Subir el código a GitHub

```bash
cd "C:\Desarrollo\github\PROYECTO MIDAS DEMO"

git init
git add .
git commit -m "feat: deploy demo MIDAS"

# Crear repo en github.com → New repository → nombre: midas-demo
git remote add origin https://github.com/<tu-usuario>/midas-demo.git
git push -u origin main
```

---

## PASO 2 — Crear el Proyecto en Railway

1. Ir a [railway.app](https://railway.app) → **New Project**
2. Seleccionar **Deploy from GitHub repo**
3. Autorizar Railway en GitHub y seleccionar el repo `midas-demo`
4. Railway crea automáticamente el primer servicio

---

## PASO 3 — Configurar Servicio 1: API (`midas-api`)

Railway usará `railway.toml` por defecto (ya está configurado correctamente).

1. Esperar a que el build termine (~2 min)
2. Ir a **Settings → Networking → Generate Domain**
3. Copiar la URL generada: `https://midas-demo-api-xxxx.railway.app`
4. Verificar que funciona: `https://<url>/health` debe devolver `{"status": "ok"}`

---

## PASO 4 — Añadir Servicio 2: Dashboard (`midas-dashboard`)

1. En el Proyecto Railway → **New** → **GitHub Repo** → seleccionar el mismo repo
2. Una vez creado el servicio, ir a su **Settings → Source**
3. En **Config file path** escribir: `railway.dashboard.toml`
4. Guardar → Railway hace redeploy automático con la config del dashboard

### Añadir variable de entorno al Dashboard

En el servicio `midas-dashboard` → **Variables** → **New Variable**:

| Variable | Valor |
|----------|-------|
| `API_URL` | `https://<url-del-servicio-api>` |

> Usar la URL pública del Servicio 1 copiada en el Paso 3.

5. Ir a **Settings → Networking → Generate Domain** del servicio dashboard
6. Verificar: la URL del dashboard debe abrir el panel Streamlit

---

## URLs finales para la presentación

| Servicio | URL | Qué mostrar |
|----------|-----|-------------|
| **API Docs** | `https://<api-url>/docs` | Swagger UI interactivo |
| **Health** | `https://<api-url>/health` | Estado en tiempo real |
| **Predicción completa** | `https://<api-url>/predict/full` | JSON con las 3 predicciones |
| **Dashboard** | `https://<dashboard-url>` | Panel visual completo |

---

## Comandos útiles en Railway CLI (opcional)

```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login
railway login

# Ver logs del servicio API
railway logs --service midas-api

# Ver logs del dashboard
railway logs --service midas-dashboard

# Redeploy manual
railway redeploy --service midas-api
```

---

## Solución de problemas

| Síntoma | Causa probable | Solución |
|---------|---------------|----------|
| Build falla con `ModuleNotFoundError` | Dependencias no encontradas | Verificar `requirements-demo.txt` |
| Dashboard muestra "API no disponible" | `API_URL` incorrecto | Revisar variable de entorno en dashboard service |
| Health check falla | App tarda en arrancar | `healthcheckTimeout = 300` ya está configurado |
| Puerto incorrecto | App no lee `$PORT` | Start command ya usa `$PORT` explícitamente |

---

## Checklist antes de la presentación

- [ ] `https://<api-url>/health` → `{"status": "ok"}`
- [ ] `https://<api-url>/docs` → Swagger UI carga correctamente
- [ ] `https://<api-url>/predict/full` → devuelve predicciones JSON
- [ ] `https://<dashboard-url>` → dashboard carga sin errores
- [ ] Dashboard muestra métricas (aunque sean datos de demo)
