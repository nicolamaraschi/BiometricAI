# Usa un'immagine di base Python
FROM python:3.9-slim

# Imposta la directory di lavoro nel contenitore
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze specificate in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il codice sorgente nella directory di lavoro
COPY . .

# Comando per eseguire il tuo script (modifica il nome dello script se necessario)
CMD ["python", "your_script.py"]
