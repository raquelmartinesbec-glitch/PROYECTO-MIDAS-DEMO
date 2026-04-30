# ══════════════════════════════════════════════════════════════════════════════
# test_dashboard.py - Tests para MIDAS Dashboard
# Tests completos para funcionalidad del dashboard
# ══════════════════════════════════════════════════════════════════════════════

import pytest
import pandas as pd
from datetime import date, datetime
import sys
import os

# Agregar el directorio src al path para importar el módulo
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'dashboard'))

# Importar funciones del dashboard
try:
    from dashboard.app import calculate_prediction, get_sample_predictions
except ImportError:
    # Fallback si el import no funciona
    print("Warning: No se pudo importar desde dashboard.app")


class TestPredictions:
    """Tests para algoritmos de predicción"""
    
    def test_calculate_prediction_sales(self):
        """Test predicción de ventas con parámetros válidos"""
        result = calculate_prediction(
            prediction_type="sales",
            date_obj=date(2026, 4, 30),
            weather="sol",
            reservations=20,
            has_event=False,
            event_people=0,
            event_price=0.0
        )
        
        assert result is not None
        assert "value" in result
        assert "confidence" in result
        assert isinstance(result["value"], (int, float))
        assert 0.0 <= result["confidence"] <= 1.0
        assert result["value"] > 0  # Las ventas deben ser positivas
        
    def test_calculate_prediction_staff(self):
        """Test predicción de personal con parámetros válidos"""
        result = calculate_prediction(
            prediction_type="staff",
            date_obj=date(2026, 4, 30),
            weather="nublado",
            reservations=15,
            has_event=True,
            event_people=50,
            event_price=25.0
        )
        
        assert result is not None
        assert "value" in result
        assert "confidence" in result
        assert isinstance(result["value"], (int, float))
        assert result["value"] >= 1  # Mínimo 1 persona de staff
        
    def test_calculate_prediction_perishables(self):
        """Test predicción de perecederos con parámetros válidos"""
        result = calculate_prediction(
            prediction_type="perishables",
            date_obj=date(2026, 4, 30),
            weather="lluvia",
            reservations=10,
            has_event=False,
            event_people=0,
            event_price=0.0
        )
        
        assert result is not None
        assert "value" in result
        assert "confidence" in result
        assert result["value"] > 0  # Los perecederos deben tener costo positivo

    def test_weather_factor_impact(self):
        """Test que diferentes climas afecten las predicciones"""
        base_params = {
            "prediction_type": "sales",
            "date_obj": date(2026, 4, 30),
            "reservations": 15,
            "has_event": False,
            "event_people": 0,
            "event_price": 0.0
        }
        
        # Predicción con sol (factor positivo)
        sunny_result = calculate_prediction(weather="sol", **base_params)
        
        # Predicción con lluvia (factor negativo)
        rainy_result = calculate_prediction(weather="lluvia", **base_params)
        
        # El sol debería generar más ventas que la lluvia
        if sunny_result and rainy_result:
            assert sunny_result["value"] > rainy_result["value"]
    
    def test_event_impact(self):
        """Test que los eventos incrementen las predicciones"""
        base_params = {
            "prediction_type": "sales",
            "date_obj": date(2026, 4, 30),
            "weather": "sol",
            "reservations": 15
        }
        
        # Sin evento
        no_event_result = calculate_prediction(
            has_event=False, event_people=0, event_price=0.0, **base_params
        )
        
        # Con evento
        event_result = calculate_prediction(
            has_event=True, event_people=50, event_price=30.0, **base_params
        )
        
        # Los eventos deberían incrementar las ventas
        if no_event_result and event_result:
            assert event_result["value"] > no_event_result["value"]

    def test_invalid_prediction_type(self):
        """Test manejo de tipos de predicción inválidos"""
        result = calculate_prediction(
            prediction_type="invalid_type",
            date_obj=date(2026, 4, 30),
            weather="sol",
            reservations=15,
            has_event=False,
            event_people=0,
            event_price=0.0
        )
        
        # Debería retornar None para tipo inválido
        assert result is None


class TestSampleData:
    """Tests para generación de datos de ejemplo"""
    
    def test_get_sample_predictions(self):
        """Test generación de datos de muestra"""
        sample_data = get_sample_predictions()
        
        assert isinstance(sample_data, pd.DataFrame)
        assert not sample_data.empty
        
        # Verificar columnas esperadas
        expected_columns = ['date', 'sales', 'staff', 'perishables', 'weather', 'reservations', 'has_event']
        for col in expected_columns:
            assert col in sample_data.columns
            
        # Verificar tipos de datos
        assert pd.api.types.is_datetime64_any_dtype(sample_data['date'])
        assert pd.api.types.is_numeric_dtype(sample_data['sales'])
        assert pd.api.types.is_numeric_dtype(sample_data['staff'])
        assert pd.api.types.is_numeric_dtype(sample_data['perishables'])


class TestEdgeCases:
    """Tests para casos límite y validaciones"""
    
    def test_zero_reservations(self):
        """Test con cero reservas"""
        result = calculate_prediction(
            prediction_type="sales",
            date_obj=date(2026, 4, 30),
            weather="sol",
            reservations=0,
            has_event=False,
            event_people=0,
            event_price=0.0
        )
        
        assert result is not None
        assert result["value"] > 0  # Aún debe haber ventas base
        
    def test_maximum_reservations(self):
        """Test con máximo número de reservas"""
        result = calculate_prediction(
            prediction_type="sales",
            date_obj=date(2026, 4, 30),
            weather="sol",
            reservations=100,
            has_event=False,
            event_people=0,
            event_price=0.0
        )
        
        assert result is not None
        assert result["value"] > 0
        
    def test_weekend_vs_weekday(self):
        """Test diferencias entre fin de semana y días laborables"""
        # Lunes (día laborable)
        weekday_result = calculate_prediction(
            prediction_type="sales",
            date_obj=date(2026, 5, 4),  # Lunes
            weather="sol",
            reservations=15,
            has_event=False,
            event_people=0,
            event_price=0.0
        )
        
        # Sábado (fin de semana)
        weekend_result = calculate_prediction(
            prediction_type="sales",
            date_obj=date(2026, 5, 2),  # Sábado
            weather="sol",
            reservations=15,
            has_event=False,
            event_people=0,
            event_price=0.0
        )
        
        # Los fines de semana suelen tener más ventas
        if weekday_result and weekend_result:
            assert weekend_result["value"] >= weekday_result["value"]


if __name__ == "__main__":
    # Ejecutar tests básicos si se ejecuta directamente
    print("🧪 Ejecutando tests básicos del dashboard MIDAS...")
    
    # Test básico de importación
    try:
        from dashboard.app import calculate_prediction
        print("✅ Importación exitosa de funciones del dashboard")
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        
    # Test básico de predicción
    try:
        result = calculate_prediction(
            prediction_type="sales",
            date_obj=date.today(),
            weather="sol",
            reservations=15,
            has_event=False,
            event_people=0,
            event_price=0.0
        )
        if result:
            print(f"✅ Test básico exitoso: Ventas estimadas {result['value']:.0f}€")
        else:
            print("❌ Test básico falló: No se obtuvo resultado")
    except Exception as e:
        print(f"❌ Error en test básico: {e}")
        
    print("🎯 Tests completados. Ejecuta 'pytest tests/' para tests completos.")