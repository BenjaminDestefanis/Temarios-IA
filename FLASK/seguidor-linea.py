import cv2 as cv
import numpy as np


# funcion para procesar imagen y detectar la linea

def detectar_linea(frame):

    # Convertir a gris
    gris = cv.cvtColor(frame, cv.COLOR_BAYER_BG2GRAY)


    desenfoque = cv.GaussianBlur(gris, (5,5), 0)
    
    # Aplicar unbral para detectar linea (asumiendo que la linea es negra)
    _, umbral = cv.threshold(desenfoque, 60, 255, cv.THRESH_BINARY_INV)

    # Definir la region de interes para enfocarse solo en la parte inferior de la imagen

