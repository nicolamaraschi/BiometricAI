import face_recognition
import os

def compare_faces(reference_image_path, images_folder):
    # Carica l'immagine di riferimento
    reference_image = face_recognition.load_image_file(reference_image_path)
    reference_encoding = face_recognition.face_encodings(reference_image)

    # Controlla se ci sono volti nell'immagine di riferimento
    if len(reference_encoding) == 0:
        print("Nessun volto trovato nell'immagine di riferimento.")
        return

    reference_encoding = reference_encoding[0]

    # Lista per memorizzare i risultati
    results = []

    # Itera attraverso le immagini nella cartella
    for i in range(2, 9):  # Da face2 a face8
        filename = f"face{i}.png"
        image_path = os.path.join(images_folder, filename)

        # Carica l'immagine da confrontare
        comparison_image = face_recognition.load_image_file(image_path)
        comparison_encoding = face_recognition.face_encodings(comparison_image)

        # Controlla se ci sono volti nell'immagine da confrontare
        if len(comparison_encoding) == 0:
            print(f"Nessun volto trovato in {filename}.")
            continue

        # Confronta i volti e ottieni la distanza
        distance = face_recognition.face_distance([reference_encoding], comparison_encoding[0])[0]

        # La percentuale di somiglianza è inversamente proporzionale alla distanza
        similarity_percentage = (1 - distance) * 100

        # Aggiungi il risultato alla lista
        results.append((filename, similarity_percentage))

    # Stampa i risultati in ordine specifico
    for filename, percentage in results:
        print(f"face1 vs {filename}: simile al {percentage:.2f}%.")

# Percorso dell'immagine di riferimento e della cartella di immagini
reference_image_path = 'imagesFaceRecognize/face1.png'  # Assicurati che il percorso sia corretto
images_folder = 'imagesFaceRecognize'  # Cartella con le immagini da confrontare

compare_faces(reference_image_path, images_folder)
