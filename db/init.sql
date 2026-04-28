-- ══════════════════════════════════════════════════════════════════════════════
-- demo_init.sql — Inicialización básica de base de datos para demostración
--
-- PROPÓSITO: Crear estructura de tablas básica que muestra la arquitectura
--           de datos sin exponer el esquema completo de producción.
--
-- NOTA: La base de datos real incluye tablas adicionales, índices optimizados,
--       triggers, vistas materializadas y procedimientos almacenados no
--       mostrados en esta demostración.
-- ══════════════════════════════════════════════════════════════════════════════

-- ── Información de la demo ─────────────────────────────────────────────────────
\echo 'Inicializando base de datos de demostración para Proyecto MIDAS...'

-- ── Tabla de ejemplo: Predicciones (estructura simplificada) ──────────────────
CREATE TABLE IF NOT EXISTS demo_predictions (
    id                SERIAL PRIMARY KEY,
    prediction_date   DATE NOT NULL,
    prediction_type   VARCHAR(20) NOT NULL CHECK (prediction_type IN ('sales', 'staff', 'perishables')),
    predicted_value   NUMERIC(10,2),
    confidence_score  NUMERIC(3,2) CHECK (confidence_score BETWEEN 0 AND 1),
    created_at        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    UNIQUE(prediction_date, prediction_type)
);

-- ── Tabla de ejemplo: Métricas del sistema ─────────────────────────────────────
CREATE TABLE IF NOT EXISTS demo_system_metrics (
    id              SERIAL PRIMARY KEY,
    metric_name     VARCHAR(50) NOT NULL,
    metric_value    NUMERIC(12,2),
    metric_date     DATE NOT NULL,
    created_at      TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ── Datos de ejemplo para demostración ─────────────────────────────────────────
INSERT INTO demo_predictions (prediction_date, prediction_type, predicted_value, confidence_score) VALUES
    (CURRENT_DATE, 'sales', 2500.00, 0.85),
    (CURRENT_DATE, 'staff', 8.0, 0.78),
    (CURRENT_DATE, 'perishables', 450.00, 0.82),
    (CURRENT_DATE + INTERVAL '1 day', 'sales', 2800.00, 0.83),
    (CURRENT_DATE + INTERVAL '1 day', 'staff', 9.0, 0.76),
    (CURRENT_DATE + INTERVAL '1 day', 'perishables', 520.00, 0.80);

INSERT INTO demo_system_metrics (metric_name, metric_value, metric_date) VALUES
    ('accuracy_sales', 0.92, CURRENT_DATE),
    ('accuracy_staff', 0.89, CURRENT_DATE),
    ('accuracy_perishables', 0.86, CURRENT_DATE),
    ('total_predictions', 1247, CURRENT_DATE),
    ('api_uptime_percent', 99.8, CURRENT_DATE);

-- ── Índices para optimización de consultas ─────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_predictions_date_type 
    ON demo_predictions(prediction_date, prediction_type);

CREATE INDEX IF NOT EXISTS idx_metrics_date 
    ON demo_system_metrics(metric_date);

-- ── Permisos básicos para usuario demo ─────────────────────────────────────────
-- GRANT SELECT, INSERT ON demo_predictions TO demo_user;
-- GRANT SELECT, INSERT ON demo_system_metrics TO demo_user;

\echo 'Base de datos de demostración inicializada correctamente.'
\echo 'Estructura básica creada para mostrar arquitectura del sistema.'
\echo ''
\echo 'NOTA: La base de datos de producción incluye:'
\echo '• Esquemas complejos con más de 15 tablas'
\echo '• Vistas materializadas para análisis de tendencias'
\echo '• Triggers para auditoría y validación automática'
\echo '• Particionado por fechas para optimización'
\echo '• Índices compuestos y funcionales'
\echo '• Procedimientos almacenados para cálculos complejos'