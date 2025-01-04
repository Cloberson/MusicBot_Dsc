import discord
from discord.ext import commands
import yt_dlp as ytdlp
import asyncio
import os
import time
import random
from collections import Counter

# Token bota
TOKEN = 'YOUR_TOKEN_DC_DEV'

# Inicjalizacja bota
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Kolejka piosenek
song_queue = []
is_playing = False
is_playing_author = False  # Flaga do sprawdzania, czy gramy piosenki autora

# Słownik przechowujący liczbę odtworzeń piosenek
play_count = Counter()

# Funkcja pobierająca audio z YouTube
def get_audio_from_youtube(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'outtmpl': 'downloads/%(id)s.%(ext)s',  # Zapisuje pliki w folderze "downloads"
        'postprocessors': [{
            'key': 'FFmpegAudio',
            'preferredcodec': 'mp3',  # Można zmienić na 'opus', 'wav', itp.
            'preferredquality': '192',
        }],
    }
    
    with ytdlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['formats'][0]['url']
        return audio_url, info['title'], info.get('uploader', 'Nieznany Twórca')

# Funkcja do odtwarzania muzyki z kolejki
async def play_from_queue(ctx):
    global is_playing, is_playing_author

    if song_queue:
        is_playing = True
        song = song_queue.pop(0)
        audio_url, title, uploader = song['audio_url'], song['title'], song['uploader']
        
        # Dołączanie do kanału głosowego
        if not ctx.voice_client:
            channel = ctx.author.voice.channel
            await channel.connect()

        # Odtwarzanie audio
        voice_client = ctx.voice_client
        voice_client.play(discord.FFmpegPCMAudio(audio_url), after=lambda e: asyncio.run_coroutine_threadsafe(play_from_queue(ctx), bot.loop))

        await ctx.send(f'Odtwarzam: {title} - Twórca: {uploader}')
    else:
        is_playing = False
        if not is_playing_author:
            await ctx.voice_client.disconnect()

# Komenda do odtwarzania muzyki z YouTube
@bot.command()
async def play(ctx, *args):
    global is_playing, is_playing_author, play_count

    # Sprawdzamy, czy użytkownik jest na kanale głosowym
    if not ctx.author.voice:
        await ctx.send("Musisz dołączyć do kanału głosowego, aby odtwarzać muzykę.")
        return
    
    url = None
    query = " ".join(args)

    if query.startswith("http") and "youtube.com" in query:
        url = query
    else:
        # Szukamy w YouTube, jeśli nie jest podany URL
        url = f"https://www.youtube.com/results?search_query={query}"

    if url:
        audio_url, title, uploader = get_audio_from_youtube(url)
        song_queue.append({'audio_url': audio_url, 'title': title, 'uploader': uploader, 'added_at': time.time()})

        # Zwiększamy licznik odtworzeń
        play_count[title] += 1

        # Jeśli bot nie odtwarza nic, zaczynamy odtwarzanie
        if not is_playing:
            await play_from_queue(ctx)
        else:
            await ctx.send(f"Dodano do kolejki: {title} - Twórca: {uploader}")

# Komenda do odtwarzania piosenek danego twórcy
@bot.command()
async def playauthor(ctx, *args):
    global is_playing_author

    if not ctx.author.voice:
        await ctx.send("Musisz dołączyć do kanału głosowego, aby odtwarzać muzykę.")
        return

    author_name = " ".join(args)
    
    # Jeśli bot już odtwarza piosenki autora, nie zaczynamy nowego odtwarzania
    if is_playing_author:
        await ctx.send(f"Bot już odtwarza piosenki {author_name}.")
        return

    is_playing_author = True

    # Szukamy piosenek danego autora w YouTube
    for i in range(1, 6):  # Będziemy pobierać 5 stron wyników
        url = f"https://www.youtube.com/results?search_query={author_name}+page{i}"
        
        # Pobieramy metadane dla każdej piosenki w wynikach
        ydl_opts = {'quiet': True}
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)

        for entry in result['entries']:
            if entry.get('title') and entry.get('uploader'):
                audio_url, title, uploader = get_audio_from_youtube(entry['url'])
                song_queue.append({'audio_url': audio_url, 'title': title, 'uploader': uploader, 'added_at': time.time()})

    # Rozpoczynamy odtwarzanie piosenek danego autora
    if not is_playing:
        await play_from_queue(ctx)

    await ctx.send(f"Odtwarzanie piosenek autora {author_name} rozpoczęte!")

# Komenda do pauzy odtwarzania
@bot.command()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("Muzyka została wstrzymana.")
    else:
        await ctx.send("Nie odtwarzam żadnej muzyki.")

# Komenda do wznowienia odtwarzania
@bot.command()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Muzyka została wznowiona.")
    else:
        await ctx.send("Muzyka nie jest wstrzymana.")

# Komenda do zmiany głośności
@bot.command()
async def volume(ctx, level: int):
    if 0 <= level <= 100:
        if ctx.voice_client:
            ctx.voice_client.source = discord.PCMVolumeTransformer(ctx.voice_client.source, volume=level / 100)
            await ctx.send(f"Ustawiono głośność na {level}%.")
        else:
            await ctx.send("Nie jestem połączony z kanałem głosowym.")
    else:
        await ctx.send("Proszę podać wartość głośności w zakresie 0-100.")

# Komenda do opuszczenia kanału głosowego
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Bot opuścił kanał głosowy.")
    else:
        await ctx.send("Bot nie jest na kanale głosowym.")

# Losowanie piosenek z kolejki
@bot.command()
async def shuffle(ctx):
    if not song_queue:
        await ctx.send("Kolejka jest pusta.")
        return
    
    song = random.choice(song_queue)
    song_queue.remove(song)
    audio_url, title, uploader = song['audio_url'], song['title'], song['uploader']
    await play_from_queue(ctx)
    await ctx.send(f'Zaczynamy losowanie! Odtwarzam: {title} - Twórca: {uploader}')

# Komenda do skipowania piosenek
@bot.command()
async def skip(ctx):
    if ctx.voice_client:
        ctx.voice_client.stop()
        await ctx.send("Piosenka została pominięta!")
        await play_from_queue(ctx)
    else:
        await ctx.send("Nie odtwarzam żadnej piosenki.")

# Komenda do wyświetlania informacji o aktualnie odtwarzanej piosence
@bot.command()
async def nowplaying(ctx):
    if not song_queue:
        await ctx.send("Nie odtwarzam żadnej muzyki.")
        return
    
    song = song_queue[0]  # Pierwsza piosenka w kolejce
    await ctx.send(f"Aktualnie odtwarzam: {song['title']} - Twórca: {song['uploader']}")

# Statystyki odtworzeń
@bot.command()
async def stats(ctx):
    total_songs_played = sum(play_count.values())
    users_using_bot = len(set([song['uploader'] for song in song_queue]))
    await ctx.send(f"Statystyki: {total_songs_played} odtworzonych piosenek, {users_using_bot} unikalnych użytkowników.")

# Usuwanie starych piosenek i kontrolowanie liczby piosenek w kolejce
async def remove_old_songs():
    global song_queue
    while True:
        current_time = time.time()
        song_queue = [song for song in song_queue if current_time - song['added_at'] < 86400]  # Usuwanie po 24h
        if len(song_queue) > 100:
            song_queue = song_queue[:100]  # Zostaw tylko pierwsze 100 piosenek
        await asyncio.sleep(600)  # Sprawdzaj co 10 minut

bot.loop.create_task(remove_old_songs())  # Uruchamiamy sprawdzanie starszych piosenek

# Uruchomienie bota
bot.run(TOKEN)