import streamlit as st
import pandas as pd
import subprocess

# Ejecutar el script de limpieza
try:
    subprocess.run(['python3', 'data/focalizacion.py'], check=True)
    st.success("Datos procesados exitosamente.")
except subprocess.CalledProcessError as e:
    st.error(f"Error al ejecutar focalizacion.py: {e}")
    
# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Reporte del de focalización'
)

# Cargar datos
data = pd.read_csv('data/focalizacion_resultados.pkl')

# Mostrar datos
st.dataframe(data)