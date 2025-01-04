# Discord Music Bot

Bot Discord do odtwarzania muzyki z YouTube. Używa bibliotek `discord.py` oraz `youtube-dl` do odtwarzania dźwięku w kanałach głosowych na serwerze Discord.

## Funkcjonalności

- Odtwarzanie muzyki z YouTube.
- Łączenie się z kanałami głosowymi.
- Możliwość opuszczenia kanału głosowego.
  
## Instalacja

Aby uruchomić bota lokalnie, wykonaj następujące kroki.

### Wymagania

- **Python 3.10** (lub wyższy)
- **Docker** (opcjonalnie, do uruchamiania bota w kontenerze)
- **FFmpeg** (do dekodowania strumieni audio)

### Krok 1: Skopiuj repozytorium

Zacznij od sklonowania repozytorium na swoje lokalne środowisko:

```bash
git clone https://github.com/TwojeRepozytorium.git
cd TwojeRepozytorium
Krok 2: Instalacja zależności
Wykorzystaj plik requirements.txt do zainstalowania wymaganych bibliotek:

bash
Skopiuj kod
pip install -r requirements.txt
Krok 3: Skonfiguruj bota
Przejdź do Discord Developer Portal, stwórz aplikację i wygeneruj token bota. Zapisz token i wstaw go do zmiennej BOT_TOKEN w kodzie, lub możesz ustawić go jako zmienną środowiskową.

Alternatywnie: Możesz dodać token bezpośrednio do pliku bot.py, w miejsce 'YOUR_BOT_TOKEN':

python
Skopiuj kod
bot.run('YOUR_BOT_TOKEN')
Krok 4: Uruchomienie bota
Po zainstalowaniu zależności i ustawieniu tokenu bota, uruchom bota:

bash
Skopiuj kod
python bot.py
Krok 5: Uruchomienie bota w Dockerze
Jeśli chcesz uruchomić bota w Dockerze, upewnij się, że masz zainstalowany Docker na swoim systemie. Możesz użyć docker-compose do łatwego zarządzania kontenerem.

Budowanie obrazu Docker:

bash
Skopiuj kod
docker-compose build
Uruchomienie bota w Dockerze:

bash
Skopiuj kod
docker-compose up -d
Komendy bota
!play <URL> - Bot dołączy do kanału głosowego i zacznie odtwarzać muzykę z YouTube.
!leave - Bot opuści kanał głosowy.
Krok 6: Wyjście z kanału głosowego
Bot opuści kanał głosowy, kiedy użyjesz komendy !leave.

Licencja
Ten projekt jest licencjonowany na zasadach MIT.

Zastrzeżenia
Bot wykorzystuje bibliotekę youtube-dl, która z kolei korzysta z YouTube API. Upewnij się, że przestrzegasz zasad korzystania z YouTube w zakresie pobierania i odtwarzania treści.
FFmpeg jest niezbędny do prawidłowego odtwarzania dźwięku. Upewnij się, że jest poprawnie zainstalowane w systemie lub kontenerze.
Problemy
Jeśli napotkasz jakiekolwiek problemy, zgłoś je na Issues.