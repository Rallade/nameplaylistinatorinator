import spotipy
import spotify_operations

so = spotify_operations.spotify_operations()
playlist_tracks = so.get_playlist_tracks(so.username, so.playlist_id)
track_id_list = so.get_tracks_in_playlist(playlist_tracks)
metadata_list = []
for track in track_id_list:
	metadata_list.append(so.get_track_metadata(track))
i = 0
for metadata in metadata_list:
	print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))

	
so = spotify_operations.spotify_operations()
so.username = "theageoldstruggle"
so.playlist_id = "0dmCRdGkYnSgLtpONJB9ZY"
playlist_tracks = so.get_playlist_tracks(so.username, so.playlist_id)
track_id_list = so.get_tracks_in_playlist(playlist_tracks)
metadata_list = []
for track in track_id_list:
	metadata_list.append(so.get_track_metadata(track))
i = 0
for metadata in metadata_list:
	print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))
	
so = spotify_operations.spotify_operations()
so.username = "spotify_uk_"
so.playlist_id = "3swUuRQY6xIKziiN31FdGQ"
playlist_tracks = so.get_playlist_tracks(so.username, so.playlist_id)
track_id_list = so.get_tracks_in_playlist(playlist_tracks)
metadata_list = []
for track in track_id_list:
	metadata_list.append(so.get_track_metadata(track))
i = 0
for metadata in metadata_list:
	print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))