import vlc
import yt_dlp
from time import sleep
import asyncio



class Player():
    def __init__(self):
        self.current_thread = None




    async def play_youtube_audio(self, url, loop):
        """
        Проигрывает аудио с YouTube по ссылке.
        loop=True — повтор трека бесконечно
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'no_warnings': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']

        player = vlc.MediaPlayer(audio_url)
        player.play()
        print("▶ Проигрывание... Нажмите Ctrl+C для остановки.")

        try:
            while True:
                state = player.get_state()
                # если трек закончился или произошла ошибка
                if state in [vlc.State.Ended, vlc.State.Error]:
                    if loop:
                        player.stop()
                        player.play()  # перезапускаем
                    else:
                        break
                sleep(1)
        except KeyboardInterrupt:
            print("\n⏹ Остановка")
            player.stop()





    def play_youtube_playlist(self, tracks, loop):
        """
        Проигрывает аудио с YouTube по ссылке.
        loop=True — повтор трека бесконечно
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'no_warnings': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if loop:
                try:
                    while True:
                        for track in tracks:
                            info = ydl.extract_info(track.link, download=False)
                            audio_url = info['url']
                            player = vlc.MediaPlayer(audio_url)
                            player.play()
                            print(f"▶{track.title}")
                            try:
                                while True:
                                    state = player.get_state()
                                    # если трек закончился или произошла ошибка
                                    if state in [vlc.State.Ended, vlc.State.Error]:
                                        break

                            except KeyboardInterrupt:
                                print("\n⏹ Остановка")
                                player.stop()
                except KeyboardInterrupt:
                    print("\n⏹ Остановка")
                    player.stop()
            else:
                for track in tracks:
                    info = ydl.extract_info(track.link, download=False)
                    audio_url = info['url']
                    player = vlc.MediaPlayer(audio_url)
                    player.play()
                    print(f"▶{track.title}")
                    try:
                        while True:
                            state = player.get_state()
                            # если трек закончился или произошла ошибка
                            if state in [vlc.State.Ended, vlc.State.Error]:
                                break
                            sleep(1)
                    except KeyboardInterrupt:
                        print("\n⏹ Остановка")
                        player.stop()
