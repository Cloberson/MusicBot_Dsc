# Używamy oficjalnego obrazu Pythona jako bazy
FROM python:3.10-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki z lokalnego systemu do kontenera
COPY . /app

# Instalujemy zależności z pliku requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instalujemy ffmpeg (konieczne do odtwarzania muzyki)
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Komenda, która uruchamia bota
CMD ["python", "bot.py"]
