import streamlit as st
import pandas as pd
import subprocess

st.title("Análisis de Datos Interactivos")

# Ejecutar el script de limpieza
try:
    result = subprocess.run(['python3', 'data/focalizacion.py'], check=True, capture_output=True, text=True)
    st.success("Datos procesados exitosamente.")
except subprocess.CalledProcessError as e:
    st.error(f"Error al ejecutar focalizacion.py: {str(e)}\nSalida: {e.stdout}\nError: {e.stderr}")

# Cargar y mostrar los resultados
try:
    data = pd.read_csv('data/focalizacion_resultados.csv')
    st.dataframe(data)
except FileNotFoundError:
    st.error("El archivo focalizacion_resultados.csv no se encontró. Verifica la ruta.")
except Exception as e:
    st.error(f"Ocurrió un error al cargar los datos: {str(e)}")

