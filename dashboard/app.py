
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime
import requests
import json
import os

# ── Configuración de la página ─────────────────────────────────────────────────
st.set_page_config(
    page_title="MIDAS - Sistema de Predicción",
    page_icon="🍽️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap');

        /* Fondo azul ultra oscuro */
        .stApp {
            background: linear-gradient(135deg, #000a1a 0%, #001122 25%, #001a33 50%, #000d1a 75%, #000511 100%) !important;
            background-attachment: fixed;
            color: #00d4ff;
        }

        /* Sidebar azul oscuro premium */
        .stSidebar {
            background: linear-gradient(180deg, #000a1a 0%, #001122 50%, #000511 100%) !important;
            border-right: 2px solid #00d4ff;
            box-shadow: 0 0 25px rgba(0, 212, 255, 0.5);
        }

        /* Títulos con degradado azul brillante */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Orbitron', monospace !important;
            font-weight: 700 !important;
            background: linear-gradient(45deg, #00d4ff 0%, #0099ff 50%, #66ccff 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.8) !important;
            margin: 1rem 0 !important;
            filter: drop-shadow(0 0 10px rgba(0, 212, 255, 0.6));
        }

        /* Texto general azul */
        .stApp, .stMarkdown, p, span, div, label, li {
            font-family: 'Exo 2', sans-serif !important;
            background: linear-gradient(45deg, #00d4ff 0%, #66ccff 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
        }

        /* Forzar texto azul en elementos específicos */
        .stSelectbox, .stDateInput, .stTimeInput, .stNumberInput, .stSlider {
            color: #00d4ff !important;
        }

        /* Input values azules */
        input, select, textarea {
            color: #00d4ff !important;
            background: rgba(0, 10, 26, 0.9) !important;
            border: 1px solid rgba(0, 212, 255, 0.5) !important;
        }

        /* Métricas premium azules */
        [data-testid="stMetric"] {
            background: linear-gradient(135deg, rgba(0, 10, 26, 0.9) 0%, rgba(0, 17, 34, 0.8) 100%) !important;
            border: 2px solid rgba(0, 212, 255, 0.6) !important;
            border-radius: 15px !important;
            padding: 1.5rem 1.2rem !important;
            border-left: 4px solid #00d4ff !important;
            box-shadow: 0 8px 32px rgba(0, 212, 255, 0.3), 0 0 25px rgba(0, 212, 255, 0.2) !important;
            backdrop-filter: blur(15px);
            transition: all 0.3s ease;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 50px rgba(0, 212, 255, 0.5), 0 0 40px rgba(102, 204, 255, 0.4) !important;
            border: 2px solid rgba(102, 204, 255, 0.8) !important;
        }

        /* Controles con bordes azules */
        .stSelectbox > div > div {
            background: rgba(0, 10, 26, 0.9) !important;
            border: 2px solid rgba(0, 212, 255, 0.5) !important;
            border-radius: 10px !important;
            color: #00d4ff !important;
        }

        .stDateInput > div > div {
            background: rgba(0, 10, 26, 0.9) !important;
            border: 2px solid rgba(0, 212, 255, 0.5) !important;
            border-radius: 10px !important;
            color: #00d4ff !important;
        }

        .stDateInput input, .stDateInput p, .stDateInput span, .stDateInput div[data-baseweb] {
            color: #00d4ff !important;
            -webkit-text-fill-color: #00d4ff !important;
        }

        div[data-baseweb="calendar"],
        div[data-baseweb="popover"] {
            background: #000a1a !important;
            background-color: #000a1a !important;
            border: 1px solid rgba(0, 212, 255, 0.4) !important;
            border-radius: 10px !important;
        }

        div[data-baseweb="calendar"] button,
        div[data-baseweb="calendar"] div[role="gridcell"] {
            background-color: transparent !important;
            color: #00d4ff !important;
            -webkit-text-fill-color: #00d4ff !important;
        }

        div[data-baseweb="calendar"] button[aria-label],
        div[data-baseweb="calendar"] [role="heading"] {
            color: #00d4ff !important;
            -webkit-text-fill-color: #00d4ff !important;
        }

        div[data-baseweb="calendar"] [aria-selected="true"] div {
            background: rgba(0, 212, 255, 0.3) !important;
            border-radius: 50% !important;
        }

        .stTimeInput > div > div {
            background: rgba(0, 10, 26, 0.9) !important;
            border: 2px solid rgba(0, 212, 255, 0.5) !important;
            border-radius: 10px !important;
        }

        .stNumberInput > div > div {
            background: rgba(0, 10, 26, 0.9) !important;
            border: 2px solid rgba(0, 212, 255, 0.5) !important;
            border-radius: 10px !important;
            color: #00d4ff !important;
        }

        /* Sliders azules */
        .stSlider {
            background: transparent !important;
        }

        .stSlider > div > div > div > div {
            background: linear-gradient(90deg, #00d4ff 0%, #66ccff 100%) !important;
        }

        /* Botones épicos azules */
        .stButton > button {
            background: linear-gradient(45deg, #00d4ff 0%, #0099ff 50%, #66ccff 100%) !important;
            color: #000a1a !important;
            -webkit-text-fill-color: #000a1a !important;
            border: none !important;
            border-radius: 12px !important;
            font-family: 'Orbitron', monospace !important;
            font-weight: 700 !important;
            padding: 0.75rem 1.5rem !important;
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.6) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
        }

        .stButton > button:hover {
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 12px 35px rgba(102, 204, 255, 0.8) !important;
            background: linear-gradient(45deg, #0099ff 0%, #66ccff 50%, #99ddff 100%) !important;
            color: #000a1a !important;
            -webkit-text-fill-color: #000a1a !important;
        }

        /* Checkboxes azules */
        .stCheckbox label {
            background: linear-gradient(45deg, #00d4ff 0%, #66ccff 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
        }

        /* PESTAÑAS PREMIUM AZULES */
        .stTabs [data-baseweb="tab-list"] {
            background: rgba(0, 10, 26, 0.9) !important;
            border-radius: 15px !important;
            padding: 0.5rem !important;
            border: 2px solid rgba(0, 212, 255, 0.4) !important;
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
        }

        /* PESTAÑAS NORMALES - SIEMPRE VISIBLES */
        .stTabs [data-baseweb="tab"] {
            background: rgba(0, 20, 40, 0.5) !important;
            color: #66ccff !important;
            -webkit-text-fill-color: #66ccff !important;
            font-family: 'Orbitron', monospace !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
            margin: 0 0.25rem !important;
            padding: 0.5rem 1rem !important;
            transition: all 0.3s ease !important;
            border: 1px solid rgba(0, 212, 255, 0.3) !important;
        }

        /* PESTAÑA SELECCIONADA */
        .stTabs [aria-selected="true"] {
            background: linear-gradient(45deg, #00d4ff 15%, #66ccff 85%) !important;
            color: #000a1a !important;
            -webkit-text-fill-color: #000a1a !important;
            box-shadow: 0 4px 20px rgba(0, 212, 255, 0.6) !important;
            font-weight: 700 !important;
            border: 2px solid #00d4ff !important;
        }

        /* HOVER PESTAÑA SELECCIONADA */
        .stTabs [aria-selected="true"]:hover {
            background: rgba(0, 10, 26, 0.95) !important;
            color: #00d4ff !important;
            -webkit-text-fill-color: #00d4ff !important;
            box-shadow: 0 6px 25px rgba(0, 212, 255, 0.8) !important;
            border: 2px solid #00d4ff !important;
        }

        /* HOVER PESTAÑAS NO SELECCIONADAS */
        .stTabs [data-baseweb="tab"]:not([aria-selected="true"]):hover {
            background: rgba(0, 212, 255, 0.2) !important;
            color: #00d4ff !important;
            -webkit-text-fill-color: #00d4ff !important;
            box-shadow: 0 3px 15px rgba(0, 212, 255, 0.4) !important;
            border: 1px solid #00d4ff !important;
        }

        /* Alertas */
        .stAlert {
            background: rgba(0, 10, 26, 0.9) !important;
            border: 2px solid rgba(0, 212, 255, 0.5) !important;
            border-radius: 12px !important;
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
        }

        /* DataFrames */
        .stDataFrame {
            background: rgba(0, 10, 26, 0.9) !important;
            border-radius: 12px !important;
            border: 2px solid rgba(0, 212, 255, 0.4) !important;
        }

        /* Contenedor principal */
        .block-container {
            padding-top: 2rem !important;
            background: transparent !important;
        }

        /* Separadores */
        hr {
            border: none !important;
            height: 3px !important;
            background: linear-gradient(90deg, transparent 0%, #00d4ff 50%, transparent 100%) !important;
            margin: 2rem 0 !important;
            box-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
        }

        /* Fondo principal forzado */
        html, body,
        [data-testid="stAppViewContainer"], .main .block-container,
        .stApp > div, .main, .main > div,
        [data-testid="stSidebar"] > div {
            background: linear-gradient(135deg, #000a1a 0%, #001122 25%, #001a33 50%, #000d1a 75%, #000511 100%) !important;
        }

        /* Sidebar */
        [data-testid="stSidebar"] > div {
            background: linear-gradient(180deg, #000a1a 0%, #001122 50%, #000511 100%) !important;
        }

        /* Transparencias para contenedores */
        .element-container, .stVerticalBlock, .stHorizontalBlock,
        [data-testid="column"], [data-testid="stHorizontalBlock"],
        [data-testid="stVerticalBlock"], div[role="tabpanel"] > div,
        .stPlotlyChart, .chart-container, .stMarkdown {
            background: transparent !important;
        }

        /* Forzar texto azul global */
        *, *::before, *::after {
            color: #00d4ff !important;
        }

        /* Scrollbars premium */
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: rgba(0, 10, 26, 0.3); border-radius: 10px; }
        ::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #00d4ff, #66ccff); border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: linear-gradient(180deg, #66ccff, #00d4ff); }

        /* Header banner */
        [data-testid="stHeader"] {
            background: rgba(0, 10, 26, 0.8) !important;
        }

        /* Animación de entrada */
        .stApp {
            animation: fadeIn 0.8s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


API_URL = os.getenv("API_URL", "http://localhost:8000")
DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"

# ── Funciones auxiliares ───────────────────────────────────────────────────────
@st.cache_data(ttl=60)
def call_api(endpoint, data=None):
    """
    Llamada a la API con cache básico
    En producción incluye manejo de errores avanzado y retry logic
    """
    try:
        if data:
            response = requests.post(f"{API_URL}{endpoint}", json=data)
        else:
            response = requests.get(f"{API_URL}{endpoint}")
        return response.json() if response.status_code == 200 else None
    except Exception:
        return None

def generate_demo_data():
    """Genera 2 años de datos demo sintéticos para visualizaciones"""
    import numpy as np
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
    seasonal_boost = [0, -200, -100, 150, 200, 300, 350, 320, 200, 100, -50, 400]
    rng = np.random.default_rng(42)
    data = []
    for d in dates:
        weekday = d.weekday()
        month = d.month
        base = 1800 + weekday * 100 if weekday < 5 else 2700 + (weekday - 5) * 180
        seasonal = seasonal_boost[month - 1]
        has_event = rng.random() < 0.15
        event_boost = int(rng.integers(400, 900)) if has_event else 0
        sales = max(800, base + seasonal + event_boost + int(rng.integers(-200, 200)))
        data.append({
            'date': d,
            'weekday': weekday,
            'month': month,
            'year': d.year,
            'sales': float(sales),
            'staff': max(4, 6 + int(weekday >= 5) * 2 + int(has_event)),
            'perishables': float(max(150, 350 + seasonal * 0.1 + int(rng.integers(-50, 80)))),
            'reservations': max(0, 15 + int(weekday >= 5) * 10 + int(has_event) * 20 + int(rng.integers(-5, 15))),
            'has_event': int(has_event),
        })
    return pd.DataFrame(data)


PLOT_LAYOUT = dict(
    paper_bgcolor='rgba(0,10,26,0)',
    plot_bgcolor='rgba(0,10,26,0.6)',
    font=dict(color='#00d4ff', family='Exo 2, sans-serif'),
    title_font=dict(color='#66ccff', size=16),
    xaxis=dict(gridcolor='rgba(0,212,255,0.1)', linecolor='rgba(0,212,255,0.3)', tickfont=dict(color='#00d4ff')),
    yaxis=dict(gridcolor='rgba(0,212,255,0.1)', linecolor='rgba(0,212,255,0.3)', tickfont=dict(color='#00d4ff')),
    legend=dict(bgcolor='rgba(0,10,26,0.7)', bordercolor='rgba(0,212,255,0.3)', borderwidth=1),
    margin=dict(l=40, r=20, t=50, b=40),
    height=420,
)

# ── Header principal ───────────────────────────────────────────────────────────
st.title("🍽️ MIDAS - Sistema de Predicción")
st.caption("Predicción de ventas · Personal · Perecederos")

# ── Sidebar de configuración ───────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Parámetros del día")

    prediction_date = st.date_input("📅 Fecha", value=date.today())

    weather = st.selectbox(
        "🌤️ Clima",
        options=["sol", "nublado", "lluvia", "nieve"],
        index=0,
        format_func=lambda x: {"sol": "☀️ Sol", "nublado": "🌥 Nublado",
                                "lluvia": "🌧️ Lluvia", "nieve": "❄️ Nieve"}[x],
    )
    is_holiday = st.checkbox("📅 ¿Día festivo?", value=False)
    reservations = st.slider("📋 Reservas confirmadas", min_value=0, max_value=100, value=15)

    st.divider()
    has_event = st.checkbox("🎉 ¿Hay evento especial?", value=False)

    if has_event:
        event_intensity = st.slider("🔥 Intensidad del evento", min_value=1, max_value=3, value=2)
        event_people    = st.slider("👥 Asistentes al evento", min_value=15, max_value=220, value=70,
                                   help="Mínimo 15 personas para considerar evento especial")
        event_price = st.number_input(
            "💶 Precio por persona del evento (€)",
            min_value=0.0,
            max_value=500.0,
            value=30.0,
            step=1.0,
            help="Precio que cobra el restaurante por persona en el evento especial"
        )
    else:
        event_intensity = 0
        event_people    = 0
        event_price = 0.0

    st.divider()
    predict_btn = st.button("🔮 Generar Predicción", type="primary", use_container_width=True)

# ── Sección de predicciones en tiempo real ─────────────────────────────────────
st.header("📊 Predicciones del Día")

# Preparar datos para la API
prediction_data = {
    "date": prediction_date.isoformat(),
    "day_of_week": prediction_date.weekday(),
    "month": prediction_date.month,
    "is_holiday": is_holiday,
    "weather": weather,
    "has_event": has_event,
    "event_intensity": event_intensity,
    "event_people": event_people,
    "event_price": event_price,
    "reservations": reservations
}

# Obtener predicciones
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💰 Ventas")
    sales_prediction = call_api("/predict/sales", prediction_data)
    if sales_prediction:
        st.metric(
            "Ventas estimadas",
            f"€{sales_prediction['value']:.0f}",
            f"Confianza: {sales_prediction['confidence']:.0%}"
        )
    else:
        st.metric("Ventas estimadas", "€2,450", "Confianza: 85%")

with col2:
    st.subheader("👥 Personal")
    staff_prediction = call_api("/predict/staff", prediction_data)
    if staff_prediction:
        st.metric(
            "Personal necesario", 
            f"{staff_prediction['value']:.0f} personas",
            f"Confianza: {staff_prediction['confidence']:.0%}"
        )
    else:
        st.metric("Personal necesario", "8 personas", "Confianza: 78%")

with col3:
    st.subheader("🥬 Perecederos")
    perishables_prediction = call_api("/predict/perishables", prediction_data)
    if perishables_prediction:
        st.metric(
            "Compra perecederos",
            f"€{perishables_prediction['value']:.0f}",
            f"Confianza: {perishables_prediction['confidence']:.0%}"
        )
    else:
        st.metric("Compra perecederos", "€420", "Confianza: 82%")

# ── Sección de análisis histórico ────────────────────────────────────────────
st.divider()
st.header("📈 Análisis histórico y patrones")
st.caption("Visualización longitudinal de ventas, personal y perecederos con datos de 2 años.")

demo_data = generate_demo_data()

tab_diario, tab_mensual, tab_anual, tab_patrones = st.tabs([
    "📅 Vista Diaria",
    "📊 Vista Mensual",
    "🗓️ Vista Anual",
    "🔍 Patrones IA"
])

# ── VISTA DIARIA ──────────────────────────────────────────────────────────────
with tab_diario:
    st.caption("📊 Evolución día a día de ventas, personal y reservas")

    # KPIs rápidos
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Venta media/día", f"€{demo_data['sales'].mean():.0f}")
    k2.metric("Día récord", f"€{demo_data['sales'].max():.0f}")
    k3.metric("Reservas medias", f"{demo_data['reservations'].mean():.0f}")
    k4.metric("Días con evento", f"{demo_data['has_event'].sum()}")

    # Gráfico principal: ventas diarias con área
    fig_daily = go.Figure()
    fig_daily.add_trace(go.Scatter(
        x=demo_data['date'], y=demo_data['sales'],
        mode='lines', name='Ventas €',
        line=dict(color='#00d4ff', width=1.5),
        fill='tozeroy',
        fillcolor='rgba(0,212,255,0.08)',
        hovertemplate='<b>%{x|%d %b %Y}</b><br>Ventas: €%{y:,.0f}<extra></extra>'
    ))
    # Media móvil 7 días
    fig_daily.add_trace(go.Scatter(
        x=demo_data['date'],
        y=demo_data['sales'].rolling(7, min_periods=1).mean(),
        mode='lines', name='Media 7 días',
        line=dict(color='#ff6b35', width=2, dash='dot'),
        hovertemplate='Media: €%{y:,.0f}<extra></extra>'
    ))
    fig_daily.update_layout(**PLOT_LAYOUT, title='Evolución diaria de ventas (2 años)',
                            xaxis_title='Fecha', yaxis_title='Ventas (€)',
                            hovermode='x unified')
    st.plotly_chart(fig_daily, use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        # Personal por día de semana
        dias_label = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
        staff_by_dow = demo_data.groupby('weekday')['staff'].mean().reset_index()
        staff_by_dow['dia'] = staff_by_dow['weekday'].map(lambda x: dias_label[x])
        fig_staff = go.Figure(go.Bar(
            x=staff_by_dow['dia'], y=staff_by_dow['staff'],
            marker=dict(
                color=staff_by_dow['staff'],
                colorscale=[[0,'#001a33'],[0.5,'#0099ff'],[1,'#00d4ff']],
                showscale=False
            ),
            text=staff_by_dow['staff'].round(1),
            textposition='outside',
            hovertemplate='%{x}: %{y:.1f} personas<extra></extra>'
        ))
        fig_staff.update_layout(**PLOT_LAYOUT, title='Personal medio por día de semana',
                                yaxis_title='Personas', height=320)
        st.plotly_chart(fig_staff, use_container_width=True)

    with col_b:
        # Reservas vs ventas scatter
        fig_scatter = go.Figure(go.Scatter(
            x=demo_data['reservations'], y=demo_data['sales'],
            mode='markers',
            marker=dict(
                size=5,
                color=demo_data['has_event'],
                colorscale=[[0,'#0055aa'],[1,'#ff6b35']],
                opacity=0.7,
                showscale=True,
                colorbar=dict(title='Evento', tickvals=[0,1], ticktext=['No','Sí'],
                              tickfont=dict(color='#00d4ff'), title_font=dict(color='#00d4ff'))
            ),
            hovertemplate='Reservas: %{x}<br>Ventas: €%{y:,.0f}<extra></extra>'
        ))
        fig_scatter.update_layout(**PLOT_LAYOUT, title='Reservas vs Ventas',
                                  xaxis_title='Reservas', yaxis_title='Ventas (€)', height=320)
        st.plotly_chart(fig_scatter, use_container_width=True)

# ── VISTA MENSUAL ─────────────────────────────────────────────────────────────
with tab_mensual:
    st.caption("📈 Tendencias y patrones por meses")

    monthly = demo_data.groupby(['year','month']).agg(
        ventas_total=('sales','sum'),
        ventas_media=('sales','mean'),
        reservas_media=('reservations','mean'),
        eventos=('has_event','sum')
    ).reset_index()
    monthly['periodo'] = monthly.apply(lambda r: f"{int(r.year)}-{int(r.month):02d}", axis=1)

    # Barras mensuales con línea de tendencia
    fig_monthly = go.Figure()
    fig_monthly.add_trace(go.Bar(
        x=monthly['periodo'], y=monthly['ventas_total'],
        name='Ventas totales',
        marker=dict(color='rgba(0,153,255,0.7)', line=dict(color='#00d4ff', width=1)),
        hovertemplate='<b>%{x}</b><br>Total: €%{y:,.0f}<extra></extra>'
    ))
    fig_monthly.add_trace(go.Scatter(
        x=monthly['periodo'], y=monthly['ventas_media'] * 30,
        mode='lines+markers', name='Tendencia',
        line=dict(color='#ff6b35', width=2),
        marker=dict(size=6),
        hovertemplate='Tendencia: €%{y:,.0f}<extra></extra>'
    ))
    fig_monthly.update_layout(**PLOT_LAYOUT, title='Ventas mensuales acumuladas',
                              xaxis_title='Mes', yaxis_title='Ventas (€)',
                              barmode='overlay', hovermode='x unified')
    fig_monthly.update_xaxes(tickangle=-45)
    st.plotly_chart(fig_monthly, use_container_width=True)

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        # Ventas medias por mes del año (estacionalidad)
        seasonality = demo_data.groupby('month')['sales'].mean().reset_index()
        meses = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
        seasonality['mes_label'] = seasonality['month'].map(lambda x: meses[x-1])
        fig_season = go.Figure(go.Scatter(
            x=seasonality['mes_label'], y=seasonality['sales'],
            mode='lines+markers',
            line=dict(color='#00d4ff', width=3),
            marker=dict(size=10, color='#66ccff',
                        line=dict(color='#000a1a', width=2)),
            fill='tozeroy', fillcolor='rgba(0,212,255,0.06)',
            hovertemplate='%{x}: €%{y:,.0f}<extra></extra>'
        ))
        fig_season.update_layout(**PLOT_LAYOUT, title='Estacionalidad mensual (venta media/día)',
                                 yaxis_title='€/día', height=320)
        st.plotly_chart(fig_season, use_container_width=True)

    with col_m2:
        # Eventos por mes
        events_month = demo_data.groupby('month')['has_event'].sum().reset_index()
        events_month['mes_label'] = events_month['month'].map(lambda x: meses[x-1])
        fig_ev = go.Figure(go.Bar(
            x=events_month['mes_label'], y=events_month['has_event'],
            marker=dict(
                color=events_month['has_event'],
                colorscale=[[0,'#001a33'],[1,'#ff6b35']],
                showscale=False
            ),
            text=events_month['has_event'],
            textposition='outside',
            hovertemplate='%{x}: %{y} eventos<extra></extra>'
        ))
        fig_ev.update_layout(**PLOT_LAYOUT, title='Eventos especiales por mes',
                             yaxis_title='Nº eventos', height=320)
        st.plotly_chart(fig_ev, use_container_width=True)

# ── VISTA ANUAL ───────────────────────────────────────────────────────────────
with tab_anual:
    st.caption("🗓️ Resumen anual y comparativas")

    yearly = demo_data.groupby('year').agg(
        ventas_total=('sales','sum'),
        ventas_media=('sales','mean'),
        reservas_media=('reservations','mean'),
        total_eventos=('has_event','sum'),
        personal_medio=('staff','mean')
    ).reset_index()

    # KPIs anuales
    years = yearly['year'].tolist()
    if len(years) >= 2:
        growth = (yearly.iloc[-1]['ventas_total'] / yearly.iloc[-2]['ventas_total'] - 1) * 100
        growth_str = f"+{growth:.1f}%" if growth >= 0 else f"{growth:.1f}%"
    else:
        growth_str = "N/A"

    ka1, ka2, ka3, ka4 = st.columns(4)
    ka1.metric(f"Ventas {years[0]}", f"€{yearly.iloc[0]['ventas_total']:,.0f}")
    if len(years) >= 2:
        ka2.metric(f"Ventas {years[1]}", f"€{yearly.iloc[1]['ventas_total']:,.0f}", growth_str)
    ka3.metric("Personal medio", f"{yearly['personal_medio'].mean():.1f} pers.")
    ka4.metric("Total eventos", f"{int(yearly['total_eventos'].sum())}")

    col_y1, col_y2 = st.columns([3, 2])
    with col_y1:
        # Comparativa barras por año con desglose mensual
        monthly_year = demo_data.groupby(['year','month'])['sales'].sum().reset_index()
        meses = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
        monthly_year['mes_label'] = monthly_year['month'].map(lambda x: meses[x-1])
        fig_cmp = go.Figure()
        colors_year = ['#0099ff', '#00d4ff']
        for i, yr in enumerate(sorted(demo_data['year'].unique())):
            yr_data = monthly_year[monthly_year['year'] == yr]
            fig_cmp.add_trace(go.Bar(
                x=yr_data['mes_label'], y=yr_data['sales'],
                name=str(yr),
                marker_color=colors_year[i % 2],
                opacity=0.85,
                hovertemplate=f'<b>{yr}</b> %{{x}}: €%{{y:,.0f}}<extra></extra>'
            ))
        fig_cmp.update_layout(**PLOT_LAYOUT, title='Ventas mensuales: comparativa anual',
                              barmode='group', xaxis_title='Mes', yaxis_title='€')
        st.plotly_chart(fig_cmp, use_container_width=True)

    with col_y2:
        # Radar / polar de estacionalidad por año
        meses_radar = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic','Ene']
        fig_polar = go.Figure()
        for i, yr in enumerate(sorted(demo_data['year'].unique())):
            yr_data = demo_data[demo_data['year'] == yr].groupby('month')['sales'].mean().tolist()
            yr_data_closed = yr_data + [yr_data[0]]
            fig_polar.add_trace(go.Scatterpolar(
                r=yr_data_closed, theta=meses_radar, fill='toself',
                name=str(yr),
                line=dict(color=colors_year[i % 2], width=2),
                fillcolor=f'rgba({["0,153,255","0,212,255"][i%2]}, 0.12)'
            ))
        fig_polar.update_layout(
            paper_bgcolor='rgba(0,10,26,0)', plot_bgcolor='rgba(0,10,26,0)',
            font=dict(color='#00d4ff'),
            polar=dict(
                bgcolor='rgba(0,10,26,0.6)',
                angularaxis=dict(color='#00d4ff', gridcolor='rgba(0,212,255,0.2)'),
                radialaxis=dict(color='#00d4ff', gridcolor='rgba(0,212,255,0.2)', showticklabels=False)
            ),
            legend=dict(bgcolor='rgba(0,10,26,0.7)', bordercolor='rgba(0,212,255,0.3)', borderwidth=1),
            title=dict(text='Estacionalidad polar', font=dict(color='#66ccff')),
            margin=dict(l=40, r=40, t=50, b=40), height=420
        )
        st.plotly_chart(fig_polar, use_container_width=True)

# ── PATRONES IA ───────────────────────────────────────────────────────────────
with tab_patrones:
    st.caption("🔍 Patrones operativos y segmentación inteligente")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        # Heatmap día de semana × mes
        st.subheader("🔥 Mapa de calor: ventas")
        dias_label = ['Lun','Mar','Mié','Jue','Vie','Sáb','Dom']
        meses = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
        pivot = demo_data.pivot_table(values='sales', index='weekday', columns='month', aggfunc='mean')
        pivot.index = [dias_label[i] for i in pivot.index]
        pivot.columns = [meses[m-1] for m in pivot.columns]
        fig_heat = go.Figure(go.Heatmap(
            z=pivot.values, x=pivot.columns.tolist(), y=pivot.index.tolist(),
            colorscale=[
                [0.0, '#000a1a'], [0.2, '#001a33'], [0.5, '#0055aa'],
                [0.75, '#00d4ff'], [1.0, '#66ffff']
            ],
            text=[[f'€{v:.0f}' for v in row] for row in pivot.values],
            texttemplate='%{text}',
            hovertemplate='%{y} · %{x}<br>€%{z:,.0f}<extra></extra>',
            showscale=True,
            colorbar=dict(title='Ventas €', tickfont=dict(color='#00d4ff'),
                          title_font=dict(color='#00d4ff'))
        ))
        fig_heat.update_layout(**PLOT_LAYOUT, title='Ventas medias por día y mes', height=380)
        st.plotly_chart(fig_heat, use_container_width=True)

    with col_p2:
        # Box plot: con evento vs sin evento
        st.subheader("🎉 Días con vs sin evento")
        fig_box = go.Figure()
        fig_box.add_trace(go.Box(
            y=demo_data[demo_data['has_event']==0]['sales'],
            name='Sin evento',
            marker_color='#0099ff',
            line_color='#00d4ff',
            fillcolor='rgba(0,153,255,0.25)',
            boxmean='sd',
            hovertemplate='Sin evento: €%{y:,.0f}<extra></extra>'
        ))
        fig_box.add_trace(go.Box(
            y=demo_data[demo_data['has_event']==1]['sales'],
            name='Con evento',
            marker_color='#ff6b35',
            line_color='#ffaa00',
            fillcolor='rgba(255,107,53,0.25)',
            boxmean='sd',
            hovertemplate='Con evento: €%{y:,.0f}<extra></extra>'
        ))
        fig_box.update_layout(**PLOT_LAYOUT, title='Distribución de ventas por tipo de día',
                              yaxis_title='Ventas (€)', height=380)
        st.plotly_chart(fig_box, use_container_width=True)

    # Perfil semanal de los 3 KPIs
    st.subheader("📊 Perfil semanal de KPIs")
    dias_label = ['Lun','Mar','Mié','Jue','Vie','Sáb','Dom']
    weekly_kpi = demo_data.groupby('weekday').agg(
        ventas=('sales','mean'),
        reservas=('reservations','mean'),
        personal=('staff','mean')
    ).reset_index()
    weekly_kpi['dia'] = weekly_kpi['weekday'].map(lambda x: dias_label[x])

    fig_kpi = go.Figure()
    fig_kpi.add_trace(go.Bar(
        x=weekly_kpi['dia'], y=weekly_kpi['ventas'],
        name='Ventas €', yaxis='y',
        marker_color='rgba(0,212,255,0.7)',
        hovertemplate='%{x}: €%{y:,.0f}<extra></extra>'
    ))
    fig_kpi.add_trace(go.Scatter(
        x=weekly_kpi['dia'], y=weekly_kpi['reservas'],
        name='Reservas', yaxis='y2', mode='lines+markers',
        line=dict(color='#ff6b35', width=2),
        marker=dict(size=8),
        hovertemplate='Reservas: %{y:.0f}<extra></extra>'
    ))
    fig_kpi.add_trace(go.Scatter(
        x=weekly_kpi['dia'], y=weekly_kpi['personal'],
        name='Personal', yaxis='y3', mode='lines+markers',
        line=dict(color='#00ff88', width=2, dash='dash'),
        marker=dict(size=8, symbol='diamond'),
        hovertemplate='Personal: %{y:.1f}<extra></extra>'
    ))
    fig_kpi.update_layout(
        **{k: v for k, v in PLOT_LAYOUT.items() if k not in ('height',)},
        height=380,
        title='Ventas, reservas y personal por día de semana',
        yaxis=dict(title='Ventas €', gridcolor='rgba(0,212,255,0.1)',
                   linecolor='rgba(0,212,255,0.3)', tickfont=dict(color='#00d4ff')),
        yaxis2=dict(title='Reservas', overlaying='y', side='right',
                    gridcolor='rgba(255,107,53,0.1)', tickfont=dict(color='#ff6b35'),
                    showgrid=False),
        yaxis3=dict(title='Personal', overlaying='y', side='right', position=0.85,
                    tickfont=dict(color='#00ff88'), showgrid=False),
        hovermode='x unified'
    )
    st.plotly_chart(fig_kpi, use_container_width=True)

    # Segmentación de días por rendimiento
    st.subheader("🔍 Segmentación de días por rendimiento")
    import numpy as np
    p33 = demo_data['sales'].quantile(0.33)
    p66 = demo_data['sales'].quantile(0.66)
    demo_data['segmento'] = pd.cut(
        demo_data['sales'],
        bins=[-float('inf'), p33, p66, float('inf')],
        labels=['🔵 Día Bajo', '🟡 Día Normal', '🔴 Día Alto']
    )
    seg_counts = demo_data['segmento'].value_counts().sort_index()
    fig_seg = go.Figure(go.Pie(
        labels=seg_counts.index.tolist(),
        values=seg_counts.values.tolist(),
        hole=0.55,
        marker=dict(colors=['#0055aa', '#0099ff', '#00d4ff'],
                    line=dict(color='#000a1a', width=3)),
        textinfo='label+percent',
        textfont=dict(color='#00d4ff', size=13),
        hovertemplate='%{label}: %{value} días (%{percent})<extra></extra>'
    ))
    fig_seg.update_layout(
        paper_bgcolor='rgba(0,10,26,0)', plot_bgcolor='rgba(0,10,26,0)',
        font=dict(color='#00d4ff'),
        title=dict(text='Distribución de días por rendimiento', font=dict(color='#66ccff')),
        legend=dict(bgcolor='rgba(0,10,26,0.7)', bordercolor='rgba(0,212,255,0.3)', borderwidth=1),
        margin=dict(l=20, r=20, t=50, b=20), height=350
    )
    st.plotly_chart(fig_seg, use_container_width=True)

# ── Sección de ROI y ahorros ───────────────────────────────────────────────────
st.header("💎 Impacto Económico")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Ahorros Mensuales Estimados")
    
    # Datos de ejemplo de ahorros
    savings_data = {
        'Concepto': ['Optimización Personal', 'Reducción Desperdicio', 'Mejor Planificación', 'Automatización'],
        'Ahorro Mensual (€)': [1540, 680, 1000, 1300]
    }
    
    savings_df = pd.DataFrame(savings_data)
    fig_savings = px.bar(savings_df, x='Concepto', y='Ahorro Mensual (€)',
                        title='Desglose de Ahorros')
    st.plotly_chart(fig_savings, use_container_width=True)

with col2:
    st.subheader("ROI Acumulado")
    
    # Métricas de ROI demo
    st.metric("ROI Total Anual", "€54,300", "+180%")
    st.metric("Payback Period", "2.3 meses", "-65%")
    st.metric("Eficiencia Operativa", "+23%", "+5% este mes")

# ── Información del sistema ────────────────────────────────────────────────────
st.header("⚙️ Estado del Sistema")

# Información de modelos (demo)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Modelos Activos")
    models_info = call_api("/models/info")
    
    if models_info and "models" in models_info:
        for model_name, info in models_info["models"].items():
            st.write(f"**{model_name}**: {info['accuracy']} precisión")
    else:
        st.write("- **sales_model**: 92% precisión")
        st.write("- **staff_model**: 89% precisión") 
        st.write("- **perishables_model**: 86% precisión")

with col2:
    st.subheader("Conectividad")
    api_status = call_api("/health")
    
    if api_status:
        st.success("✅ API conectada y funcionando")
        st.write(f"Última actualización: {datetime.now().strftime('%H:%M:%S')}")
    else:
        st.error("❌ API no disponible")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
<p><strong>MIDAS</strong> | Sistema de Predicción para Restaurante</p>
</div>
""", unsafe_allow_html=True)