import streamlit as st 
import pandas as pd 
import plotly.express as px 
st.title("Dashboard de Ventas") 
# Sidebar 
with st.sidebar: 
st.header("Filtros") 
year = st.selectbox("Año", [2022, 2023, 2024])
# Datos de ejemplo 
df = pd.DataFrame({ 
"Año": [2022, 2022, 2023, 2023, 2024, 2024], 
"Mes": ["Ene","Feb","Ene","Feb","Ene","Feb"], 
"Ventas": [100,150,200,180,250,300] 
}) 
df_filtrado = df[df["Año"] == year] 
# Métricas 
st.metric("Ventas totales", f"{df_filtrado['Ventas'].sum()} €") 
# Gráfico 
fig = px.bar(df_filtrado, x="Mes", y="Ventas", title="Ventas por mes") 
st.plotly_chart(fig) 
# Tabla 
st.dataframe(df_filtrado) 