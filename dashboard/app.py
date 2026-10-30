import streamlit as st
import pandas as pd
import sys
import os 
import plotly.express as px

# Ruta para los modulos locales.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transformation import load_and_clean_data
from src.features import calculate_rfm

st.set_page_config(
    page_title="Online Retail Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Online Retail y Segmentacion de Clientes")
st.markdown("Panel analitico de transacciones y segmentacion de clientes basados en el modelo **RFM (Recencia, Frecuencia, Monetario)**.")

@st.cache_data
def get_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "data", "raw", "online_retail.csv")
    df_clean = load_and_clean_data(file_path)
    rfm_df = calculate_rfm(df_clean)
    return df_clean, rfm_df

with st.spinner("Cargando y procesando datos del e-commerce..."):
    df_clean, rfm_df = get_data()

st.subheader("Indicadores Clave de Desempeno")
col1, col2, col3 = st.columns(3)

total_revenue = df_clean['TotalRevenue'].sum()
total_transactions = df_clean['InvoiceNo'].nunique()
total_customers = len(rfm_df)

col1.metric("Ingresos Totales", f"${total_revenue:,.2f}")
col2.metric("Transacciones Totales", f"{total_transactions:,}")
col3.metric("Clientes Unicos", f"{total_customers:,}")

st.markdown("---")

st.subheader("Analisis de Clientes con Mayor Valor (Top 10)")
st.markdown("Identificacion rapida de los clientes que aportan el mayor volumen de ingresos al negocio (Modelo RFM).")

top_customers_df = rfm_df.sort_values(by='Monetary', ascending=False).head(10)
top_customers_df['CustomerID_str'] = top_customers_df['CustomerID'].astype(str)

fig_bar = px.bar(
    top_customers_df,
    x='CustomerID_str',
    y='Monetary',
    color='Frequency',
    title='Top 10 Clientes por Gasto Total ($) y Frecuencia de Compra',
    labels={
        'CustomerID_str': 'ID de Cliente',
        'Monetary': 'Gasto Total ($)',
        'Frequency': 'Frecuencia (Compras)'
    },
    template='plotly_white',
    color_continuous_scale='Viridis'
)
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

st.subheader("Explorador de Clientes (Modelo RFM)")
st.markdown("Filtra y analiza el comportamiento de los clientes de acuerdo con su valor monetario.")

min_monetario = st.slider("Filtrar clientes con un gasto monetario minimo de ($):", 0, int(rfm_df['Monetary'].max()), 500)

filtered_rfm = rfm_df[rfm_df['Monetary'] >= min_monetario].sort_values(by='Monetary', ascending=False)

st.write(f"Mostrando {len(filtered_rfm)} clientes que cumplen con el criterio:")
st.dataframe(filtered_rfm, width='stretch')

st.success("Dashboard cargado correctamente.")