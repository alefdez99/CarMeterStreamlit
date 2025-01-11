![CarMeter](img/carmeter.png)

# CarMeter: Predicción de Precios de Vehículos Usados

CarMeter es una aplicación de aprendizaje automático diseñada para predecir con precisión el precio de venta de vehículos usados. Los usuarios pueden ingresar información clave sobre el vehículo, como la marca, el modelo, el año, el kilometraje, el tipo de combustible y la transmisión, y la aplicación proporcionará una estimación del precio basado en un modelo preentrenado.

## Características
- Predicción basada en características clave del vehículo.
- Fácil de usar con una interfaz web construida en Streamlit.
- Totalmente contenedorizada con Docker.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/carmeter.git
   cd carmeter

2. Construye la imagen Docker:
   docker build -t car_meter_streamlit .

3. Ejecuta el contenedor Docker:
   docker run -p 8501:8501 car_meter_streamlit

4. Abre tu navegador web y ve a http://localhost:8501 para acceder a la aplicación.

## Uso
* Sube una imagen de la matrícula del vehículo.
* Ingresa la información del vehículo en la barra lateral:
* Marca
* Modelo
* Año de Fabricación
* Kilómetros recorridos
* Capacidad del motor (en cc)
* Potencia máxima (en bhp)
* Consumo de combustible (km/l)
* Tipo de Combustible
* La aplicación mostrará una estimación del precio del vehículo basado en el modelo preentrenado.