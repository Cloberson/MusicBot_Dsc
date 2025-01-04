# **Discord Music Bot** (PL & ENG)

## **PL:**

**Bot Discord do odtwarzania muzyki z YouTube.** Używa bibliotek `discord.py` oraz `yt-dlp` do odtwarzania dźwięku w kanałach głosowych na serwerze Discord.

### **Funkcjonalności:**
- Odtwarzanie muzyki z YouTube.
- Łączenie się z kanałami głosowymi.
- Możliwość opuszczenia kanału głosowego.
- Kolejka piosenek.
- Zmiana głośności (0-100%).
- Pauza, wznowienie, pomijanie piosenek.
- Automatyczne usuwanie piosenek po 24h lub po osiągnięciu 100 piosenek w kolejce.

### **Instalacja:**

1. **Wymagania:**
   - Python 3.10+.
   - Docker (opcjonalnie).
   - FFmpeg (do dekodowania strumieni audio).
   - yt-dlp (lub youtube-dl) do pobierania treści z YouTube.

2. **Krok 1: Skopiuj repozytorium:**
   ```bash
   git clone https://github.com/Cloberson/MusicBot_Dsc
   cd MusicBot_Dsc
   ```

3. **Krok 2: Instalacja zależności:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Krok 3: Skonfiguruj bota:**
   Przejdź do [Discord Developer Portal](https://discord.com/developers/applications), stwórz aplikację, wygeneruj token bota i wstaw go do kodu.

5. **Krok 4: Uruchomienie bota:**
   ```bash
   python bot.py
   ```

6. **Krok 5: Uruchomienie bota w Dockerze:**
   ```bash
   docker-compose build
   docker-compose up -d
   ```

### **Komendy:**
- **`!play <URL>`** - Odtwarza muzykę z YouTube.
- **`!play <nazwa utworu> <autor (opcjonalnie)>`** - Odtwarza muzykę na podstawie podanej nazwy utworu.
- **`!playauthor <nazwa autora>`** - Odtwarza piosenki autora z YouTube.
- **`!pause`** - Pauzuje aktualnie odtwarzaną piosenkę.
- **`!resume`** - Wznawia odtwarzanie.
- **`!volume <poziom (0-100)>`** - Zmienia głośność.
- **`!leave`** - Opuści kanał głosowy.
- **`!skip`** - Pomija aktualną piosenkę.
- **`!shuffle`** - Losowo odtwarza piosenki.
- **`!nowplaying`** - Wyświetla aktualnie odtwarzaną piosenkę.
- **`!stats`** - Pokazuje statystyki bota.

---

## **ENG:**

**Discord Music Bot to play music from YouTube.** It uses the `discord.py` and `yt-dlp` libraries to play audio in voice channels on a Discord server.

### **Features:**
- Play music from YouTube.
- Join voice channels.
- Ability to leave the voice channel.
- Song queue.
- Volume control (0-100%).
- Pause, resume, skip songs.
- Auto-remove songs after 24 hours or when the queue exceeds 100 songs.

### **Installation:**

1. **Requirements:**
   - Python 3.10+.
   - Docker (optional).
   - FFmpeg (for audio stream decoding).
   - yt-dlp (or youtube-dl) for downloading content from YouTube.

2. **Step 1: Clone the repository:**
   ```bash
   git clone https://github.com/YourRepository.git
   cd YourRepository
   ```

3. **Step 2: Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Step 3: Configure the bot:**
   Go to [Discord Developer Portal](https://discord.com/developers/applications), create an application, generate the bot token, and add it to the code.

5. **Step 4: Run the bot:**
   ```bash
   python bot.py
   ```

6. **Step 5: Run the bot in Docker:**
   ```bash
   docker-compose build
   docker-compose up -d
   ```

### **Bot Commands:**
- **`!play <URL>`** - Play music from YouTube.
- **`!play <song name> <author (optional)>`** - Play music by song name and optional author.
- **`!playauthor <author name>`** - Play songs by the specified author from YouTube.
- **`!pause`** - Pause the currently playing song.
- **`!resume`** - Resume playback.
- **`!volume <level (0-100)>`** - Adjust the volume level.
- **`!leave`** - Make the bot leave the voice channel.
- **`!skip`** - Skip the current song.
- **`!shuffle`** - Shuffle the songs in the queue.
- **`!nowplaying`** - Display the currently playing song.
- **`!stats`** - Show the bot's stats.

---

### **License:**
This project is licensed under the MIT License.

---

### **Disclaimer:**
- The bot uses `yt-dlp` (or `youtube-dl`), which in turn uses the YouTube API. Ensure that you comply with YouTube's terms of service regarding downloading and playing content.
- FFmpeg is required for audio playback. Make sure it is installed correctly on your system or container.

---

### **Issues:**
If you encounter any issues, please report them in the repository’s Issues section.