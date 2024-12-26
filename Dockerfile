FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
#EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "streamlit_app.py"]