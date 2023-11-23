#Proyecto de la Finca Chelsea
#Crear gráficos que muestren las relaciones entre las variables

#Importar librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importar los datos y convertirlos a DataFrames
#En este caso los datos están guardados en las carpetas: NodoAmbiente, NodoPH y NodoSuelo
#Los datos están en diferentes archivos por lo que se deben importar todos para poder hacer las relaciones


#Datos de NodoAmbiente: humedad
NA_H = pd.read_csv("/home/pi/AnalisisDatos/Chelsea/NodoAmbiente/humedad.csv", sep=';') #Se debe espicificar en donde está el archivo con los datos y se separa con ;
NA_H['DateTime'] = pd.to_datetime(NA_H['DateTime'], format='%Y-%m-%d %H:%M:%S') #Se asegura que la columna fecha tenga el formato adecuado
#Se debe cambiar las comas por puntos para convertir la columna/ a tipo decimal
NA_H['Humedad %'] = NA_H['Humedad %'].str.replace(',', '.')  
NA_H['Humedad %']=(NA_H['Humedad %'].astype(float))
#Buscamos valores nulos
print("Números de valores nulos: ", NA_H.isnull().sum())
print(NA_H.info())

#Datos de NodoAmbiente: temperatura
NA_T = pd.read_csv("/home/pi/AnalisisDatos/Chelsea/NodoAmbiente/temperatura.csv", sep=';')
NA_T['DateTime'] = pd.to_datetime(NA_T['DateTime'], format='%Y-%m-%d %H:%M:%S')
NA_T['Temperatura °C'] = NA_T['Temperatura °C'].str.replace(',', '.')  
NA_T['Temperatura °C']=(NA_T['Temperatura °C'].astype(float))
#Buscamos valores nulos
print("Números de valores nulos: ", NA_T.isnull().sum())
print(NA_T.info())

#Datos de NodoPH: ph
N_PH = pd.read_csv("/home/pi/AnalisisDatos/Chelsea/NodoPH/ph.csv", sep=';')
N_PH['DateTime'] = pd.to_datetime(N_PH['DateTime'], format='%Y-%m-%d %H:%M:%S')
N_PH['PH Suelo PH'] = N_PH['PH Suelo PH'].str.replace(',', '.')  
N_PH['PH Suelo PH']=(N_PH['PH Suelo PH'].astype(float))
#Buscamos valores nulos
print("Números de valores nulos: ", N_PH.isnull().sum())
print(N_PH.info())


#Datos de NodoSuelo: ConductividadSuelo
NS_C = pd.read_csv("/home/pi/AnalisisDatos/Chelsea/NodoSuelo/conductividadSuelo.csv", sep=';')
NS_C['DateTime'] = pd.to_datetime(NS_C['DateTime'], format='%Y-%m-%d %H:%M:%S')
#En este DataFrame no hay que cambiar las , por . porque el valor de conductividad viene en números enteros
print("Números de valores nulos: ", NS_C.isnull().sum())
print(NS_C.info())

#Datos de NodoSuelo: humedadSuelo
NS_H = pd.read_csv("/home/pi/AnalisisDatos/Chelsea/NodoSuelo/humedadSuelo.csv", sep=';')
NS_H['DateTime'] = pd.to_datetime(NS_H['DateTime'], format='%Y-%m-%d %H:%M:%S')
NS_H['Humedad Suelo %'] = NS_H['Humedad Suelo %'].str.replace(',', '.')  
NS_H['Humedad Suelo %']=(NS_H['Humedad Suelo %'].astype(float))
#Buscamos valores nulos
print("Números de valores nulos: ", NS_H.isnull().sum())
print(NS_H.info())

#Datos de NodoSuelo: temperaturaSuelo
NS_T = pd.read_csv("/home/pi/AnalisisDatos/Chelsea/NodoSuelo/temperaturaSuelo.csv", sep=';')
NS_T['DateTime'] = pd.to_datetime(NS_T['DateTime'], format='%Y-%m-%d %H:%M:%S')
NS_T['Temperatura Suelo °C'] = NS_T['Temperatura Suelo °C'].str.replace(',', '.')  
NS_T['Temperatura Suelo °C']=(NS_T['Temperatura Suelo °C'].astype(float))
#Buscamos valores nulos
print("Números de valores nulos: ", NS_H.isnull().sum())
print(NS_H.info())

############

#Descripción por mes
#Lo siguiente descargará una imagen de una descripción por cada DAtaFrame separado por mes

#Descripcion Humedad_Suelo
desc_h=NS_H.groupby(NS_H['DateTime'].dt.to_period("M"))['Humedad Suelo %'].describe().round(2)
print(desc_h)
fig, ax = plt.subplots(figsize=(12, 2))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=desc_h.values, colLabels=desc_h.columns, rowLabels=desc_h.index, cellLoc = 'center', loc='center')
plt.savefig('desc_hs.png')

#Descripcion Temperatura_Suelo
desc_ts=NS_T.groupby(NS_T['DateTime'].dt.to_period("M"))['Temperatura Suelo °C'].describe().round(2)
print(desc_ts)
fig, ax = plt.subplots(figsize=(12, 2))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=desc_ts.values, colLabels=desc_ts.columns, rowLabels=desc_ts.index, cellLoc = 'center', loc='center')
plt.savefig('desc_ts.png')

#Descripcion Conductividad_Suelo
desc_c=NS_C.groupby(NS_C['DateTime'].dt.to_period("M"))['Conductividad Suelo uS/cm'].describe().round(2)
print(desc_c)#
fig, ax = plt.subplots(figsize=(12, 2))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=desc_c.values, colLabels=desc_c.columns, rowLabels=desc_c.index, cellLoc = 'center', loc='center')
plt.savefig('desc_cs.png')


#Descripcion pH
desc_ph=N_PH.groupby(N_PH['DateTime'].dt.to_period("M"))['PH Suelo PH'].describe().round(2)
print(desc_ph)
fig, ax = plt.subplots(figsize=(12, 2))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=desc_ph.values, colLabels=desc_ph.columns, rowLabels=desc_ph.index, cellLoc = 'center', loc='center')
plt.savefig('desc_ph.png')

#Descripcion Humedad_Ambiente
desc_ha=NA_H.groupby(NA_H['DateTime'].dt.to_period("M"))['Humedad %'].describe().round(2)
print(desc_ha)
fig, ax = plt.subplots(figsize=(12, 2))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=desc_ha.values, colLabels=desc_ha.columns, rowLabels=desc_ha.index, cellLoc = 'center', loc='center')
plt.savefig('desc_ha.png')

#Descripcion Temperatura_Ambiente
desc_ta=NA_T.groupby(NA_T['DateTime'].dt.to_period("M"))['Temperatura °C'].describe().round(2)
print(desc_ta)
fig, ax = plt.subplots(figsize=(12, 2))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=desc_ta.values, colLabels=desc_ta.columns, rowLabels=desc_ta.index, cellLoc = 'center', loc='center')
plt.savefig('desc_ta.png')

############


#
#
##
###
####
#####
######
#######
########
#########
########
#######
######
#####
####
###
##
#



#..........................................#
#..........................................#
#..........................................#
# - - - - - - - - GRÁFICOS - - - - - - -   #
#..........................................#
#..........................................#
#..........................................#


# # # GRÁFICOS DE HUMEDAD AMBIENTE # # #

#GRÁFICO DE LÍNEAS#

plt.figure(figsize=(10, 6))
for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-octubre)
    df_mes = NA_H[NA_H['DateTime'].dt.month == mes]
    plt.plot(df_mes['DateTime'], df_mes['Humedad %'], label=f'Mes {mes}')
plt.xlabel('FECHA')
plt.ylabel('Humedad')
plt.title('Relación de humedad del ambiente en los ultimos 7 meses')
plt.legend()
plt.grid(True)
plt.show()

#Histograma de Humedad del Ambiente, ordenado por meses

plt.figure(figsize=(12, 8))
for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-setiembre)
    df_mes = NA_H[NA_H['DateTime'].dt.month == mes]
    plt.hist(df_mes['Humedad %'], bins=20, alpha=0.7, label= f'Mes {mes}', density=True)#
plt.xlabel('NA_Humedad')
plt.ylabel('Frecuencia')
plt.title('Histograma de Humedad del ambiente')
plt.legend()
plt.grid(True)
plt.show()

#Boxplot comparativo de NA_Humedad (Horizontal)

plt.figure(figsize=(10,8))
sns.boxplot(x=NA_H['Humedad %'], y=NA_H['DateTime'].dt.strftime('%B'), orient='h')
plt.xlabel('Humedad')
plt.ylabel('Mes')
plt.title('Boxplot de humedad del ambiente')
plt.grid(True)
plt.show()


# # # GRÁFICOS HUMEDAD DEL SUELO # # #

#GRÁFICO DE LÍNEAS
for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-octubre)
    df_mes = NS_H[NS_H['DateTime'].dt.month == mes]
    plt.plot(df_mes['DateTime'], df_mes['Humedad Suelo %'], label=f'Mes {mes}')#

plt.xlabel('FECHA')
plt.ylabel('Humedad')
plt.title('Relación de humedad del suelo en los ultimos 7 meses')
plt.legend()
plt.grid(True)
plt.show()


#Histograma de Humedad del Suelo, ordenado por meses

plt.figure(figsize=(12, 8))

for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-setiembre)
    df_mes = NS_H[NS_H['DateTime'].dt.month == mes]
    plt.hist(df_mes['Humedad Suelo %'], bins=10, alpha=0.7, label= f'Mes {mes}', density=True)

plt.xlabel('NS_Humedad')
plt.ylabel('Frecuencia')
plt.title('Histograma de Humedad del suelo')
plt.legend()
plt.grid(True)
plt.show()

#Boxplot comparativo de NS_Humedad (Horizontal)

plt.figure(figsize=(10,8))
sns.boxplot(x=NS_H['Humedad Suelo %'], y=NS_H['DateTime'].dt.strftime('%B'), orient='h')
plt.xlabel('Humedad')
plt.ylabel('Mes')
plt.title('Boxplot de humedad del suelo')
plt.grid(True)
plt.show()


# # # Graficos de Temperatura SUELO # # #

#GRÁFICO DE LÍNEAS#

plt.figure(figsize=(10, 6))

for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-octubre)
    df_mes = NS_T[NS_T['DateTime'].dt.month == mes]
    plt.plot(df_mes['DateTime'], df_mes['Temperatura Suelo °C'], label=f'Mes {mes}')

plt.xlabel('FECHA')
plt.ylabel('Temperatura')
plt.title('Relación de la temperatura del suelo en los ultimos 7 meses')
plt.legend()
plt.grid(True)
plt.show()

#Histogramas de TEMPERATURA SUELO

plt.figure(figsize=(12, 8))
for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-setiembre)
    df_mes = NS_T[NS_T['DateTime'].dt.month == mes]
    plt.hist(df_mes['Temperatura Suelo °C'], bins=20, alpha=0.7, label= f'Mes {mes}', density=True)
plt.xlabel('Temperatura')
plt.ylabel('Frecuencia')
plt.title('Histograma de Temperatura del Suelo')
plt.legend()
plt.grid(True)
plt.show()

#BOXPLOT DE TEMPERATURA SUELO

plt.figure(figsize=(10,8))
sns.boxplot(x=NS_T['Temperatura Suelo °C'], y=NS_T['DateTime'].dt.strftime('%B'), orient='h')
plt.xlabel('Temperatura')
plt.ylabel('Mes')
plt.title('Boxplot de Temperatura del SUELO')
plt.grid(True)
plt.show()


# # # Graficos de Temperatura AMBIENTE # # #

#GRÁFICO DE LÍNEAS#

plt.figure(figsize=(10, 6))

for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-octubre)
    df_mes = NA_T[NA_T['DateTime'].dt.month == mes]
    plt.plot(df_mes['DateTime'], df_mes['Temperatura °C'], label=f'Mes {mes}')

plt.xlabel('FECHA')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura del ambiente en los ultimos 7 meses')
plt.legend()
plt.grid(True)
plt.show()

#Histogramas de TEMPERATURA AMBIENTE

plt.figure(figsize=(12, 8))

for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-setiembre)
    df_mes = NA_T[NA_T['DateTime'].dt.month == mes]
    plt.hist(df_mes['Temperatura °C'], bins=20, alpha=0.7, label= f'Mes {mes}', density=True)

plt.xlabel('Temperatura')
plt.ylabel('Frecuencia')
plt.title('Histograma de Temperatura Ambiente')
plt.legend()
plt.grid(True)
plt.show()

#BOXPLOT DE TEMPERATURA AMBIENTE

plt.figure(figsize=(10,8))
sns.boxplot(x=NA_T['Temperatura °C'], y=NA_T['DateTime'].dt.strftime('%B'), orient='h')
plt.xlabel('Temperatura')
plt.ylabel('Mes')
plt.title('Boxplot de Temperatura Ambiente')
plt.grid(True)
plt.show()



# # # GRAFICOS DE PH # # #

#Gráfico de líneas

plt.figure(figsize=(10, 6))
for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-octubre)
    df_mes = N_PH[N_PH['DateTime'].dt.month == mes]
    plt.plot(df_mes['DateTime'], df_mes['PH Suelo PH'], label=f'Mes {mes}')
plt.xlabel('FECHA')
plt.ylabel('pH')
plt.title('Relación de pH en los ultimos 7 meses')
plt.legend()
plt.grid(True)
plt.show()

#Histograma de pH

plt.figure(figsize=(12, 8))
for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-setiembre)
    df_mes = N_PH[N_PH['DateTime'].dt.month == mes]
    plt.hist(df_mes['PH Suelo PH'], bins=20, alpha=0.7, label= f'Mes {mes}', density=True)
plt.xlabel('pH')
plt.ylabel('Frecuencia')
plt.title('Histograma de pH')
plt.legend()
plt.grid(True)
plt.show()

#Boxplot de pH

plt.figure(figsize=(10,8))
sns.boxplot(x=N_PH['PH Suelo PH'], y=N_PH['DateTime'].dt.strftime('%B'), orient='h')
plt.xlabel('pH')
plt.ylabel('Mes')
plt.title('Boxplot de pH')
plt.grid(True)
plt.show()

###GRAFICOS DE CONDUCTIVIDAD###

#Grafico de LÍNEAS

plt.figure(figsize=(10, 6))
for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-octubre)
    df_mes = NS_C[NS_C['DateTime'].dt.month == mes]
    plt.plot(df_mes['DateTime'], df_mes['Conductividad Suelo uS/cm'], label=f'Mes {mes}')
plt.xlabel('FECHA')
plt.ylabel('CONDUCTIVIDAD')
plt.title('La conductividad del suelo en los ultimos 7 meses')
plt.legend()
plt.grid(True)
plt.show()

##Histograma de conductividad

plt.figure(figsize=(12, 8))
for mes in range(4, 11):   #El rango de meses que se quieren separar(abril-setiembre)
    df_mes = NS_C[NS_C['DateTime'].dt.month == mes]
    plt.hist(df_mes['Conductividad Suelo uS/cm'], bins=20, alpha=0.7, label= f'Mes {mes}', density=True)
plt.xlabel('Conductividad')
plt.ylabel('Frecuencia')
plt.title('Histograma de Conductividad')
plt.legend()
plt.grid(True)
plt.show()


#Boxplot

plt.figure(figsize=(10,8))
sns.boxplot(x=NS_C['Conductividad Suelo uS/cm'], y=NS_C['DateTime'].dt.strftime('%B'), orient='h')
plt.xlabel('Conductividad')
plt.ylabel('Mes')
plt.title('Boxplot de Conductividad')
plt.grid(True)
plt.show()

######################################################################
#heatmap
#Correlación

#Un valor cercano a 1 o -1 indica una correlación fuerte, 
# mientras que un valor cercano a 0 indica una correlación débil. 
# Un valor positivo indica una correlación directa (cuando uno aumenta, el otro también lo hace), 
# mientras que un valor negativo indica una correlación inversa (cuando uno aumenta, el otro disminuye).

matriz_correlacion = pd.concat([NA_T['Temperatura °C'], NA_H['Humedad %'], NS_H['Humedad Suelo %'], NS_T['Temperatura Suelo °C'], NS_C['Conductividad Suelo uS/cm']],axis=1).corr()
sns.set(style="whitegrid")
plt.figure(figsize=(12, 10))
sns.heatmap(matriz_correlacion, linewidths=.5, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size":10})
plt.title("Mapa de calor de correlación")
plt.xticks(rotation=90)
plt.yticks(rotation=45)
plt.gcf().subplots_adjust(bottom=0.25, left=0.25) # Ajusta el margen de la figura
plt.show()



#GRÁFICOS DE RELACIONES
#Los siguiente gráficos explicarán las relaciones entre valores de diferentes DataFrames

#Grafico de relacion entre humedad y temperatura del suelo 
plt.figure(figsize=(10,6))
sns.regplot(x=NS_T['Temperatura Suelo °C'], y=NS_H['Humedad Suelo %'], line_kws={"color" : "red"})
plt.title('Relación entre temperatura y humedad del suelo')
plt.show()

#Grafico de relacion entre humedad y temperatura del ambiente
plt.figure(figsize=(10,6))
sns.regplot(x=NA_T['Temperatura °C'], y=NA_H['Humedad %'], line_kws={"color" : "red"})
plt.title('Relación entre temperatura y humedad del ambiente')
plt.show()

#Grafico de relacion entre humedad y conductividad del suelo
plt.figure(figsize=(10,6))
sns.regplot(x=NS_H['Humedad Suelo %'], y=NS_C['Conductividad Suelo uS/cm'], line_kws={"color" : "red"})
plt.title("Relación entre la conductividad y la humedad del suelo")
plt.show()



#
#
##
###
####
#####
######
#######
########
#########
########
#######
######
#####
####
###
##
#

#Descripción por mes
#Lo siguiente descargará una imagen por cada descripción

#Descripcion Humedad_Suelo
#desc_h=NS_H.groupby(NS_H['DateTime'].dt.to_period("M"))['Humedad Suelo %'].describe().round(2)
#print(desc_h)
#fig, ax = plt.subplots(figsize=(12, 2))
#ax.axis('tight')
#ax.axis('off')
#ax.table(cellText=desc_h.values, colLabels=desc_h.columns, rowLabels=desc_h.index, cellLoc = 'center', loc='center')
#plt.savefig('desc_h.png')

#Descripcion Humedad_Suelo
#desc_ts=NS_T.groupby(NS_T['DateTime'].dt.to_period("M"))['Temperatura Suelo °C'].describe().round(2)
#print(desc_ts)
#fig, ax = plt.subplots(figsize=(12, 2))
#ax.axis('tight')
#ax.axis('off')
#ax.table(cellText=desc_ts.values, colLabels=desc_ts.columns, rowLabels=desc_ts.index, cellLoc = 'center', loc='center')
#plt.savefig('desc_ts.png')

#Descripcion Conductividad_Suelo
#desc_c=NS_C.groupby(NS_C['DateTime'].dt.to_period("M"))['Conductividad Suelo uS/cm'].describe().round(2)
#print(desc_c)#
#fig, ax = plt.subplots(figsize=(12, 2))
#ax.axis('tight')
#ax.axis('off')
#ax.table(cellText=desc_c.values, colLabels=desc_c.columns, rowLabels=desc_c.index, cellLoc = 'center', loc='center')
#plt.savefig('desc_c.png')


#Descripcion pH
#desc_ph=N_PH.groupby(N_PH['DateTime'].dt.to_period("M"))['PH Suelo PH'].describe().round(2)
#print(desc_ph)
#fig, ax = plt.subplots(figsize=(12, 2))
#ax.axis('tight')
#ax.axis('off')
#ax.table(cellText=desc_ph.values, colLabels=desc_ph.columns, rowLabels=desc_ph.index, cellLoc = 'center', loc='center')
#plt.savefig('desc_ph.png')

#Descripcion Humedad_Ambiente
#esc_ha=NA_H.groupby(NA_H['DateTime'].dt.to_period("M"))['Humedad %'].describe().round(2)
#print(desc_ha)
#fig, ax = plt.subplots(figsize=(12, 2))
#ax.axis('tight')
#ax.axis('off')
#ax.table(cellText=desc_ha.values, colLabels=desc_ha.columns, rowLabels=desc_ha.index, cellLoc = 'center', loc='center')
#plt.savefig('desc_ha.png')

#Descripcion Temperatura_Ambiente
#desc_ta=NA_T.groupby(NA_T['DateTime'].dt.to_period("M"))['Temperatura °C'].describe().round(2)
#print(desc_ta)
#fig, ax = plt.subplots(figsize=(12, 2))
#ax.axis('tight')
#ax.axis('off')
#ax.table(cellText=desc_ta.values, colLabels=desc_ta.columns, rowLabels=desc_ta.index, cellLoc = 'center', loc='center')
#plt.savefig('desc_ta.png')


#heatmap

#matriz_correlacion = pd.concat([NA_T['Temperatura °C'], NA_H['Humedad %'], NS_H['Humedad Suelo %'], NS_T['Temperatura Suelo °C'], NS_C['Conductividad Suelo uS/cm']],axis=1).corr()
#sns.set(style="whitegrid")
#plt.figure(figsize=(12, 10))
#sns.heatmap(matriz_correlacion, linewidths=.5, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size":10})
#plt.title("Mapa de calor de correlación")
#plt.xticks(rotation=90)
#plt.yticks(rotation=45)
#plt.gcf().subplots_adjust(bottom=0.25, left=0.25) # Ajusta el margen de la figura
#plt.show()

#matriz_correlacion = pd.concat([NA_T['Temperatura °C'], NA_H['Humedad %'], NS_H['Humedad Suelo %'], NS_T['Temperatura Suelo °C'], NS_C['Conductividad Suelo uS/cm']],axis=1).corr()
#sns.set(style="whitegrid")
#plt.figure(figsize=(12, 10))
#sns.heatmap(matriz_correlacion, linewidths=.5, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size":10})
#plt.title("Mapa de calor de correlación")
#plt.xticks(rotation=90)
#plt.yticks(rotation=45)
#plt.gcf().subplots_adjust(bottom=0.25, left=0.25) # Ajusta el margen de la figura
#plt.show()
