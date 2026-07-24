import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página con temática Air Tractor
st.set_page_config(
    page_title="Agro Fly - Gestión de Aviación Agrícola",
    page_icon="✈️",
    layout="wide",
)

# Estilos CSS personalizados (Colores Amarillo Air Tractor y Azul Marino)
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .stButton>button {
        background-color: #ffcc00;
        color: #0b1d3a;
        font-weight: bold;
        border-radius: 6px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #e6b800;
        color: #0b1d3a;
    }
    h1, h2, h3 {
        color: #0b1d3a;
    }
    .sidebar .sidebar-content {
        background-color: #0b1d3a;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Título Principal
st.title("✈️ Agro Fly - Control de Pista & Operaciones")
st.markdown(
    "**Air Tractor 301 (Radial)** | Control Operativo, Tacómetro, Recetas y Comisiones"
)

# Menú lateral de navegación
menu = st.sidebar.selectbox(
    "Menú Principal",
    [
        "🚀 Registrar Vuelo Diario",
        "👥 Clientes y Recetas",
        "⚙️ Mantenimiento (25h/50h/100h)",
        "💰 Control de Comisiones",
        "📄 Revisión y Exportar PDF",
    ],
)

# Simulación de Base de Datos en Memoria (Sesión)
if "vuelos" not in st.session_state:
    st.session_state.vuelos = [
        {
            "id": 1,
            "fecha": "2026-07-24",
            "pagador": "Rayo S.A.",
            "productor": "Sr. Dani",
            "lote": "Estancia San José - Lote 3",
            "ingeniero": "Ing. Carlos Gómez",
            "tipo": "Líquido",
            "receta": "Insecticida X (20 L/ha)",
            "carga_litros": 800,
            "has_gps": 40.0,
            "has_cobro": 40.0,
            "tac_ini": 1234.0,
            "tac_fin": 1234.8,
            "observacion": "Sin inconvenientes",
        }
    ]

if "comisiones_pagos" not in st.session_state:
    st.session_state.comisiones_pagos = []

# ==========================================
# 1. REGISTRAR VUELO DIARIO
# ==========================================
if menu == "🚀 Registrar Vuelo Diario":
    st.header("Registro de Vuelo - Pista")

    with st.form("form_vuelo"):
        col1, col2, col3 = st.columns(3)

        with col1:
            fecha = st.date_input("Fecha del Vuelo", datetime.now())
            pagador = st.selectbox(
                "Pagador / Financiera", ["Rayo S.A.", "Campo Fe", "Particular"]
            )
            productor = st.text_input(
                "Productor / Establecimiento", "Ej: Estancia Puerto Casado"
            )

        with col2:
            lote = st.text_input("Lote / Parcela", "Ej: Lote 002")
            ingeniero = st.text_input(
                "Ing. Agrónomo a cargo", "Ej: Ing. Juan Pérez"
            )
            tipo_aplicacion = st.selectbox(
                "Tipo de Aplicación", ["Líquido", "Sólido (Urea/Fertilizante)"]
            )

        with col3:
            receta = st.text_input(
                "Receta / Producto", "Ej: Insecticida 15 L/has"
            )
            carga_litros = st.number_input(
                "Litros / Kilos Cargados", value=1000.0, step50.0
            )
            has_gps = st.number_input(
                "Hectáreas según GPS", value=50.0, step5.0
            )

        st.markdown("---")
        st.subheader("Control de Tacómetro (Analógico) y Consumos")
        col4, col5, col6, col7 = st.columns(4)

        with col4:
            tac_ini = st.number_input(
                "Tacómetro Inicial", value=1234.0, step=0.1
            )
        with col5:
            tac_fin = st.number_input(
                "Tacómetro Final", value=1234.7, step=0.1
            )
        with col6:
            combustible = st.number_input(
                "Combustible agregado (L)", value=120.0
            )
        with col7:
            aceite = st.number_input("Aceite agregado (L)", value=2.0)

        observacion = st.text_area(
            "Observaciones (Ej: Taponamiento de picos, purga, etc.)"
        )

        submitted = st.form_submit_button("Guardar Vuelo en el Sistema")

        if submitted:
            horas_vuelo = round(tac_fin - tac_ini, 2)
            nuevo_vuelo = {
                "id": len(st.session_state.vuelos) + 1,
                "fecha": str(fecha),
                "pagador": pagador,
                "productor": productor,
                "lote": lote,
                "ingeniero": ingeniero,
                "tipo": tipo_aplicacion,
                "receta": receta,
                "carga_litros": carga_litros,
                "has_gps": has_gps,
                "has_cobro": has_gps,  # Por defecto igual al GPS, editable después
                "tac_ini": tac_ini,
                "tac_fin": tac_fin,
                "horas": horas_vuelo,
                "observacion": observacion,
            }
            st.session_state.vuelos.append(nuevo_vuelo)
            st.success(
                f"¡Vuelo guardado con éxito! Horas de tacómetro calculadas: {horas_vuelo} hrs."
            )

# ==========================================
# 2. CLIENTES Y RECETAS
# ==========================================
elif menu == "👥 Clientes y Recetas":
    st.header("Gestión de Clientes, Parcelas y Recetas")
    st.info(
        "Aquí puedes precargar recetas de los ingenieros agrónomos para evitar los papelitos rotos en la pista."
    )

    with st.form("form_receta"):
        c1, c2, c3 = st.columns(3)
        with c1:
            cli = st.text_input("Cliente / Pagador")
        with c2:
            ing = st.text_input("Ingeniero Agrónomo")
        with c3:
            prod_receta = st.text_input(
                "Detalle de Receta / Dosis por Hectárea"
            )
        if st.form_submit_button("Guardar Receta en Base"):
            st.success(f"Receta de {ing} registrada correctamente.")

    st.subheader("Historial de Clientes Activos (Temporada 25/26)")
    df_clientes_demo = pd.DataFrame(
        {
            "Cliente / Pagador": ["Rayo S.A.", "Campo Fe", "GASA"],
            "Estado": ["Activo", "Activo", "Pendiente"],
            "Canal de Cobro": ["Cocco", "Directo", "Cocco"],
        }
    )
    st.dataframe(df_clientes_demo, use_container_width=True)

# ==========================================
# 3. MANTENIMIENTO PREVENTIVO (25h / 50h / 100h)
# ==========================================
elif menu == "⚙️ Mantenimiento (25h/50h/100h)":
    st.header("Control Mecánico - Air Tractor 301")

    # Calcular horas totales acumuladas basadas en los vuelos
    total_horas_voladas = sum(
        [v.get("horas", 0.7) for v in st.session_state.vuelos]
    )
    proximo_service = 25 - (total_horas_voladas % 25)

    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Horas Totales Acumuladas", f"{total_horas_voladas:.1f} hrs")
    col_m2.metric(
        "Próximo Service (Alarma)",
        f"Faltan {proximo_service:.1f} hrs",
        delta_color="inverse",
    )
    col_m3.metric("Mecánico Asignado 100h", "Externo (Taller)")

    st.subheader("Registro de Costos de Mantenimiento y Repuestos")
    with st.form("form_mantenimiento"):
        cm1, cm2, cm3 = st.columns(3)
        with cm1:
            tipo_serv = st.selectbox(
                "Tipo de Mantenimiento / Gasto",
                [
                    "Service 25 Horas",
                    "Service 50 Horas",
                    "Service 75 Horas",
                    "Service 100 Horas",
                    "Cambio de Neumático",
                    "Cambio de Cilindro",
                    "Reparación de Magnetos",
                    "Mano de Obra Taller",
                ],
            )
        with cm2:
            costo_usd = st.number_input("Costo en Dólares ($USD)", value=150.0)
        with cm3:
            fecha_serv = st.date_input("Fecha de Mantenimiento", datetime.now())

        obs_serv = st.text_input("Detalles del repuesto o trabajo realizado")
        if st.form_submit_button("Registrar Gasto de Mantenimiento"):
            st.success(
                f"Gasto de {tipo_serv} por ${costo_usd} registrado con éxito."
            )

# ==========================================
# 4. CONTROL DE COMISIONES
# ==========================================
elif menu == "💰 Control de Comisiones":
    st.header("Liquidación de Comisiones ($1 USD / Hectárea Cobrada)")

    total_has_cobradas = sum(
        [v.get("has_cobro", 0) for v in st.session_state.vuelos]
    )
    comision_total = total_has_cobradas * 1.0  # $1 por hectárea

    # Simular pagos recibidos por papá
    total_pagado = sum(st.session_state.comisiones_pagos)
    saldo_pendiente = comision_total - total_pagado

    cc1, cc2, cc3 = st.columns(3)
    cc1.metric(
        "Total Hectáreas Cobradas", f"{total_has_cobradas} Has", "$1 / ha"
    )
    cc2.metric("Comisión Generada", f"${comision_total:.2f} USD")
    cc3.metric(
        "Saldo Pendiente de Pago",
        f"${saldo_pendiente:.2f} USD",
        delta_color="inverse",
    )

    st.markdown("---")
    st.subheader("Registrar Pago de Comisión por parte de Papá")
    with st.form("form_pago_comision"):
        monto_pago = st.number_input("Monto abonado ($USD)", value=100.0)
        if st.form_submit_button("Registrar Pago"):
            st.session_state.comisiones_pagos.append(monto_pago)
            st.success(f"Se registró un pago de ${monto_pago} USD.")
            st.rerun()

# ==========================================
# 5. REVISIÓN Y EXPORTAR PDF
# ==========================================
elif menu == "📄 Revisión y Exportar PDF":
    st.header("Revisión Libre de Datos y Generación de PDF")
    st.info(
        "Aquí puedes corregir manualmente cualquier discrepancia (por picos trancados, GPS descalibrado, etc.) antes de bajar el reporte definitivo para el cliente o la financiera."
    )

    if not st.session_state.vuelos:
        st.warning("No hay vuelos registrados todavía.")
    else:
        # Tabla editable de vuelos
        df_vuelos = pd.DataFrame(st.session_state.vuelos)
        st.subheader("Detalle de Vuelos Registrados (Editable)")

        edited_df = st.data_editor(
            df_vuelos, num_rows="dynamic", use_container_width=True
        )

        st.markdown("---")
        st.subheader("Personalización del Reporte Final")
        col_pdf1, col_pdf2 = st.columns(2)
        with col_pdf1:
            nro_cuenta = st.text_input(
                "Datos de Cuenta Bancaria para Transferencia",
                "Banco Sudameris - Cta Cte: 12345678 - RUC: 80000000-0",
            )
        with col_pdf2:
            nota_adicional = st.text_area(
                "Notas al pie / Observaciones comerciales",
                "Servicio prestado con Air Tractor 301. Gracias por confiar en FJ Servicios.",
            )

        if st.button("📥 Generar PDF con Resumen y Datos de Pago"):
            st.success(
                "¡Reporte PDF generado correctamente con los ajustes manuales aplicados y listo para enviar por WhatsApp!"
            )
            # Simulación visual del reporte
            st.markdown("### Vista Previa del Reporte PDF - FJ Servicios")
            st.code(
                f"""
            ==================================================
            FJ SERVICIOS - AVIACIÓN AGRÍCOLA
            Tel: 0983 081 234 | agroflyzp@gmail.com
            ==================================================
            Resumen de Trabajos y Vuelos Realizados:
            - Total de Hectáreas procesadas: {edited_df['has_cobro'].sum()} Has
            - Total de Vuelos: {len(edited_df)}
            --------------------------------------------------
            Observación de Cierre: {nota_adicional}
            Forma de Pago: {nro_cuenta}
            ==================================================
            """,
                language="text",
            )