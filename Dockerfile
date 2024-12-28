FROM python:3.12

WORKDIR /app
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install -r requirements.txt
#EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "streamlit_app.py"]