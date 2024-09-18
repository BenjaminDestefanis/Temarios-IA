import cv2
import numpy as np

# Función para procesar la imagen y detectar la línea
def detectar_linea(frame):
    # Convertir a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Aplicar desenfoque gaussiano para reducir el ruido
    desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)
    
    # Aplicar un umbral para detectar la línea (asumiendo que es una línea negra)
    _, umbral = cv2.threshold(desenfoque, 60, 255, cv2.THRESH_BINARY_INV)
    
    # Definir la región de interés (ROI) para enfocarse solo en la parte inferior de la imagen
    altura, ancho = umbral.shape
    roi = umbral[int(altura / 2):, :]  # La mitad inferior de la imagen
    
    # Encontrar los contornos de la línea
    contornos, _ = cv2.findContours(roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dibujar la línea detectada y calcular el centro
    if len(contornos) > 0:
        # Obtener el contorno más grande (asumimos que es la línea)
        contorno_mayor = max(contornos, key=cv2.contourArea)
        # Obtener las coordenadas del rectángulo delimitador de la línea
        x, y, w, h = cv2.boundingRect(contorno_mayor)
        # Dibujar el rectángulo alrededor de la línea
        cv2.rectangle(frame, (x, int(altura / 2) + y), (x + w, int(altura / 2) + y + h), (0, 255, 0), 2)
        # Calcular el centro de la línea
        centro_x = x + w // 2
        return centro_x
    return None

# Captura de video (desde la cámara)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar la línea en la imagen
    centro_linea = detectar_linea(frame)

    # Obtener el centro de la imagen
    altura, ancho, _ = frame.shape
    centro_imagen = ancho // 2

    # Dibujar el centro de la imagen
    cv2.line(frame, (centro_imagen, 0), (centro_imagen, altura), (255, 0, 0), 2)

    # Si se ha detectado una línea, dibujar una línea indicadora desde el centro de la imagen
    if centro_linea is not None:
        cv2.line(frame, (centro_linea, altura // 2), (centro_linea, altura), (0, 0, 255), 2)
        # Control lógico o simulación de movimiento (dependería de tu robot)
        if centro_linea < centro_imagen - 10:
            print("Mover a la izquierda")
        elif centro_linea > centro_imagen + 10:
            print("Mover a la derecha")
        else:
            print("Seguir recto")
    else:
        print("Línea no detectada")

    # Mostrar el frame procesado
    cv2.imshow("Seguidor de línea", frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
