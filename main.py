import spotify_operations
import ml_operations

if __name__ == "__main__":
    with open('playlist.json') as f:
        so = spotify_operations.spotify_operations()
        ml = ml_operations.ml_operations()
        playlist_tracks = so.get_playlist_tracks()
        track_id_list = so.get_tracks_in_playlist(playlist_tracks)
        metadata_list = []
        for track in track_id_list:
            metadata_list.append(so.get_track_metadata(track))
        i = 0

        scores_list = []
        for metadata in metadata_list:
            #print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))
            scores_list.append(ml.predict([metadata[i]["valence"], metadata[i]["energy"]]))
        print(scores_list)
