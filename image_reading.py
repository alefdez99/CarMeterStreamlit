import cv2
import pytesseract
import re

def extract_plate_text(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    
    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar un filtro de desenfoque
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detección de bordes con Canny
    edges = cv2.Canny(blur, 50, 150)
    
    # Encontrar contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filtrar contornos por área
    contours = [c for c in contours if cv2.contourArea(c) > 1000]
    
    # Extraer texto de la imagen usando pytesseract
    plate_text = pytesseract.image_to_string(gray)
    
    # Filtrar el texto para obtener solo la matrícula
    #plate_text = re.findall(r'[A-Z0-9]{2,}', plate_text)
    
    return plate_text if plate_text else "No se encontró matrícula"