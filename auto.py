import spotipy
import spotify_operations
import ml_operations

so = spotify_operations.spotify_operations()
ml = ml_operations.ml_operations()

playlist_tracks = so.get_playlist_tracks()
track_id_list = so.get_tracks_in_playlist(playlist_tracks)
metadata_list = []
for track in track_id_list:
	metadata_list.append(so.get_track_metadata(track))
i = 0
for metadata in metadata_list:
	print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))
scores_list=[]
for metadata in metadata_list:
    #print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))
    scores_list.append(ml.predict([metadata[i]["valence"], metadata[i]["energy"]]))
print(scores_list)


so = spotify_operations.spotify_operations()
ml = ml_operations.ml_operations()
so.username = "theageoldstruggle"
so.playlist_id = "0dmCRdGkYnSgLtpONJB9ZY"
playlist_tracks = so.get_playlist_tracks()
track_id_list = so.get_tracks_in_playlist(playlist_tracks)
metadata_list = []
for track in track_id_list:
	metadata_list.append(so.get_track_metadata(track))
i = 0
for metadata in metadata_list:
	print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))
scores_list=[]
for metadata in metadata_list:
    #print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))
    scores_list.append(ml.predict([metadata[i]["valence"], metadata[i]["energy"]]))
print(scores_list)

so = spotify_operations.spotify_operations()
ml = ml_operations.ml_operations()
so.username = "1142780915"
so.playlist_id = "2IEfJNoWklzEaJY1jNTLdE"
playlist_tracks = so.get_playlist_tracks()
track_id_list = so.get_tracks_in_playlist(playlist_tracks)
metadata_list = []
for track in track_id_list:
	metadata_list.append(so.get_track_metadata(track))
i = 0
for metadata in metadata_list:
	print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))
scores_list=[]
for metadata in metadata_list:
    #print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))
    scores_list.append(ml.predict([metadata[i]["valence"], metadata[i]["energy"]]))
print(scores_list)
