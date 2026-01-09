from Base.manipulation import Manipulation_with_DB
from Audio.Play import Tracks
import asyncio


async def main():
    print("1. Добавить трек")
    print("2. Посмотреть трек")
    print("3. Посмотреть все треки")
    print("4. Создать плейлист")
    print("5. Добавить трек в плейлист")
    print("6. Посмотреть все плейлисты")
    print("7. Посмотреть плейлист")
    print("8. Проиграть выбранный трек")
    print("9. Проигррать выбранный плейлист")
    choice = int(input("Выбор: "))


    match choice:
        case 1:
            Manipulation_with_DB.add_track()
        case 2:
            Manipulation_with_DB.get_track()
        case 3:
            Manipulation_with_DB.get_all_tracks()
        case 4:
            Manipulation_with_DB.crate_playlist()
        case 5:
            Manipulation_with_DB.add_track_to_playlist()
        case 6:
            Manipulation_with_DB.list_playlist
        case 7:
            Manipulation_with_DB.show_playlist()
        case 8:
            id = int(input("input: "))
            await Tracks.Track_to_play(id)
        case 9:
            id = int(input("input: "))
            Tracks.Playlist_to_play(id)
        case _:
            print("Неизвестная команда")

   

if __name__ == "__main__":
    asyncio.run(main())