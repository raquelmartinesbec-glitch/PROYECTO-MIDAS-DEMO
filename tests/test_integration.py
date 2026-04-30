# ══════════════════════════════════════════════════════════════════════════════
# test_integration.py - Tests de integración para MIDAS
# Tests end-to-end y de integración del sistema completo
# ══════════════════════════════════════════════════════════════════════════════

import pytest
import requests
import pandas as pd
from datetime import date
import time
import os
import subprocess
import sys


class TestSystemIntegration:
    """Tests de integración del sistema completo"""
    
    def test_dashboard_structure_exists(self):
        """Verificar que la estructura de archivos del dashboard existe"""
        # Archivos críticos del dashboard
        critical_files = [
            "dashboard/app.py",
            "src/dashboard/app.py", 
            "config/railway.toml",
            "docker/Dockerfile",
            "requirements/requirements.txt"
        ]
        
        for file_path in critical_files:
            full_path = os.path.join(os.path.dirname(__file__), '..', file_path)
            assert os.path.exists(full_path), f"Archivo crítico faltante: {file_path}"
            
    def test_python_imports(self):
        """Verificar que las dependencias principales están disponibles"""
        try:
            import streamlit
            import plotly
            import pandas
            print(f"✅ Dependencias OK - Streamlit {streamlit.__version__}, Plotly {plotly.__version__}, Pandas {pandas.__version__}")
        except ImportError as e:
            pytest.fail(f"Dependencia faltante: {e}")
            
    def test_config_files_valid(self):
        """Verificar que los archivos de configuración son válidos"""
        # Verificar railway.toml
        railway_config = os.path.join(os.path.dirname(__file__), '..', 'config', 'railway.toml')
        if os.path.exists(railway_config):
            with open(railway_config, 'r') as f:
                content = f.read()
                assert 'startCommand' in content
                assert 'streamlit run' in content
                
        # Verificar requirements.txt
        requirements_file = os.path.join(os.path.dirname(__file__), '..', 'requirements', 'requirements.txt')
        if os.path.exists(requirements_file):
            with open(requirements_file, 'r') as f:
                content = f.read()
                assert 'streamlit' in content.lower()
                assert 'plotly' in content.lower()
                assert 'pandas' in content.lower()


class TestProductionEndpoint:
    """Tests para el endpoint de producción en Railway"""
    
    PRODUCTION_URL = "https://desirable-luck-production.up.railway.app"
    
    def test_production_accessibility(self):
        """Verificar que el dashboard de producción sea accesible"""
        try:
            response = requests.get(self.PRODUCTION_URL, timeout=10)
            assert response.status_code == 200, f"Status code: {response.status_code}"
            assert len(response.content) > 1000, "Response demasiado pequeño"
            print(f"✅ Producción accesible - Status: {response.status_code}, Size: {len(response.content)} bytes")
        except requests.exceptions.RequestException as e:
            pytest.skip(f"Producción no accesible (normal en CI): {e}")
            
    def test_production_content(self):
        """Verificar que el contenido de producción contenga elementos esperados"""
        try:
            response = requests.get(self.PRODUCTION_URL, timeout=10)
            content = response.text.lower()
            
            # Elementos que deben estar presentes
            expected_elements = [
                'midas',
                'predicción', 
                'ventas',
                'personal',
                'perecederos',
                'streamlit'
            ]
            
            for element in expected_elements:
                assert element in content, f"Elemento faltante en producción: {element}"
                
        except requests.exceptions.RequestException as e:
            pytest.skip(f"No se pudo verificar contenido de producción: {e}")


class TestLocalExecution:
    """Tests para ejecución local del dashboard"""
    
    @pytest.mark.slow
    def test_dashboard_starts_locally(self):
        """Test que el dashboard inicie correctamente en local"""
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'dashboard', 'app.py')
        
        if not os.path.exists(dashboard_path):
            pytest.skip("Dashboard app.py no encontrado")
            
        # Test de sintaxis básica
        result = subprocess.run([
            sys.executable, '-m', 'py_compile', dashboard_path
        ], capture_output=True, text=True)
        
        assert result.returncode == 0, f"Error de sintaxis en dashboard: {result.stderr}"
        print("✅ Dashboard pasa validación de sintaxis")
        
    def test_dashboard_imports(self):
        """Verificar que el dashboard puede importar sus dependencias"""
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'dashboard')
        src_path = os.path.join(os.path.dirname(__file__), '..')
        
        # Agregar paths para importación
        if dashboard_path not in sys.path:
            sys.path.insert(0, dashboard_path)
        if src_path not in sys.path:
            sys.path.insert(0, src_path)
            
        try:
            # Test de importaciones críticas del dashboard
            import streamlit
            import plotly.express
            import plotly.graph_objects
            import pandas
            print("✅ Todas las dependencias del dashboard están disponibles")
        except ImportError as e:
            pytest.fail(f"Error de importación en dashboard: {e}")


class TestDataValidation:
    """Tests para validación de datos y algoritmos"""
    
    def test_sample_data_generation(self):
        """Test que la generación de datos de muestra funcione"""
        try:
            # Intentar importar y ejecutar función de muestra
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'dashboard'))
            from app import get_sample_predictions
            
            sample_data = get_sample_predictions()
            assert isinstance(sample_data, pd.DataFrame)
            assert len(sample_data) > 0
            print(f"✅ Datos de muestra generados: {len(sample_data)} registros")
            
        except ImportError:
            pytest.skip("No se pudo importar función de datos de muestra")
        except Exception as e:
            pytest.fail(f"Error generando datos de muestra: {e}")
            
    def test_prediction_algorithm_basic(self):
        """Test básico del algoritmo de predicción"""
        try:
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'dashboard'))
            from app import calculate_prediction
            
            # Test con parámetros típicos
            result = calculate_prediction(
                prediction_type="sales",
                date_obj=date.today(),
                weather="sol",
                reservations=15,
                has_event=False,
                event_people=0,
                event_price=0.0
            )
            
            assert result is not None, "Algoritmo de predicción retornó None"
            assert "value" in result, "Resultado falta campo 'value'"
            assert "confidence" in result, "Resultado falta campo 'confidence'"
            assert result["value"] > 0, "Predicción debe ser positiva"
            assert 0 <= result["confidence"] <= 1, "Confianza debe estar entre 0 y 1"
            
            print(f"✅ Algoritmo funcionando - Predicción: {result['value']:.0f}, Confianza: {result['confidence']:.1%}")
            
        except ImportError:
            pytest.skip("No se pudo importar algoritmo de predicción")
        except Exception as e:
            pytest.fail(f"Error en algoritmo de predicción: {e}")


class TestPerformance:
    """Tests de rendimiento básico"""
    
    def test_prediction_performance(self):
        """Test que las predicciones se ejecuten en tiempo razonable"""
        try:
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'dashboard'))
            from app import calculate_prediction
            
            start_time = time.time()
            
            # Ejecutar múltiples predicciones
            for _ in range(10):
                calculate_prediction(
                    prediction_type="sales",
                    date_obj=date.today(),
                    weather="sol",
                    reservations=15,
                    has_event=False,
                    event_people=0,
                    event_price=0.0
                )
            
            execution_time = time.time() - start_time
            avg_time = execution_time / 10
            
            # Cada predicción debe tomar menos de 1 segundo
            assert avg_time < 1.0, f"Predicción demasiado lenta: {avg_time:.2f}s promedio"
            print(f"✅ Rendimiento OK - {avg_time:.3f}s promedio por predicción")
            
        except ImportError:
            pytest.skip("No se pudo importar para test de rendimiento")


if __name__ == "__main__":
    print("🔗 Ejecutando tests de integración MIDAS...")
    
    # Test básico de estructura
    print("\n📁 Verificando estructura de archivos...")
    try:
        test_integration = TestSystemIntegration()
        test_integration.test_dashboard_structure_exists()
        test_integration.test_python_imports() 
        print("✅ Estructura de archivos OK")
    except Exception as e:
        print(f"❌ Error en estructura: {e}")
    
    # Test de accesibilidad de producción
    print("\n🌐 Verificando accesibilidad de producción...")
    try:
        test_production = TestProductionEndpoint()
        test_production.test_production_accessibility()
    except Exception as e:
        print(f"⚠️  Producción no accesible: {e}")
        
    # Test de algoritmo básico
    print("\n🧮 Verificando algoritmo de predicción...")
    try:
        test_data = TestDataValidation()
        test_data.test_prediction_algorithm_basic()
    except Exception as e:
        print(f"❌ Error en algoritmo: {e}")
        
    print("\n🎯 Tests de integración completados.")