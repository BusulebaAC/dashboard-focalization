import streamlit as st
import pandas as pd
import subprocess

st.title("Análisis de Datos Interactivos")

# Ejecutar el script de limpieza
try:
    subprocess.run(['python3', 'data/focalizacion.py'], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError:
    # No hacer nada en caso de error
    pass

# Cargar y mostrar los resultados
try:
    data = pd.read_csv('data/focalizacion_resultados.csv')
    st.dataframe(data)
except FileNotFoundError:
    # No mostrar error si no se encuentra el archivo
    pass
except Exception:
    # No mostrar error en otros casos
    pass


