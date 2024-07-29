
# your code here

import streamlit as st
import numpy as np 
import pandas as pd
from pickle import load

# Cargar el modelo
# @st.cache(persist=True, allow_output_mutation=True)
def load_model():
    with open("linear_regression.pkl", "rb") as file:
        model = load(file)
    return model

model = load_model()

st.write(""" 
# Predicción de la Prima del Seguro Médico
Esta aplicación predice la prima del seguro médico basada en diversos parámetros.
""")

st.sidebar.header("Parámetros de entrada para predecir la prima del seguro médico")

def user_inputs():
    bmi = st.sidebar.number_input("Índice de Masa Corporal (BMI)", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
    children = st.sidebar.number_input("Cantidad de Hijos", min_value=0, max_value=10, value=0, step=1)
    sex = st.sidebar.selectbox("Sexo", ("Hombre", "Mujer"))
    smoker = st.sidebar.selectbox("¿Fumador?", ("Sí", "No"))
    
    sex_n = 1 if sex == "Hombre" else 0
    smoker_n = 1 if smoker == "Sí" else 0
    
    # Convertir las entradas a un DataFrame
    data = {
        'bmi': bmi,
        'children': children,
        'sex_n': sex_n,
        'smoker_n': smoker_n
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Obtener inputs de entradad el user
input_df = user_inputs()

# inputs de entradad el user
st.subheader('Parámetros de entrada')
st.write(input_df)

# Ahroa tiens que predecir
prediction = model.predict(input_df)

# Results -- que mas pues
st.subheader('Resultado de la Predicción')
st.write(f'La prima del seguro médico es: ${prediction[0]:.2f}')