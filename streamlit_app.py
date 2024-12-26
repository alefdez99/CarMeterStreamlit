import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Carga el modelo
model = load('carmeter_rf_model.joblib')

# Título y logo de la aplicación
st.image("img/carmeter.png", use_container_width=True)  # Se cambió a use_container_width
st.title("CarMeter")
st.markdown(
    """
    Bienvenido a **CarMeter**, la herramienta que te ayuda a predecir el precio de venta de vehículos usados 
    utilizando técnicas avanzadas de aprendizaje automático.
    """
)

# Mejorar la visualización con separadores y subtítulos
st.markdown("---")
st.subheader("Información del Vehículo")

# Diccionario para codificar tipos de combustible
fuel_encoding = {
    "Gasolina": "fuel_Petrol",
    "Diésel": "fuel_Diesel",
    "Híbrido": "fuel_Hybrid",
    "Eléctrico": "fuel_Electric",
    "Gasolina + Gas Natural (CNG)": "fuel_CNG + CNG",
    "Gasolina + GLP (LPG)": "fuel_Petrol + LPG",
}

# Diccionario para codificar transmisión
transmission_encoding = {
    "Manual": 0,
    "Automática": 1,
}

# Formulario de entrada
def user_input_features():
    st.sidebar.header("Entrada de datos")
    st.sidebar.markdown("Completa los detalles del vehículo para obtener el precio estimado.")

    brand = st.sidebar.text_input("Marca", "Toyota")
    model = st.sidebar.text_input("Modelo", "Corolla")
    year = st.sidebar.slider("Año de Fabricación", 2000, 2023, 2015)
    km_driven = st.sidebar.number_input("Kilómetros recorridos", 0, 300000, 50000)
    engine = st.sidebar.number_input("Capacidad del motor (en cc)", 800, 5000, 1500)
    max_power = st.sidebar.number_input("Potencia máxima (en bhp)", 50, 500, 100)
    mileage = st.sidebar.number_input("Consumo de combustible (km/l)", 5.0, 40.0, 15.0)
    fuel_type = st.sidebar.selectbox("Tipo de Combustible", list(fuel_encoding.keys()))
    transmission = st.sidebar.selectbox("Transmisión", list(transmission_encoding.keys()))
    owner_type = st.sidebar.selectbox("Número de propietarios anteriores", ["Primera mano", "Segunda mano", "Tercera mano o más"], index=0)

    # Codificar entradas
    data = {
        'year': year,
        'km_driven': km_driven,
        'engine': engine,
        'max_power': max_power,
        'mileage': mileage,
        'transmission_encoded': transmission_encoding[transmission],
        'owner_encoded': {"Primera mano": 0, "Segunda mano": 1, "Tercera mano o más": 2}[owner_type]
    }

    # Agregar columnas de tipo de combustible
    for fuel_col in fuel_encoding.values():
        data[fuel_col] = 1 if fuel_col == fuel_encoding[fuel_type] else 0

    # Agregar columnas de tipo de vendedor con valores predeterminados
    for seller_col in ['seller_Corporate', 'seller_Dealer', 'seller_Individual', 'seller_Trustmark Dealer']:
        data[seller_col] = 0  # Valor predeterminado: sin especificar vendedor

    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Mostrar datos de entrada procesados
st.markdown("---")
st.subheader("Datos Ingresados")
st.write(input_df)

# Predicción
st.markdown("---")
st.subheader("Resultado de la Predicción")
if st.button("Predecir"):
    # Alinear columnas con las del modelo entrenado
    expected_columns = [
        'year', 'km_driven', 'engine', 'max_power', 'mileage',
        'fuel_CNG + CNG', 'fuel_Diesel', 'fuel_Electric', 'fuel_Hybrid',
        'fuel_LPG', 'fuel_Petrol', 'fuel_Petrol + CNG', 'fuel_Petrol + LPG',
        'seller_Corporate', 'seller_Dealer', 'seller_Individual', 'seller_Trustmark Dealer',
        'transmission_encoded', 'owner_encoded'
    ]
    input_df = input_df.reindex(columns=expected_columns, fill_value=0)

    # Realizar predicción
    prediction = model.predict(input_df)
    st.success(f"El precio estimado de venta es: **{prediction[0]:,.2f}€**")

# Pie de página
st.markdown("---")
st.markdown("Desarrollo de Aplicación Web con Modelo Integrado - CarMeter")
