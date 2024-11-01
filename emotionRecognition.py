import os
import numpy as np
from fer import FER
from PIL import Image
import matplotlib.pyplot as plt

# Percorso della cartella contenente le immagini
input_folder = 'faceEmotion'

# Crea l'oggetto per il rilevamento delle emozioni
emotion_detector = FER()

# Inizializza una lista per i nomi dei file ordinati
image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.jpeg'))])

# Prepara la figura per i grafici
plt.figure(figsize=(15, 10))

# Itera sulle immagini ordinate
for idx, filename in enumerate(image_files):
    image_path = os.path.join(input_folder, filename)
    image = Image.open(image_path)

    # Converte l'immagine in un array NumPy
    image_np = np.array(image)

    # Rileva le emozioni
    emotions = emotion_detector.detect_emotions(image_np)  # Passa l'array NumPy

    print(f"Risultati per {filename}:")
    
    if emotions:  # Se ci sono emozioni rilevate
        emotion_scores_total = {emotion: 0 for emotion in ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']}
        
        for emotion in emotions:
            # Stampa il riquadro e le emozioni con i punteggi
            box = emotion['box']
            emotion_scores = emotion['emotions']
            
            print(f"  Riquadro: {box}")
            print("  Emozioni:")
            
            for emo, score in emotion_scores.items():
                emotion_scores_total[emo] += score  # Somma i punteggi per l'istogramma
                print(f"    - {emo}: {score:.2f}")
            
            # Trova l'emozione dominante
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            print(f"  Emozione dominante: {dominant_emotion} ({emotion_scores[dominant_emotion]:.2f})")
        
        # Disegna l'istogramma delle emozioni
        plt.subplot(2, 3, idx + 1)  # Crea una sottopagina per ogni immagine
        plt.bar(emotion_scores_total.keys(), emotion_scores_total.values(), color=['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'grey'])
        plt.title(f'Emozioni in {filename}')
        plt.xlabel('Emozioni')
        plt.ylabel('Punteggio')
        plt.ylim(0, 1)  # Imposta l'asse y da 0 a 1
        plt.grid(axis='y')
        
    else:
        print("  Nessuna emozione rilevata.")
    
    print("-" * 30)  # Separator for clarity

print("Elaborazione completata.")

# Mostra tutti i grafici sulla stessa pagina
plt.tight_layout()  # Ottimizza il layout
plt.show()
