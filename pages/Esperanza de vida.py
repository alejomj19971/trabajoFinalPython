import streamlit as st
import pandas as pd
import numpy as np


#Title sirve para mostrar un titulo con un texto como parámetro
st.title("Esperanza de Vida (2000-2015) ")
st.header("Este dataset muestra la esperanza de vida en este rango de tiempo, teniendo en cuenta características como PIB,escolaridad,país,región,enfermedades,entre otros.")

# se lee el archivo en data,queda en un formato de texto compatible para crear un dataframe
data = pd.read_csv('aVida.csv')
df = pd.DataFrame(data)

st.write(df)
añoRenueva=2000
listaPromedioVida=[]
listaAños=[]

while(añoRenueva<2016):
    arreglo=df[df['Year']==añoRenueva]
    promedio=arreglo.loc[:,['Life_expectancy']]
    promedio=promedio.mean()
    promedio=promedio.replace('Life_expectancy ','')
    promedio=float(promedio)
    listaPromedioVida.append(round(promedio,2))
    listaAños.append(añoRenueva)
    añoRenueva+=1

nuevoDataSet=pd.DataFrame({'Año':listaAños,'Esperanza de Vida Promedio':listaPromedioVida})

nuevoDataSet.set_index('Año', inplace=True)
st.title("Esperanza de Vida Promedio (2000-2015) ")
# Creamos un gráfico de línea con las ventas de los vehículos por año
st.line_chart(nuevoDataSet[['Esperanza de Vida Promedio']])


st.title("Esperanza de Vida por Región y Año" )

region = st.selectbox('REGION',(df["Region"].sort_values(ascending=True).unique()))
año = st.selectbox('AÑO',(df["Year"].sort_values(ascending=True).unique()))  
#filtroBarras = (df['Country'] == pais)&(df['Year']==año)
filtroBarras = (df['Region'] == region)&(df['Year']==año)
#"Filtra por valores en fila y columna"
df_filtrado = df.loc[filtroBarras] 
#"Filtra las columnas"
df_filtrado = df_filtrado.loc[:,['Country','Life_expectancy']]  
st.bar_chart(df_filtrado.set_index('Country'))




st.title("Esperanza de Vida Países por Muerte de Infantes y Año" )
Muerte_de_Infantes = st.selectbox('MUERTE DE INFANTES MIN',(df["Infant_deaths"].sort_values(ascending=True).unique())) 
Muerte_de_Infantes2 = st.selectbox('MUERTE DE INFANTES MAX',(df["Infant_deaths"].sort_values(ascending=True).unique())) 
año2 = st.selectbox('AÑO  ',(df["Year"].sort_values(ascending=True).unique()))  
filtroBarras2 = (df['Infant_deaths']>=Muerte_de_Infantes) & (df['Infant_deaths']<=Muerte_de_Infantes2)& (df['Year']==año2)
df_filtrado2 = df.loc[filtroBarras2] 
df_filtrado2 = df_filtrado2.loc[:,['Country','Life_expectancy']]    
st.bar_chart(df_filtrado2.set_index('Country'))


st.title("Esperanza de Vida por PBI y Año" )
año2 = st.selectbox('AÑO ',(df["Year"].sort_values(ascending=True).unique()))  
pib = st.selectbox('PIB MIN',(df["GDP_per_capita"].sort_values(ascending=True).unique()))
pib2 = st.selectbox('PIB MAX',(df["GDP_per_capita"].sort_values(ascending=True).unique()))    
filtroBarras4 = (df['GDP_per_capita']>=pib)&(df['GDP_per_capita']<=pib2)&(df['Year']==año2)
df_filtrado4 = df.loc[filtroBarras4] 
df_filtrado4 = df_filtrado4.loc[:,['Country','Life_expectancy']]    
st.bar_chart(df_filtrado4.set_index('Country'))


