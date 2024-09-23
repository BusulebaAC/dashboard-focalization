# -*- coding: utf-8 -*-
"""focalizacion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XnnLsd1WWCPXzDxup3lK4vXiBNV4sfQy
"""

import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR-r1GK0Jrbdw9RZCOezUEhdMvwpweLbhxsibsP-oNXBG6eScvlrsxGt0icaMHfzPNzcQslQxxypA3Y/pub?gid=736112076&single=true&output=csv'
focalizacion = pd.read_csv (url)

focalizacion = focalizacion.drop(focalizacion.columns[[0, 1]], axis=1)
focalizacion ['Ingresa tu nombre completo'] = focalizacion ['Ingresa tu nombre completo'].str.lower()

reemplazo = {
    'Nunca' : 0,
    'A veces' : 1,
    'Siempre' : 2
}

reemplazo_inverso = {
    'Nunca': 2,
    'A veces': 1,
    'Siempre': 0
}

def reemplazos(df, columnas_invertidas):
    for i in df.columns:
        if i in columnas_invertidas:
            # Reemplazo inverso para columnas especificadas
            df[i] = df[i].replace(reemplazo_inverso)
        else:
            # Reemplazo estándar
            df[i] = df[i].replace(reemplazo)
    return df

columnas_invertidas = [8, 12, 27, 57, 58]

focalizacion = reemplazos(focalizacion, columnas_invertidas)

focalizacion

# indices de potencial agresor
indices_agresor = [0, 1, 4, 6, 7, 11, 33, 34, 35, 2, 15, 32, 59, 43, 44, 49,
                   40, 41, 73, 19, 20, 50, 56, 62, 37, 55, 23, 70]

columnas_agresor= focalizacion.columns[indices_agresor]
focalizacion_sin_agresor = focalizacion.drop(columns=columnas_agresor)
focalizacion['Total Victima'] = focalizacion_sin_agresor.sum(axis=1)

# indices de potencial victima
indices_victima = [0, 3, 5, 9, 10, 12, 17, 8, 13, 14, 16, 29, 30, 31, 51, 57,
                   58, 42, 45, 46, 47, 48, 38, 72, 36, 53, 54, 63, 64, 25, 52,
                   65, 66, 18, 21, 22, 24, 26, 27, 28, 39, 60, 61, 67,
                   68, 69, 71]

columnas_victima= focalizacion.columns[indices_victima]
focalizacion_sin_victima = focalizacion.drop(columns=columnas_victima)
focalizacion['Total Agresor'] = focalizacion_sin_victima.sum(axis=1)

focalizacion

def condicion_riesgo_agresor(x):
    if x <= 5:
        return 'Sin riesgo'
    elif x <= 21:
        return 'Riesgo bajo'
    elif x <= 37:
        return 'Riesgo medio'
    else:
        return 'Riesgo alto'

def condicion_riesgo_victima(x):
    if x <= 8:
        return 'Sin riesgo'
    elif x <= 36:
        return 'Riesgo bajo'
    elif x <= 64:
        return 'Riesgo medio'
    else:
        return 'Riesgo alto'


focalizacion['Nivel de riesgo Victima'] = focalizacion['Total Victima'].apply(lambda x: condicion_riesgo_victima(x))
focalizacion['Nivel de riesgo Agresor'] = focalizacion['Total Agresor'].apply(lambda x: condicion_riesgo_agresor(x))

focalizacion

focalizacion.to_csv('focalizacion.csv', index=False)

columnas_resultados = ['Ingresa tu nombre completo', 'Total Victima',
                       'Total Agresor', 'Nivel de riesgo Victima',
                       'Nivel de riesgo Agresor']

focalizacion_resultados = focalizacion[columnas_resultados]

focalizacion_resultados = focalizacion_resultados.rename(columns={'Ingresa tu nombre completo': 'Nombre'})

focalizacion_resultados

# focalizacion.to_excel('focalizacion.xlsx', index=False)
# focalizacion_resultados.to_csv('data/focalizacion_resultados.csv', index=False)
focalizacion_resultados.to_pickle('../data/focalizacion_resultados.pkl')