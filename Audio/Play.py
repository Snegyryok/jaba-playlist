from Base.manipulation import Tracks_for_Player, Manipulation_with_DB
from Audio.player import Player





class Tracks():

    async def Track_to_play(id):
        player = Player()
        Track = Manipulation_with_DB()
        track = Track.get_track(id)
        loop = input("loop? y/n: ")
        if loop =="y":
           await player.play_youtube_audio(track.link, True)
        else:
           await player.play_youtube_audio(track.link, False)



    def Playlist_to_play(id):
        player = Player()
        Playlist = Tracks_for_Player()
        track_playlist = Playlist.get_tracks_from_playlist(id)
        loop = input("loop? y/n: ")
        if loop == "y":
            player.play_youtube_playlist(track_playlist, True)
        else:
            player.play_youtube_playlist(track_playlist, False)
