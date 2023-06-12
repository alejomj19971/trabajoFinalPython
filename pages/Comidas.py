
import streamlit as st
import pandas as pd 
import requests
import  json
import requests
from PIL import Image
from io import BytesIO



st.title("RECETAS DEL MUNDO")
st.header("Apunta los ID de las recetas que más te gusten y busca la receta al final de la página.")
# Hacer una solicitud GET al endpoint de la API APOD
response = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convertir la respuesta JSON en un diccionario Python
    data = response.json()
    categorias=[]
    listaObjetos=(data['categories'])
    for receta in listaObjetos:
        categorias.append({"categoria":receta['strCategory'].strip()})


    dfCategorias=pd.DataFrame(categorias)
 
else:
    print('Se produjo un error al realizar la solicitud:', response.status_code)



categoriasBox = st.selectbox('CATEGORIAS',(dfCategorias["categoria"].sort_values(ascending=True).unique()))

response2 = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={categoriasBox}')

if response2.status_code == 200:
    data2 = response2.json()
   

    comidas=[]
    listaObjetos2=(data2['meals'])
    for comida in listaObjetos2:
        comidas.append({"nombre":comida['strMeal'],
                        "imagen":comida['strMealThumb'],
                        "id":comida['idMeal'],
                        })


    dfComidas=pd.DataFrame(comidas)
    
 

else:
    print('Se produjo un error al realizar la solicitud:', response.status_code)

for comida in comidas:
    response = requests.get(comida['imagen'])
    img = Image.open(BytesIO(response.content))
    st.header('Nombre de la receta: '+comida['nombre'])
    st.header('Id la receta: '+comida['id'])
    st.image(img, caption=comida['nombre'])
    st.divider()
    


st.title('Luego de ver las recetas busca tu receta con detalle colocando el id')
IdBox = st.selectbox('ID DE RECETA',(dfComidas["id"].sort_values(ascending=True).unique()))
response3 = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={IdBox}')

if response3.status_code == 200:
    data3 = response3.json()


    comidasDetalle=[]
    listaObjetos3=(data3['meals'])
    for comida in listaObjetos3:
        comidasDetalle.append({
            "nombre":comida['strMeal'],
            "area":comida['strArea'],
            "categoria":comida['strCategory'],
            "imagen":comida['strMealThumb'],
            "video":comida['strYoutube'],
            "instrucciones":comida['strInstructions'],
            })


    dfComidasDetalle=pd.DataFrame(comidasDetalle)
 

 
    for comida in comidasDetalle:
        response = requests.get(comida['imagen'])
        img = Image.open(BytesIO(response.content))
        st.header('Nombre de la receta: '+comida['nombre'])
        st.image(img, caption=comida['nombre'])
        st.header('Tipo de Comida: '+comida['area'])
        st.header('Caregoria: '+comida['categoria'])
        st.write('Instrucciones: '+comida['instrucciones'])
        st.video(comida['video'])
        