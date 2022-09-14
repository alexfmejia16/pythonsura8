import pandas as pd

#CARGAR LOS DATOS 

dataFrame=pd.read_csv('./empleados.csv')
#print(dataFrame)

#Cargar todos los datos 

#print(dataFrame.to_string())

#Cargar los primero N registros de un banco de datos 

#print(dataFrame.head(20))

#Cargar los primeros 20 registros de un banco de datos 
#print(dataFrame.tail(20))

#Obtener informacion de los datos cargados 
#print(dataFrame.info())
#print.(dataFrame.describe())

# Acceder a datos o registros especificos 
#print(dataFrame["nombres"].head())
#print(dataFrame["salario".tail(20)])

#Acceder a registros por su indice
#print(dataFrame.iloc[20:30])
#print(dataFrame.loc[[10,20,30,40]])
'''
tabla=(dataFrame.loc[[1,5,10],["nombres"]])

html=tabla.to_html()
text_file=open("index.html","w")
text_file.write(html)
text_file.close()
'''

#filtros con dondiciones logicas 

print(dataFrame[(dataFrame["salario"]>5000000) & (dataFrame(dataFrame ["cargo"]=="analista2")])

