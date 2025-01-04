# Używamy oficjalnego obrazu Pythona jako bazy
FROM python:3.10-slim

# Instalacja wymaganych narzędzi
RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Tworzymy i ustawiamy katalog roboczy
WORKDIR /app

# Kopiowanie plików do kontenera
COPY . /app

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Komenda uruchamiająca bota
CMD ["python", "bot.py"]
