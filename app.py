import pandas as pd 
import streamlit as st 
import plotly_express as px

#Se da un encabezado a la app
st.header("Análisis de venta de coches")

#Ahora leemos los datos contenidos en el archivo vehicles_us.csv
car_data = pd.read_csv('vehicles_us.csv') 

#Ahora creamos un botón para construir el histograma
hist_button = st.button('Construir histograma') 
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         # crear un histograma
        fig = px.histogram(car_data, x="odometer")
         # mostrar un gráfico Plotly interactivo    
        st.plotly_chart(fig, use_container_width=True)

#Ahora creamos un botón para crear el gráfico de dispersión 
scatter_button=st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write('Creación de un gráfico de dispersión: odómetro vs precio')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)