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
st.text("SS - Soporte Social")
st.text("IE Autopercibida - Inteligencia emocional 19 y mayores")
st.text("IE Baron ICE - Inteligencia emocional 18 o menores")
# Cargar y mostrar los resultados estres
try:
    data = pd.read_csv('data/check_total.csv')

    # Función para reemplazar valores, ignorando la columna "Usuarios"
    def reemplazar_valores(df):
        df_modificado = df.copy()  # Crear una copia del DataFrame
        columnas_a_reemplazar = df.columns[df.columns != 'Usuarios']  # Excluir la columna "Usuarios"
        
        # Reemplazar valores con HTML
        df_modificado[columnas_a_reemplazar] = df_modificado[columnas_a_reemplazar].applymap(
            lambda x: '<span style="color:red;">✖️</span>' if x == 0 or pd.isna(x) else '✅'
        )
        
        return df_modificado

    # Aplicar la función
    df_reemplazado = reemplazar_valores(data)

    # Mostrar solo el DataFrame modificado con el argumento unsafe_allow_html=True
    st.markdown(df_reemplazado.to_html(escape=False), unsafe_allow_html=True)

except FileNotFoundError:
    # No mostrar error si no se encuentra el archivo
    pass
except Exception:
    # No mostrar error en otros casos
    pass

 
