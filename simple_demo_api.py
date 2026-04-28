#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════════════════
# simple_demo_api.py — API completamente funcional para demostración
#
# USO: python simple_demo_api.py
# URL: http://localhost:8001
# ══════════════════════════════════════════════════════════════════════════════

from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uvicorn
import os

# ── Configuración de la aplicación ─────────────────────────────────────────────
app = FastAPI(
    title="MIDAS Demo API",
    description="API de demostración para sistema de predicción de restaurante",
    version="demo-1.0.0"
)

# ── Modelos de datos ───────────────────────────────────────────────────────────
class PredictionRequest(BaseModel):
    """Entrada simplificada para demo"""
    date: Optional[str] = "2026-04-28"
    scenario: Optional[str] = "normal"  # normal, busy, quiet

class PredictionResult(BaseModel):
    """Respuesta de predicción"""
    date: str
    type: str
    value: float
    confidence: float
    scenario: str
    timestamp: str

# ── Endpoints ──────────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    """Información principal de la API demo"""
    # Detectar si está en Railway
    is_production = os.getenv("RAILWAY_ENVIRONMENT_NAME") is not None
    base_url = os.getenv("RAILWAY_PUBLIC_DOMAIN", "localhost:8001")
    
    return {
        "name": "MIDAS - Sistema de Predicción para Restaurante",
        "version": "demo-1.0.0", 
        "status": "✅ funcionando",
        "environment": "production" if is_production else "development",
        "demo_mode": True,
        "base_url": f"https://{base_url}" if is_production else f"http://{base_url}",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "sales": "/predict/sales", 
            "staff": "/predict/staff",
            "perishables": "/predict/perishables",
            "full": "/predict/full",
            "models": "/models"
        },
        "note": "API de demostración - El código completo está protegido por PI",
        "deployment": "Deployado en Railway.app" if is_production else "Ejecutando localmente"
    }

@app.get("/health")
async def health():
    """Health check"""
    return {
        "status": "ok",
        "models": ["sales_model", "staff_model", "perishables_model"],
        "accuracy": {"sales": 0.92, "staff": 0.89, "perishables": 0.86},
        "timestamp": datetime.now().isoformat()
    }

@app.post("/predict/sales", response_model=PredictionResult)
@app.get("/predict/sales", response_model=PredictionResult)  # GET también para facilidad
async def predict_sales(request: Optional[PredictionRequest] = None):
    """Predicción de ventas diarias"""
    if not request:
        request = PredictionRequest()
    
    # Simulación inteligente basada en escenario
    base_sales = 2450
    scenarios = {"quiet": 0.75, "normal": 1.0, "busy": 1.35}
    multiplier = scenarios.get(request.scenario, 1.0)
    prediction = base_sales * multiplier
    
    return PredictionResult(
        date=request.date,
        type="sales",
        value=round(prediction, 2),
        confidence=0.92,
        scenario=request.scenario,
        timestamp=datetime.now().isoformat()
    )

@app.post("/predict/staff", response_model=PredictionResult)
@app.get("/predict/staff", response_model=PredictionResult)
async def predict_staff(request: Optional[PredictionRequest] = None):
    """Predicción de personal necesario"""
    if not request:
        request = PredictionRequest()
    
    staff_needed = {"quiet": 6, "normal": 8, "busy": 12}
    prediction = staff_needed.get(request.scenario, 8)
    
    return PredictionResult(
        date=request.date,
        type="staff", 
        value=prediction,
        confidence=0.89,
        scenario=request.scenario,
        timestamp=datetime.now().isoformat()
    )

@app.post("/predict/perishables", response_model=PredictionResult)
@app.get("/predict/perishables", response_model=PredictionResult)
async def predict_perishables(request: Optional[PredictionRequest] = None):
    """Predicción de productos perecederos"""
    if not request:
        request = PredictionRequest()
    
    perishables_budget = {"quiet": 350, "normal": 480, "busy": 650}
    prediction = perishables_budget.get(request.scenario, 480)
    
    return PredictionResult(
        date=request.date,
        type="perishables",
        value=prediction,
        confidence=0.86,
        scenario=request.scenario,
        timestamp=datetime.now().isoformat()
    )

@app.post("/predict/full")
@app.get("/predict/full")
async def predict_full(request: Optional[PredictionRequest] = None):
    """Predicción completa - todos los tipos"""
    if not request:
        request = PredictionRequest()
        
    # Obtener todas las predicciones
    sales = await predict_sales(request)
    staff = await predict_staff(request)
    perishables = await predict_perishables(request)
    
    # Calcular métricas agregadas
    avg_confidence = (sales.confidence + staff.confidence + perishables.confidence) / 3
    total_cost = staff.value * 25 + perishables.value  # €25/hora personal + perecederos
    
    return {
        "date": request.date,
        "scenario": request.scenario,
        "predictions": {
            "sales": sales.model_dump(),
            "staff": staff.model_dump(), 
            "perishables": perishables.model_dump()
        },
        "summary": {
            "expected_revenue": sales.value,
            "total_operational_cost": round(total_cost, 2),
            "estimated_profit": round(sales.value - total_cost, 2),
            "avg_confidence": round(avg_confidence, 2),
            "recommendation": get_recommendation(request.scenario)
        },
        "generated_at": datetime.now().isoformat()
    }

@app.get("/models")
async def models_info():
    """Información de modelos (versión demo)"""
    return {
        "status": "demo_active",
        "models": {
            "sales_model": {
                "algorithm": "RandomForestRegressor",
                "accuracy": 0.92,
                "features": 15,
                "last_training": "2026-04-15",
                "status": "production_ready"
            },
            "staff_model": {
                "algorithm": "RandomForestRegressor", 
                "accuracy": 0.89,
                "features": 12,
                "last_training": "2026-04-15",
                "status": "production_ready"
            },
            "perishables_model": {
                "algorithm": "RandomForestRegressor",
                "accuracy": 0.86,
                "features": 18,
                "last_training": "2026-04-15",
                "status": "production_ready"
            }
        },
        "infrastructure": {
            "framework": "FastAPI + Uvicorn",
            "ml_stack": "Scikit-learn + Pandas",
            "database": "PostgreSQL 16",
            "cache": "Redis (producción)",
            "monitoring": "Prometheus + Grafana"
        },
        "note": "Modelos reales y lógica completa protegidos por propiedad intelectual"
    }

# ── Funciones auxiliares ───────────────────────────────────────────────────────
def get_recommendation(scenario: str) -> str:
    """Genera recomendación según escenario"""
    recommendations = {
        "quiet": "Considera promociones para incrementar tráfico",
        "normal": "Operación estándar - monitorear tendencias", 
        "busy": "Preparar personal extra y stock adicional"
    }
    return recommendations.get(scenario, "Revisar predicciones")

# ── Ejecutar servidor ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Puerto para Railway.app (usa variable de entorno PORT)
    port = int(os.getenv("PORT", 8001))
    
    print("🚀 Iniciando MIDAS Demo API...")
    print("📋 Endpoints disponibles:")
    print(f"   • API principal: http://localhost:{port}/") 
    print(f"   • Documentación: http://localhost:{port}/docs")
    print(f"   • Health check:  http://localhost:{port}/health")
    print(f"   • Predicciones:  http://localhost:{port}/predict/full")
    print(f"   • Modelos:       http://localhost:{port}/models")
    print(f"\n💡 Tip: Abre http://localhost:{port}/docs para probar interactivamente")
    print("\n🎯 Para presentación: Esta API funciona completamente con mocks realistas")
    print(f"🌍 Ejecutando en puerto: {port}")
    
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")