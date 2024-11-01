import cv2
import face_recognition
import numpy as np
import time

def load_authorized_image(image_path):
    try:
        image = face_recognition.load_image_file(image_path)
        return face_recognition.face_encodings(image)[0]
    except Exception as e:
        print(f"Errore nel caricamento dell'immagine autorizzata: {e}")
        return None

# Carica l'immagine autorizzata
authorized_encoding = load_authorized_image("faceAcess/autorizzato.png")
if authorized_encoding is None:
    print("Impossibile caricare l'immagine autorizzata. Uscita.")
    exit()

# Inizializza la webcam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Errore nell'aprire la webcam.")
    exit()

while True:
    try:
        # Cattura un fotogramma dalla webcam
        ret, frame = video_capture.read()
        if not ret:
            print("Impossibile acquisire un fotogramma.")
            break

        rgb_frame = frame[:, :, ::-1]  # Converti BGR a RGB

        # Trova i volti nel fotogramma corrente
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Verifica i volti trovati
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces([authorized_encoding], face_encoding)
            name = "Non autorizzato"

            if True in matches:
                name = "Autorizzato"

            # Mostra il risultato
            print(name)

        # Mostra il fotogramma
        cv2.imshow('Video', frame)

        # Esci dal ciclo se si preme 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Ritardo per ridurre il carico della CPU
        time.sleep(0.1)

    except Exception as e:
        print(f"Errore durante l'esecuzione del ciclo: {e}")

# Rilascia la cattura e chiudi le finestre
video_capture.release()
cv2.destroyAllWindows()
