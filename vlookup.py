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
    


