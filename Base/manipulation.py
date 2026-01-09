from Base.db import Base, engine, SessionLocal
from Base.model import Track, Playlist

PAGE_SIZE = 10

class Manipulation_with_DB():

    def init_db():
        Base.metadata.create_all(bind=engine)



    def add_track():
        with SessionLocal() as session:

            track = Track(
                title = input("Название: "),
                source = input("Источник (youtube/local/url): "),
                link = input("Ссылка: "),
                rating = int(input("Оценка (1–10): "))
            )

            session.add(track)
            session.commit()
            session.close()



    def get_track(self,id):
        with SessionLocal() as session:
            track = session.get(Track,int(id))
            if track is None:
                print("Не найдено")
                return
            print (track.title,track.link)
        return track



    def get_all_tracks():
        page = 0
        while True:
            with SessionLocal() as session:
                tracks = (
                    session.query(Track.id,Track.title,Track.rating)
                    .order_by(Track.id)
                    .offset(page * PAGE_SIZE)
                    .limit(PAGE_SIZE)
                    .all())
            if not tracks:
                print("Больше треков нет.")
                break
            print(f"\nСтраница {page + 1}\n" + "-" * 30)
            for track in tracks:
                print(f"[{track.id}] {track.title} | ⭐ {track.rating}")

            print("\n[N] далее  [P] назад  [Q] выход")
            choice = input("→ ").lower()

            if choice == "n":
                page += 1
            elif choice == "p" and page > 0:
                page -= 1
            elif choice == "q":
                break
            else:
                print("Неизвестная команда")



    def crate_playlist():
        with SessionLocal() as session:
            playlist = Playlist(
                name = input("Название плейлиста:"))
        session.add(playlist)
        session.commit()
        session.close()




    def add_track_to_playlist():
        with SessionLocal() as session:
            playlists = session.query(Playlist).order_by(Playlist.id).all()

            if not playlists:
                print("Плейлистов нет")
                return

            for playlist in playlists:
                print(f"{playlist.id} || {playlist.name} — {len(playlist.tracks)} треков")

            playlist_id = int(input("Выберите плейлист (id): "))
            playlist = session.get(Playlist, playlist_id)

            if not playlist:
                print("Несуществующий плейлист")
                return

            track_ids = input("Введите id треков (через запятую): ")

            valid_tracks = []

            for raw_id in track_ids.split(","):
                try:
                    track_id = int(raw_id.strip())
                except ValueError:
                    print(f"Некорректный id: {raw_id}")
                    continue

                track = session.get(Track, track_id)
                if not track:
                    print(f"Трека с id={track_id} не существует")
                    continue

                valid_tracks.append(track)

            if not valid_tracks:
                print("Нет валидных треков для добавления")
                return

            for track in valid_tracks:
                if track not in playlist.tracks:
                    playlist.tracks.append(track)

            session.commit()
            print("✔ Треки добавлены в плейлист")




    def list_playlists():
        with SessionLocal() as session:
            playlists = session.query(Playlist).order_by(Playlist.name).all()

            if not playlists:
                print("Плейлистов пока нет.")
                return

            for playlist in playlists:
                print(f"\n📂 {playlist.name} — {len(playlist.tracks)} треков")
                print("-" * 40)

                if playlist.tracks:
                    for track in playlist.tracks:
                        print(f"[{track.id}] {track.title} | ⭐ {track.rating}")
                else:
                    print("— пустой —")



    def show_playlist():
        playlist_name = input("Название плейлиста: ")

        with SessionLocal() as session:
            playlist = session.query(Playlist).filter_by(name=playlist_name).first()

            if not playlist:
                print("Плейлист не найден.")
                return

            tracks = playlist.tracks
            if not tracks:
                print("Плейлист пустой.")
                return

            page = 0
            while True:
                start = page * PAGE_SIZE
                end = start + PAGE_SIZE
                page_tracks = tracks[start:end]

                print(f"\n📂 {playlist.name} — Страница {page + 1}")
                print("-" * 40)

                for track in page_tracks:
                    print(f"[{track.id}] {track.title} | ⭐ {track.rating}")

                # Проверка на конец/начало
                has_next = end < len(tracks)
                has_prev = page > 0

                commands = []
                if has_next:
                    commands.append("[N] далее")
                if has_prev:
                    commands.append("[P] назад")
                commands.append("[Q] выход")

                print("\n" + "  ".join(commands))
                choice = input("→ ").lower()

                if choice == "n" and has_next:
                    page += 1
                elif choice == "p" and has_prev:
                    page -= 1
                elif choice == "q":
                    break
                else:
                    print("Неизвестная команда")



class Tracks_for_Player():
    def get_tracks_from_playlist(self, playlist_id):
        with SessionLocal() as session:
            playlist = session.query(Playlist).filter_by(id=playlist_id).first()
            if not playlist:
                print("Плейлист не найден.")
                return

            tracks = playlist.tracks
            if not tracks:
                print("Плейлист пустой.")
                return

            return tracks
