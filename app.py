import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Agro-Fly - Gestión de Vuelos y Clientes", page_icon="✈️", layout="wide")

# Estilo visual inspirado en la aviación agrícola (Air Tractor / tonos aeronáuticos)
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    h1, h2, h3 {
        color: #1b365d;
    }
    .stButton>button {
        background-color: #d9534f;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #c9302c;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✈️ Agro-Fly: Gestión de Vuelos Agrícolas")
st.markdown("---")

# Menú lateral para navegar entre secciones
menu = st.sidebar.selectbox("Seleccioná una sección", ["Control de Vuelos", "Gestión de Clientes", "Comisiones y Resumen"])

if menu == "Control de Vuelos":
    st.header("📋 Registro de Vuelos")
    
    col1, col2 = st.columns(2)
    with col1:
        fecha = st.date_input("Fecha del Vuelo", datetime.now())
        cliente = st.selectbox("Cliente", ["Estancia La Morena", "Agropecuaria El Sol", "Don Juan S.A.", "Otro"])
        lote = st.text_input("Nombre del Lote / Establecimiento")
    
    with col2:
        producto = st.text_input("Producto Aplicado (Ej: Glifosato, Urea)")
        litros = st.number_input("Litros / Kilos Cargados", value=1000.0, step=50.0)
        hectareas = st.number_input("Hectáreas Tratadas", value=100.0, step=10.0)

    if st.button("Guardar Vuelo"):
        st.success(f"¡Vuelo registrado con éxito para {cliente} en el lote {lote}!")

elif menu == "Gestión de Clientes":
    st.header("👥 Base de Clientes (25/26)")
    
    # Tabla simulada de clientes
    data_clientes = {
        "Cliente": ["Estancia La Morena", "Agropecuaria El Sol", "Don Juan S.A."],
        "Contacto": ["Carlos Gómez", "Mariana Pérez", "Juan Carlos Benítez"],
        "Teléfono": ["3754-123456", "3754-987654", "3754-112233"],
        "Localidad": ["Oberá", "Alem", "Posadas"]
    }
    df_clientes = pd.DataFrame(data_clientes)
    st.dataframe(df_clientes, use_container_width=True)

elif menu == "Comisiones y Resumen":
    st.header("💰 Resumen y Comisiones")
    st.info("Acá podés visualizar el acumulado de hectáreas aplicadas y las comisiones correspondientes.")
    
    # Métricas simuladas
    col1, col2, col3 = st.columns(3)
    col1.metric("Hectáreas Totales", "1,250 ha")
    col2.metric("Vuelos Realizados", "18")
    col3.metric("Comisión Estimada", "$ 450,000")
