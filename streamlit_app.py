import streamlit as st
import pandas as pd
import subprocess

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(page_title='Reporte del de focalización')  # Debe ser la primera línea de Streamlit

# Ejecutar el script de limpieza
result = subprocess.run(['python3', 'data/focalizacion.py'], check=True, capture_output=True, text=True)

# Cargar datos
data = pd.read_csv('data/focalizacion_resultados.csv') 

# Mostrar datos
st.dataframe(data)
