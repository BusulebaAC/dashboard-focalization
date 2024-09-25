import streamlit as st
import pandas as pd
import subprocess

st.title("Reporte BUSULEBA")

st.subheader("Focalización")
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


# Ejecutar el script de limpieza de las otras encuestas
try:
    subprocess.run(['python3', 'data/check_de_encuestas.py'], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError:
    # No hacer nada en caso de error
    pass

st.subheader("Encuestas")
# Cargar y mostrar los resultados estres
try:
    data = pd.read_csv('data/check_total.csv')
    st.dataframe(data)
except FileNotFoundError:
    # No mostrar error si no se encuentra el archivo
    pass
except Exception:
    # No mostrar error en otros casos
    pass



