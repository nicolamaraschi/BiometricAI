import os
from rembg import remove
from PIL import Image

# Cartella di input e output
input_folder = 'deliteBackground'
output_folder = 'deliteBackground'  # Stesso percorso per l'output

# Controlla se la cartella esiste
if not os.path.exists(input_folder):
    print(f"La cartella {input_folder} non esiste.")
else:
    # Crea la cartella di output se non esiste
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Elenca tutti i file nella cartella di input
    for filename in os.listdir(input_folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Rimuovi lo sfondo
            with open(input_path, 'rb') as input_file:
                input_data = input_file.read()
                output_data = remove(input_data)

                # Salva l'immagine risultante
                with open(output_path, 'wb') as output_file:
                    output_file.write(output_data)

            print(f'Elaborato: {filename}')

    print("Elaborazione completata.")
