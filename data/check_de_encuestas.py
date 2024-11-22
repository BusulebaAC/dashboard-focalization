# -*- coding: utf-8 -*-
"""check de encuestas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VMwbXocDEMhvPoZMnEMuUtxHeGoIKnRz
"""
# importar librerías necesarias
import pandas as pd
from unidecode import unidecode

# definir la url de cada google sheets en la web
url_ie_autopercibida = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTBC4rqPYUZv0mz_Bib1YDbozpDNuNi8RevDBlGhFtWY1qqNsOB7AQzIWINDzQDQnG4WElfC_REXaE_/pub?gid=674318718&single=true&output=csv'
url_estres = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTdC4-7fDOtpF0OB11jY6opSsraRbcUeDVEhiHLeZhIwJVGUYBLVMyimXl0slteOR2IPwjG3NAbK3r2/pub?gid=266592112&single=true&output=csv'
url_ss = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy1HfwiXB9YIlswNVkHYzl2bWhmPS-m0rjK-AO3_nZTB0tQ0sGEi54YTaMnsoatlfDEkKEgsK6ksIV/pub?gid=1642954170&single=true&output=csv'
url_ie_baron_ice = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRAsrl7ChUwyWQFpMxogVGQAyDUVGm0An0--NtBFoNjrSex9g_-n2_t-R_9SW_DJ9U_oYSAbjnshqtl/pub?gid=1082257911&single=true&output=csv'

# leer cada sheets para convertirlo en df
ie_autopercibida = pd.read_csv (url_ie_autopercibida)
ie_baron_ice = pd.read_csv (url_ie_baron_ice)
estres = pd.read_csv (url_estres)
ss = pd.read_csv (url_ss)

# funcion para transformar df y datos
def transform_df(lista_df):
    for i, df in enumerate(lista_df):
      df.drop(df.columns[[0, 1]], axis=1, inplace=True)
      df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.lower()

# lista de dataframes
dataframes = [ie_autopercibida, ie_baron_ice, estres, ss]

# llamar la funcion
transform_df(dataframes)

reemplazo_ss = {
    'Nunca' : 0,
    'Pocas veces' : 1,
    'Algunas veces' : 2,
    'La mayoría de las veces' : 3,
    'Siempre' : 4
}

def reemplazos_ss (df):
  for i in df.columns:
    df[i] = df[i].replace(reemplazo_ss)
  return df

reemplazos_ss (ss)

# Seleccionar solo las columnas numéricas
numerical_df = ss.select_dtypes(include='number')

# Calcular la suma de cada fila
ss['Total'] = numerical_df.sum(axis=1)
# limpiar nombres
ss ['Nombre completo'] = ss ['Nombre completo'].str.lower()
ss['Nombre completo'] = ss['Nombre completo'].str.rstrip('*')
ss['Nombre completo'] = ss['Nombre completo'].apply(unidecode)
ss

reemplazo_estres = {
    'Nunca' : 0,
    'Casi nunca' : 1,
    'De vez en cuando' : 2,
    'A menudo' : 3,
    'Muy a menudo' : 4
}

def reemplazos_estres (df):
  for i in df.columns:
    df[i] = df[i].replace(reemplazo_estres)
  return df

reemplazos_estres (estres)
numerical_df = estres.select_dtypes(include='number')
# Calcular la suma de cada fila
estres['Total'] = numerical_df.sum(axis=1)
# limpiar nombres
estres ['Nombre completo'] = estres ['Nombre completo'].str.lower()
#
estres['Nombre completo'] = estres['Nombre completo'].str.rstrip('*')
estres['Nombre completo'] = estres['Nombre completo'].apply(unidecode)

reemplazo_ie_baron_ice = {
    'Muy rara vez' : 0,
    'Rara vez' : 1,
    'A menudo' : 2,
    'Muy a menudo' : 3
}

def reemplazos_ie_baron_ice (df):
  for i in df.columns:
    df[i] = df[i].replace(reemplazo_ie_baron_ice)
  return df

reemplazos_ie_baron_ice (ie_baron_ice)
numerical_df = ie_baron_ice.select_dtypes(include='number')
# Calcular la suma de cada fila
ie_baron_ice['Total'] = numerical_df.sum(axis=1)
# limpiar nombres
ie_baron_ice ['Nombre completo'] = ie_baron_ice ['Nombre completo'].str.lower()
#
ie_baron_ice['Nombre completo'] = ie_baron_ice['Nombre completo'].str.rstrip('*')
ie_baron_ice['Nombre completo'] = ie_baron_ice['Nombre completo'].apply(unidecode)

check_total=pd.DataFrame()
check_total ['Usuarios'] = ss['Nombre completo']
check_total ['SS'] = ss ['Total']

check_total ['Estres'] = 0
check_total ['IE Autopercibida'] = 0
check_total ['IE Baron Ice'] = 0

for _, row in estres.iterrows():
    if row['Nombre completo'] in check_total['Usuarios'].values:
        check_total.loc[check_total['Usuarios'] == row['Nombre completo'], 'Estres'] = row['Total']
    else:
        # Si no existe el nombre, añádelo con el total de estres y 0 en las demás columnas
        new_row = pd.DataFrame({
            'Usuarios': [row['Nombre completo']],
            'SS': [0],
            'Estres': [row['Total']],
            'IE Autopercibida': [0],
            'IE Baron Ice': [0]
        })
        check_total = pd.concat([check_total, new_row], ignore_index=True)

for _, row in ie_baron_ice .iterrows():
    if row['Nombre completo'] in check_total['Usuarios'].values:
        check_total.loc[check_total['Usuarios'] == row['Nombre completo'], 'IE Baron Ice'] = row['Total']
    else:
        # Si no existe el nombre, añádelo con el total de ie y 0 en las demás columnas
        new_row = pd.DataFrame({
            'Usuarios': [row['Nombre completo']],
            'SS': [0],
            'Estres': [0],
            'IE Autopercibida': [0],
            'IE Baron Ice': [row['Total']]
        })
        check_total = pd.concat([check_total, new_row], ignore_index=True)

check_total_copy = check_total.copy()
check_total

check_total_copy.at[3, 'IE Baron Ice'] = 36
check_total_copy.at[4, 'IE Baron Ice'] = 46
check_total_copy.at[5, 'Estres'] = 30
check_total_copy.at[6, 'Estres'] = 29
check_total_copy.at[7, 'IE Baron Ice'] = 46

filas_a_eliminar = [17,18,14,12,19]
check_total_copy = check_total_copy.drop(filas_a_eliminar)

check_total_copy.replace(0, '*', inplace=True)

#ie_baron_ice.to_csv('/workspaces/dashboard-focalization/data/ie_baron_ice.csv', index=False)
#ss.to_csv('/workspaces/dashboard-focalization/data/ss.csv', index=False)
#estres.to_csv('/workspaces/dashboard-focalization/data/estres.csv', index=False)
check_total_copy.reset_index(drop=True, inplace = True)

'''
limpieza corregidas
'''
# Definir las URLs o rutas locales de los otros 4 CSVs
url_ie_autopercibida_2 = 'https://docs.google.com/spreadsheets/d/1cOeWbh-LbdwP7_hqu-Dtk6N28E9cwkUzlTJMhWN1_sc/gviz/tq?tqx=out:csv'
url_estres_2 = 'https://docs.google.com/spreadsheets/d/19bdfQHVxca7Ga5SyJbTCi7klsorYYEOgll6W7rjZIo0/gviz/tq?tqx=out:csv'
url_ss_2 = 'https://docs.google.com/spreadsheets/d/18RiD5ezgXnEY5BUesdOddjkBS5d1HxhSCsG2E7fwhMg/gviz/tq?tqx=out:csv'
url_ie_baron_ice_2 = 'https://docs.google.com/spreadsheets/d/1H0g2_Wl35QM6Tx4cpbhZazgAVxGi_Te-MLlmqei2ilw/gviz/tq?tqx=out:csv'

# Leer los otros 4 archivos
ie_autopercibida_2 = pd.read_csv(url_ie_autopercibida_2)
ie_baron_ice_2 = pd.read_csv(url_ie_baron_ice_2)
estres_2 = pd.read_csv(url_estres_2)
ss_2 = pd.read_csv(url_ss_2)

# Transformar las nuevas tablas (solo si es necesario)
transform_df([ie_autopercibida_2, ie_baron_ice_2, estres_2, ss_2])

# Reemplazar los valores en las nuevas tablas
reemplazos_ss(ss_2)
reemplazos_estres(estres_2)
reemplazos_ie_baron_ice(ie_baron_ice_2)

# Calcular los totales para las nuevas tablas
# Filtrar solo las columnas numéricas, luego eliminar 'edad' y calcular la suma
numerical_columns = ss_2.select_dtypes(include='number').columns.difference(['Edad (solo el número)'])
ss_2['Total'] = ss_2[numerical_columns].sum(axis=1)

numerical_columns = estres_2.select_dtypes(include='number').columns.difference(['Edad (solo el número)'])
estres_2['Total'] = estres_2[numerical_columns].sum(axis=1)

numerical_columns = ie_baron_ice_2.select_dtypes(include='number').columns.difference(['Edad (solo el número)'])
ie_baron_ice_2['Total'] = ie_baron_ice_2[numerical_columns].sum(axis=1)

# Limpiar los nombres
for df in [ss_2, estres_2, ie_baron_ice_2]:
    df['Nombre completo'] = df['Nombre completo'].str.lower().apply(unidecode).str.rstrip('*')

# Crear una copia de check_total para evitar modificar la original durante el proceso
check_total_copy_2 = check_total.copy()

# Agregar datos de ss_2
for _, row in ss_2.iterrows():
    if row['Nombre completo'] in check_total_copy_2['Usuarios'].values:
        check_total_copy_2.loc[check_total_copy_2['Usuarios'] == row['Nombre completo'], 'SS'] = row['Total']
    else:
        new_row = pd.DataFrame({
            'Usuarios': [row['Nombre completo']],
            'SS': [row['Total']],
            'Estres': [0],
            'IE Autopercibida': [0],
            'IE Baron Ice': [0]
        })
        check_total_copy_2 = pd.concat([check_total_copy_2, new_row], ignore_index=True)

# Agregar datos de estres_2
for _, row in estres_2.iterrows():
    if row['Nombre completo'] in check_total_copy_2['Usuarios'].values:
        check_total_copy_2.loc[check_total_copy_2['Usuarios'] == row['Nombre completo'], 'Estres'] = row['Total']
    else:
        new_row = pd.DataFrame({
            'Usuarios': [row['Nombre completo']],
            'SS': [0],
            'Estres': [row['Total']],
            'IE Autopercibida': [0],
            'IE Baron Ice': [0]
        })
        check_total_copy_2 = pd.concat([check_total_copy_2, new_row], ignore_index=True)

# Agregar datos de ie_baron_ice_2
for _, row in ie_baron_ice_2.iterrows():
    if row['Nombre completo'] in check_total_copy_2['Usuarios'].values:
        check_total_copy_2.loc[check_total_copy_2['Usuarios'] == row['Nombre completo'], 'IE Baron Ice'] = row['Total']
    else:
        new_row = pd.DataFrame({
            'Usuarios': [row['Nombre completo']],
            'SS': [0],
            'Estres': [0],
            'IE Autopercibida': [0],
            'IE Baron Ice': [row['Total']]
        })
        check_total_copy_2 = pd.concat([check_total_copy_2, new_row], ignore_index=True)

# Eliminar filas específicas (si es necesario)
filas_a_eliminar_2 = [17, 18, 14, 12, 19]
check_total_copy_2 = check_total_copy_2.drop(filas_a_eliminar_2)

# Reemplazar ceros por asteriscos
check_total_copy_2.replace(0, '*', inplace=True)

# exportar 
check_total_copy_2.to_csv('/workspaces/dashboard-focalization/data/check_total.csv', index=False)