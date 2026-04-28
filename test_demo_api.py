#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════════════════
# test_demo_api.py — Script de prueba para verificar la API mock
#
# PROPÓSITO: Demostrar que todos los endpoints funcionan correctamente
#           con datos simulados realistas.
# ══════════════════════════════════════════════════════════════════════════════

import requests
import json
from datetime import date, datetime
from typing import Dict, Any

# Configuración
API_BASE_URL = "http://localhost:8000"

def test_health_check():
    """Probar endpoint de salud"""
    print("🔍 Probando health check...")
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check OK: {data}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error conectando: {e}")
        return False

def test_root_endpoint():
    """Probar endpoint principal"""
    print("\n🔍 Probando endpoint principal...")
    try:
        response = requests.get(f"{API_BASE_URL}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint OK:")
            print(f"   📋 {data['message']}")
            print(f"   🏷️  Version: {data['version']}")
            print(f"   🎭 Demo Mode: {data['demo_mode']}")
            return True
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_prediction_endpoint(endpoint: str, prediction_type: str):
    """Probar un endpoint de predicción específico"""
    print(f"\n🔍 Probando predicción de {prediction_type}...")
    
    # Datos de prueba simplificados
    test_data = {
        "target_date": "2026-04-28",
        "scenario": "normal"
    }
    
    try:
        response = requests.post(
            f"{API_BASE_URL}{endpoint}", 
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Predicción de {prediction_type} OK:")
            print(f"   📅 Fecha: {data['date']}")
            print(f"   📊 Valor predicho: {data['value']}")
            print(f"   🎯 Confianza: {data['confidence']:.0%}")
            print(f"   ⏰ Generado: {data['timestamp']}")
            return data
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_full_prediction():
    """Probar el endpoint de predicción completa"""
    print(f"\n🔍 Probando predicción COMPLETA (todos los tipos)...")
    
    test_data = {
        "target_date": "2026-04-29",
        "scenario": "busy"
    }
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/predict/full", 
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Predicción completa OK:")
            print(f"   📅 Fecha: {data['date']}")
            print(f"   🎭 Escenario: {data['scenario']}")
            print(f"\n   📊 RESULTADOS:")
            
            for pred_type, pred_data in data['predictions'].items():
                print(f"   🔸 {pred_type.upper()}: {pred_data['value']} "
                      f"(confianza: {pred_data['confidence']:.0%})")
            
            print(f"\n   🎯 Confianza total: {data['summary']['total_confidence']:.0%}")
            print(f"   🎭 Modo demo: {data['summary']['demo_mode']}")
            return True
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_models_info():
    """Probar endpoint de información de modelos"""
    print(f"\n🔍 Probando información de modelos...")
    
    try:
        response = requests.get(f"{API_BASE_URL}/models")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Información de modelos OK:")
            print(f"   📋 Estado: {data['status']}")
            
            if "models" in data:
                for model_name, model_info in data["models"].items():
                    print(f"   🤖 {model_name}:")
                    print(f"      📈 Precisión: {model_info['accuracy']:.0%}")
                    print(f"      🏷️  Tipo: {model_info['type']}")
                    print(f"      📅 Entrenado: {model_info['last_trained']}")
                    print(f"      🔢 Features: {model_info['features']}")
            
            if 'note' in data:
                print(f"\n   ⚠️  {data['note']}")
            return True
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🚀 INICIANDO PRUEBAS DE LA API MIDAS DEMO")
    print("=" * 60)
    
    # Contador de pruebas exitosas
    successful_tests = 0
    total_tests = 0
    
    # Test 1: Health Check
    total_tests += 1
    if test_health_check():
        successful_tests += 1
    
    # Test 2: Root Endpoint
    total_tests += 1
    if test_root_endpoint():
        successful_tests += 1
    
    # Test 3: Predicción de ventas
    total_tests += 1
    if test_prediction_endpoint("/predict/sales", "ventas"):
        successful_tests += 1
    
    # Test 4: Predicción de personal
    total_tests += 1
    if test_prediction_endpoint("/predict/staff", "personal"):
        successful_tests += 1
    
    # Test 5: Predicción de perecederos
    total_tests += 1
    if test_prediction_endpoint("/predict/perishables", "perecederos"):
        successful_tests += 1
    
    # Test 6: Predicción completa
    total_tests += 1
    if test_full_prediction():
        successful_tests += 1
    
    # Test 7: Información de modelos
    total_tests += 1
    if test_models_info():
        successful_tests += 1
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"✅ Pruebas exitosas: {successful_tests}/{total_tests}")
    print(f"📈 Tasa de éxito: {(successful_tests/total_tests*100):.1f}%")
    
    if successful_tests == total_tests:
        print("🎉 ¡TODAS LAS PRUEBAS PASARON! La API mock funciona perfectamente.")
        print("🚀 Lista para presentación profesional.")
    else:
        print("⚠️  Algunas pruebas fallaron. Revisar configuración.")
    
    print("\n📋 URLs para la demostración:")
    print(f"   🔗 API Docs (Swagger): {API_BASE_URL}/docs")
    print(f"   🔗 API Redoc:         {API_BASE_URL}/redoc")
    print(f"   🔗 Health Check:      {API_BASE_URL}/health")

if __name__ == "__main__":
    main()