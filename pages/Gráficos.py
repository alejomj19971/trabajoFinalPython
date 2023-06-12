import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Algunos gráficos con Python y Streamlit')
# Creamos un DataFrame de ejemplo con información de vehículos

st.header('Ventas de Vehículos por Modelo y Año (Gráfico de Lineas)')

vehiculos_data = {
    'Modelo': ['Ford', 'Toyota', 'Honda', 'Chevrolet', 'Nissan', 'Kia'],
    'Ventas 2020': [100000, 90000, 80000, 70000, 60000, 50000],
    'Ventas 2021': [120000, 95000, 85000, 75000, 65000, 55000]
}
vehiculos_df = pd.DataFrame(vehiculos_data)

# Establecemos la columna 'Modelo' como índice del DataFrame
vehiculos_df.set_index('Modelo', inplace=True)

# Creamos un gráfico de línea con las ventas de los vehículos por año
st.line_chart(vehiculos_df[['Ventas 2020', 'Ventas 2021']])



st.header('Ingresos de Tienda por Trimestre (Gráfico de Areas)')
# Crear el DataFrame con los ingresos de tres tiendas en cuatro trimestres

data = {
    'Tienda': ['Tienda 1', 'Tienda 1', 'Tienda 1', 'Tienda 1', 'Tienda 2', 'Tienda 2', 'Tienda 2', 'Tienda 2', 'Tienda 3', 'Tienda 3', 'Tienda 3', 'Tienda 3'],
    'Trimestre': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
    'Ingresos': [100, 120, 110, 130, 80, 190, 100, 110, 270, 80, 85, 90]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame


# Graficar el DataFrame con un gráfico de área
df_pivot = df.pivot(index='Tienda', columns='Trimestre', values='Ingresos')
st.area_chart(df_pivot)



st.header('Cantidad de Animales (Gráfico de Barras)')
data = {
    'Tipo': ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Hamster'],
    'Cantidad': [50, 30, 20, 10, 5]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame


# Graficar el DataFrame con un gráfico de barras
st.bar_chart(df.set_index('Tipo'))

st.header('Cantidad de Insectos (Gráfico de Barras)')
# Datos de insectos
mosca = 100
hormiga = 50 
mariposa = 20
escarabajo = 30

# Categorías de insectos
insectos = ['Moscas', 'Hormigas', 'Mariposas', 'Escarabajos']

# Frecuencia de insectos
frecuencias = [mosca, hormiga, mariposa, escarabajo]

# Crear el gráfico 
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)  
ax.bar(insectos, frecuencias)

# Mostrar el gráfico  
st.pyplot(fig)
