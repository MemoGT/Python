import pandas as pd
from pandas import DataFrame, read_excel, merge

df1 = read_excel('C:/Users/A462138/Documents/archivo.xlsx', sheet_name='Tabla1')
df2 = read_excel('C:/Users/A462138/Documents/archivo.xlsx', sheet_name='Tabla2')

df1 = df1.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
df2 = df2.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

#df2 = df2.filter(items=['Nombre','Profesion'])
df3 = df1.merge(df2, on='Nombre', how='left')

with pd.ExcelWriter('C:/Users/A462138/Documents/archivo.xlsx', engine='openpyxl', mode='a') as writer:
    #df1.to_excel(writer, sheet_name='Tabla_1', index=False)
    #df2.to_excel(writer, sheet_name='Tabla_2', index=False)
    df3.to_excel(writer, sheet_name='Tabla3', index=False)

"""
Este script utiliza la librería Pandas para manipular datos en formato Excel.
Importa las librerías necesarias: Pandas y algunas funciones específicas de esta librería.
Lee dos hojas de cálculo en un archivo llamado "archivo.xlsx" y las almacena en dos variables diferentes: df1 y df2.
Aplica una función lambda a cada una de las dos variables anteriores para convertir todos los valores de tipo "objeto" a minúsculas.
Utiliza el método merge() para unir los datos de df1 y df2 en una nueva variable llamada df3, utilizando la columna "Nombre" como clave de unión y utilizando una unión tipo "left" (es decir, incluye todos los registros de la tabla de la izquierda, y los registros de la tabla de la derecha que coincidan con los de la izquierda).
Utiliza un bloque with para abrir un archivo de excel en modo escritura, y escribe el contenido de df3 en una nueva hoja llamada "Tabla3".
"""



