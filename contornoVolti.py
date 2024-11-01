import cv2
import os

# Percorsi delle cartelle
input_folder = 'input'  # Cartella di input
output_folder = 'output'  # Cartella di output

# Crea la cartella di output se non esiste
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Carica il classificatore Haar per il rilevamento dei volti
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Itera su tutte le immagini nella cartella di input
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  # Controlla i formati delle immagini
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # Converti l'immagine in scala di grigi
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Rileva i volti nell'immagine
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

        # Disegna un rettangolo attorno a ciascun volto sull'immagine originale
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Verde con spessore 2

        # Salva l'immagine con i contorni dei volti
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, image)

print("Elaborazione completata. Le immagini con i volti contornati sono salvate in:", output_folder)
