import streamlit as st
import pandas as pd

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Reporte del de focalización'
)

# Cargar datos
data = pd.read_csv('data/focalizacion_resultados.pkl')

# Mostrar datos
st.dataframe(data)