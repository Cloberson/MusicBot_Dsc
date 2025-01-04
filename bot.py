import discord
from discord.ext import commands, tasks
import youtube_dl

# Inicjalizacja bota
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Ustawienia youtube_dl
ytdl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True,
    'logtostderr': False,
}

ffmpeg_opts = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

# Funkcja do odtwarzania audio z YouTube
async def play(ctx, url):
    # Sprawdzamy, czy bot jest już na kanale głosowym
    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()

    with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(url2, **ffmpeg_opts))

# Komenda bot do łączenia się do kanału i odtwarzania muzyki
@bot.command(name='play')
async def play_command(ctx, url):
    if not ctx.author.voice:
        await ctx.send("Musisz być na kanale głosowym, aby używać tej komendy.")
        return
    await play(ctx, url)

# Komenda do opuszczania kanału głosowego
@bot.command(name='leave')
async def leave_command(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        await voice_client.disconnect()

# Uruchomienie bota
bot.run('YOUR_DSC_TOKEN')