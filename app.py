import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Agro-Fly - Gestión Profesional", page_icon="✈️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    h1, h2, h3 { color: #1b365d; }
    .stButton>button {
        background-color: #d9534f;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }
    .stButton>button:hover { background-color: #c9302c; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("✈️ Agro-Fly: Control Profesional de Vuelos Agrícolas")
st.markdown("---")

menu = st.sidebar.selectbox("Menú Principal", ["Registrar Vuelo / Receta", "Base de Clientes", "Reportes y Cargas"])

if menu == "Registrar Vuelo / Receta":
    st.header("📋 Carga de Operación y Caldo de Aplicación")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        fecha = st.date_input("Fecha", datetime.now())
        cliente = st.selectbox("Cliente / Empresa", ["Estancia La Morena", "Agropecuaria El Sol", "Don Juan S.A.", "Otro"])
    with col2:
        establecimiento = st.text_input("Establecimiento / Lote")
        piloto = st.selectbox("Piloto Asignado", ["Juan Pérez", "Carlos Gómez", "Mario Rossi"])
    with col3:
        capacidad_tanque = st.selectbox("Capacidad del Tanque (Litros)", [1000.0, 850.0, 500.0, 400.0], index=0)
        hectareas_lote = st.number_input("Hectáreas Totales del Lote", value=150.0, step=10.0)

    st.markdown("---")
    st.subheader("🧪 Configuración del Caldo (Múltiples Productos)")
    st.markdown("Agregá los productos que componen la mezcla y su dosis respectiva por hectárea.")

    # Simulamos una tabla interactiva para agregar productos
    if 'productos_caldo' not in st.session_state:
        st.session_state.productos_caldo = pd.DataFrame(columns=["Producto", "Dosis (L o Kg / ha)", "Unidad"])

    with st.form("form_producto", clear_on_submit=True):
        c1, c2, c3, c4 = st.columns([3, 2, 2, 1])
        with c1:
            prod_nombre = st.text_input("Nombre del Producto / Adyuvante")
        with c2:
            prod_dosis = st.number_input("Dosis", min_value=0.0, value=1.0, step=0.1)
        with c3:
            prod_unidad = st.selectbox("Unidad", ["Litros", "Kilos", "CC", "Gramos"])
        with c4:
            st.markdown("<br>", unsafe_allow_html=True)
            agregar_btn = st.form_submit_button("Agregar")
        
        if agregar_btn and prod_nombre:
            nuevo_item = pd.DataFrame([[prod_nombre, prod_dosis, prod_unidad]], columns=["Producto", "Dosis (L o Kg / ha)", "Unidad"])
            st.session_state.productos_caldo = pd.concat([st.session_state.productos_caldo, nuevo_item], ignore_index=True)

    if not st.session_state.productos_caldo.empty:
        st.write("**Productos cargados para este vuelo:**")
        st.dataframe(st.session_state.productos_caldo, use_container_width=True)
        
        if st.button("🗑️ Limpiar Lista de Productos"):
            st.session_state.productos_caldo = pd.DataFrame(columns=["Producto", "Dosis (L o Kg / ha)", "Unidad"])
            st.rerun()

    st.markdown("---")
    if st.button("💾 Guardar Operación Completa", type="primary"):
        st.success(f"¡Operación registrada con éxito para el lote {establecimiento} con tanque de {capacidad_tanque}L!")

elif menu == "Base de Clientes":
    st.header("👥 Gestión de Clientes y Establecimientos")
    data_clientes = {
        "Cliente": ["Estancia La Morena", "Agropecuaria El Sol", "Don Juan S.A."],
        "Contacto": ["Carlos Gómez", "Mariana Pérez", "Juan Carlos Benítez"],
        "Teléfono": ["3754-123456", "3754-987654", "3754-112233"],
        "Localidad": ["Oberá", "Alem", "Posadas"]
    }
    st.dataframe(pd.DataFrame(data_clientes), use_container_width=True)

elif menu == "Reportes y Cargas":
    st.header("📊 Resumen de Vuelos y Estadísticas")
    col1, col2, col3 = st.columns(3)
    col1.metric("Hectáreas Totales Aplicadas", "2,450 ha")
    col2.metric("Cargas Totales Realizadas", "42")
    col3.metric("Litros Totales Dispersados", "38,500 L")
    st.info("Próximamente: Exportación de reportes detallados en PDF para presentación a clientes y entes regulatorios.")
