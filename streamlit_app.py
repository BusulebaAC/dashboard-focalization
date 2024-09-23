import streamlit as st
import pandas as pd
import subprocess

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(page_title='Reporte del de focalización')  # Debe ser la primera línea de Streamlit

# Ejecutar el script de limpieza
try:
    result = subprocess.run(['python3', 'data/focalizacion.py'], check=True, capture_output=True, text=True)
    st.success("Datos procesados exitosamente.")
    print(result.stdout)  # Imprimir salida estándar en la consola
except subprocess.CalledProcessError as e:
    st.error(f"Error al ejecutar focalizacion.py: {e}\n{e.output}")

# Cargar datos
data = pd.read_pickle('data/focalizacion_resultados.csv')  # Cambia a .csv si es necesario

# Mostrar datos
st.dataframe(data)
