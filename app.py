import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

cars_data = pd.read_csv('vehicles_us.csv')


# Título de la aplicación
st.title("Mi primera aplicación Web sobre el mejor Auto")

# Agregar un texto
st.write("¡Bienvenido a tu primera aplicación interactiva en Python!")

# Entrada de texto para el usuario
nombre = st.text_input("¿Cual es tu Nombre?")
edad = st.text_input("¿Cual es tu edad")

# Botón para saludar
if st.button("Saludar"):
    st.write(f"Hola, {nombre}!mi edad es {edad} años 🎉 Bienvenido.")


comparation = pd.DataFrame(np.random.randn(20, 3), columns=["price", "model", "cylinders"])

st.write("📊 Aquí tienes algunos datos aleatorios:")
st.dataframe(comparation)

st.write("📈 Gráfico de los datos:")
fig, ax = plt.subplots()
ax.plot(comparation)
st.pyplot(fig)

if st.button("grafico dispersion"):
    st.write('Diagrama de dispersion')
    fig = px.scatter(cars_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)



