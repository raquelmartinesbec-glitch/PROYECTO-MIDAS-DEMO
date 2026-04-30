# ── run_local.py - Script para ejecutar dashboard localmente ───────
"""
Script para facilitar la ejecución local del dashboard MIDAS
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    print("🎯 MIDAS Dashboard - Ejecución Local")
    print("=" * 50)
    
    # Verificar que estamos en el directorio correcto  
    if not Path("src/dashboard/app.py").exists():
        print("❌ Error: Ejecutar desde la raíz del proyecto")
        sys.exit(1)
    
    # Verificar dependencias
    print("🔍 Verificando dependencias...")
    try:
        import streamlit
        import plotly
        import pandas
        print("✅ Dependencias verificadas")
    except ImportError as e:
        print(f"❌ Error: Dependencia faltante - {e}")
        print("💡 Ejecutar: pip install -r requirements/requirements.txt")
        sys.exit(1)
    
    # Cambiar al directorio del dashboard
    os.chdir("src/dashboard")
    
    # Ejecutar Streamlit
    print("🚀 Iniciando dashboard en http://localhost:8501")
    print("Press Ctrl+C para detener")
    
    try:
        subprocess.run([
            "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n✅ Dashboard detenido")
    except Exception as e:
        print(f"❌ Error al ejecutar dashboard: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()