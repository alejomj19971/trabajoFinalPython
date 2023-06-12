import pandas as pd
import numpy as np
import streamlit as st

# Crear datos de ejemplo
marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai']
modelos = ['Camry', 'Civic', 'F-150', 'Silverado', 'Altima', 'X5', 'C-Class', 'A4', 'Jetta', 'Elantra']
anios = [2018, 2020, 2019, 2017, 2016, 2021, 2018, 2020, 2019, 2017]
precios = np.random.randint(15000, 50000, 10)
df_autos = pd.DataFrame({'marca': marcas, 'modelo': modelos, 'anio': anios, 'precio': precios})

# Mostrar el DataFrame
st.write(df_autos)
st.header('Todas las filas de marca')
st.write(df_autos.loc[:,'marca'])    
st.divider()
    
st.header('Vehículos con Precio mayor a 40000')                      
st.write(df_autos.loc[df_autos['precio'] > 40000, :])
st.divider()
st.header('Filas con la marca BMW')
st.write(df_autos.loc[df_autos['marca'] =="BMW", :])
st.divider()


st.header('Vehículos de marca Toyota y con precio menor a 20000')
st.write(df_autos.loc[(df_autos['marca']=="Toyota")&(df_autos['precio']<20000), :])
st.divider()

st.header('Vehículos del Año 2019')
st.write(df_autos.loc[(df_autos['anio']==2019), :])
st.divider()

st.header('Vehículos del Año 2016 o anteriores a ese año')
st.write(df_autos.loc[(df_autos['anio']<=2016), :])
st.divider()

st.header('Vehículos de la marca Honda Civic')
st.write(df_autos.loc[(df_autos['marca']=="Honda")&(df_autos['modelo']=="Civic"), :])
st.divider()


st.header('Vehículos con precio entre 25000 y 30000')
st.write(df_autos.loc[(df_autos['precio']>=25000)&(df_autos['precio']<=35000), :])
st.divider()




st.header('Vehículso de precio mayor a 30000 y de marca C-Class')
st.write(df_autos.loc[(df_autos['precio']>30000)&(df_autos['modelo']=="C-Class"), :])
st.divider()

st.header('Vehículos de marca VolksWagen y que no sean del modelo Jetta')
st.write(df_autos.loc[(df_autos['marca']=="Volkswagen")&(df_autos['modelo']!="Jetta"), :])
st.divider()


st.header('Primeros cinco fabricantes')
st.write(df_autos.iloc[0:5,0])
st.divider()


st.header('Ultimos cinco fabricantes')
st.write(df_autos.iloc[5:,0])
st.divider()


st.header('Primera columna de todas las filas')
st.write(df_autos.iloc[:,0])
st.divider()

st.header('Valor de la primera fila y la primera columna')
st.write(df_autos.iloc[0,0])
st.divider()


st.header('Filas Pares')
st.write(df_autos.iloc[::2, :])
st.divider()


st.header('Impares mayor a 25000')
st.write(df_autos.iloc[1::2,:][df_autos['precio']>25000])
st.divider()

st.header('Ford y modelo F-150')
st.write(df_autos.iloc[:,:][df_autos['marca']=="Ford"][df_autos['modelo']=='F-150'])
st.divider()

#2018 y mayor a 20000
st.header('Vehículos del año 2018 precio mayor a 20000')
st.write(df_autos.iloc[:,:][df_autos['precio']>20000][df_autos['anio']==2018])
st.divider()

#Mayor a 30k y toyota
st.header('Vehículos de marca Toyota precio mayor a 30000')
st.write(df_autos.iloc[:,:][df_autos['precio']>30000][df_autos['marca']=='Toyota'])
st.divider()


#Honda y No civic
st.header('Vehículos de marca Honda que no sean del modelo Civic')
st.write(df_autos.iloc[:,:][df_autos['marca']=='Honda'][df_autos['modelo']!='Civic'])
st.divider()
