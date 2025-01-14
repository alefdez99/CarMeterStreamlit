FROM python:3.12

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema, incluyendo libGL y Tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requisitos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Comando para ejecutar la aplicación
ENTRYPOINT ["streamlit", "run", "streamlit_app.py"]
