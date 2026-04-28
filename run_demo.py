#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════════════════
# run_demo.py — Script para arrancar API + Dashboard de MIDAS
#
# USO: python run_demo.py
# 
# Este script arranca automáticamente:
# - API en puerto 8001
# - Dashboard en puerto 8501
# ══════════════════════════════════════════════════════════════════════════════

import subprocess
import sys
import time
import os
import webbrowser
from threading import Thread

def run_api():
    """Ejecuta la API en background"""
    print("🚀 Iniciando API MIDAS en puerto 8001...")
    try:
        subprocess.run([sys.executable, "simple_demo_api.py"], cwd=os.path.dirname(__file__))
    except KeyboardInterrupt:
        print("🛑 API detenida")

def run_dashboard():
    """Ejecuta el dashboard Streamlit"""
    print("📊 Iniciando Dashboard MIDAS en puerto 8501...")
    time.sleep(3)  # Esperar a que la API arranque
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "midas_dashboard.py", 
                       "--server.port=8501", "--server.headless=false"], 
                      cwd=os.path.dirname(__file__))
    except KeyboardInterrupt:
        print("🛑 Dashboard detenido")

def check_dependencies():
    """Verifica que las dependencias estén instaladas"""
    required_packages = ['streamlit', 'plotly', 'pandas', 'requests']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Faltan dependencias:")
        for package in missing_packages:
            print(f"   • {package}")
        print("\n📦 Instala las dependencias:")
        print("   pip install -r requirements-dashboard.txt")
        return False
    
    return True

def main():
    print("🍽️ MIDAS Demo - Iniciando Sistema Completo")
    print("=" * 50)
    
    # Verificar dependencias
    if not check_dependencies():
        return
    
    print("✅ Dependencias verificadas")
    print("\n🔄 Arrancando servicios...")
    
    try:
        # Arrancar API en thread separado
        api_thread = Thread(target=run_api, daemon=True)
        api_thread.start()
        
        print("⏳ Esperando que la API arranque...")
        time.sleep(5)
        
        # Abrir navegador automáticamente
        print("🌐 Abriendo navegador...")
        webbrowser.open("http://localhost:8501")
        
        # Arrancar dashboard (blocking)
        run_dashboard()
        
    except KeyboardInterrupt:
        print("\n🛑 Deteniendo sistema...")
        print("✅ Sistema detenido correctamente")

if __name__ == "__main__":
    main()