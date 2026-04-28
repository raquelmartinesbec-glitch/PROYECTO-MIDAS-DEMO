#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════════════════
# test_simple_demo.py — Pruebas simples para la API demo 
#
# USO: python test_simple_demo.py
# REQUISITO: simple_demo_api.py debe estar corriendo en puerto 8001
# ══════════════════════════════════════════════════════════════════════════════

import requests
import json
import time

API_URL = "http://localhost:8001"

def test_endpoint(name: str, url: str, expected_status: int = 200) -> bool:
    """Probar un endpoint específico"""
    try:
        print(f"🔍 Probando {name}...")
        response = requests.get(url, timeout=5)
        
        if response.status_code == expected_status:
            data = response.json()
            print(f"✅ {name} OK")
            
            # Mostrar algunos datos clave
            if name == "Root":
                print(f"   📋 {data.get('name', 'N/A')}")
                print(f"   🏷️  Versión: {data.get('version', 'N/A')}")
                print(f"   🎭 Demo: {data.get('demo_mode', False)}")
                
            elif name == "Health":
                print(f"   📊 Estado: {data.get('status', 'N/A')}")
                if 'accuracy' in data:
                    for model, acc in data['accuracy'].items():
                        print(f"   🎯 {model}: {acc:.0%}")
                        
            elif "predict" in name.lower():
                print(f"   📅 Fecha: {data.get('date', 'N/A')}")
                print(f"   📊 Valor: {data.get('value', 'N/A')}")
                print(f"   🎯 Confianza: {data.get('confidence', 0):.0%}")
                
            elif name == "Modelos":
                print(f"   📊 Estado: {data.get('status', 'N/A')}")
                if 'models' in data:
                    for model_name, info in data['models'].items():
                        print(f"   🤖 {model_name}: {info.get('accuracy', 0):.0%}")
            
            return True
        else:
            print(f"❌ {name} falló: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ {name}: No se puede conectar (¿API corriendo en {API_URL}?)")
        return False
    except Exception as e:
        print(f"❌ {name}: Error {e}")
        return False

def test_prediction_full():
    """Probar predicción completa con escenarios"""
    print(f"\n🔍 Probando predicciones completas por escenario...")
    
    scenarios = ["quiet", "normal", "busy"]
    results = {}
    
    for scenario in scenarios:
        try:
            response = requests.get(f"{API_URL}/predict/full?scenario={scenario}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                results[scenario] = data
                print(f"✅ Escenario '{scenario}':")
                print(f"   💰 Ventas: €{data['predictions']['sales']['value']}")
                print(f"   👥 Personal: {data['predictions']['staff']['value']} personas")
                print(f"   🥬 Perecederos: €{data['predictions']['perishables']['value']}")
                print(f"   📈 Beneficio estimado: €{data['summary']['estimated_profit']}")
            else:
                print(f"❌ Escenario '{scenario}' falló: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error en escenario '{scenario}': {e}")
    
    return len(results) == len(scenarios)

def main():
    """Ejecutar todas las pruebas"""
    print("🚀 INICIANDO PRUEBAS DE MIDAS DEMO API")
    print("=" * 60)
    print(f"🔗 Probando API en: {API_URL}")
    print()
    
    # Lista de pruebas
    tests = [
        ("Root", f"{API_URL}/"),
        ("Health", f"{API_URL}/health"),
        ("Predicción Ventas", f"{API_URL}/predict/sales"),
        ("Predicción Personal", f"{API_URL}/predict/staff"),
        ("Predicción Perecederos", f"{API_URL}/predict/perishables"),
        ("Modelos", f"{API_URL}/models")
    ]
    
    passed = 0
    total = len(tests)
    
    # Ejecutar pruebas básicas
    for test_name, test_url in tests:
        if test_endpoint(test_name, test_url):
            passed += 1
        print()  # Línea vacía entre pruebas
        time.sleep(0.2)  # Pequeña pausa para no saturar
    
    # Prueba especial: predicciones completas
    print("🔍 Pruebas avanzadas:")
    if test_prediction_full():
        passed += 1
    total += 1
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"✅ Exitosas: {passed}/{total}")
    print(f"📈 Tasa éxito: {(passed/total*100):.1f}%")
    
    if passed == total:
        print("\n🎉 ¡PERFECTO! Todos los mocks funcionan correctamente")
        print("🚀 La API demo está lista para presentación profesional")
        print("\n📋 URLs para demostración en vivo:")
        print(f"   🌐 Documentación interactiva: {API_URL}/docs")
        print(f"   📊 Dashboard principal: {API_URL}/")
        print(f"   🔍 Health check: {API_URL}/health")
        print(f"   🎯 Predicción completa: {API_URL}/predict/full")
        print(f"   🤖 Info modelos: {API_URL}/models")
    else:
        print(f"\n⚠️  {total-passed} pruebas fallaron")
        print("🔧 Verificar que la API esté corriendo: python simple_demo_api.py")

if __name__ == "__main__":
    main()