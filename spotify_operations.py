#!/usr/bin/env python

import requests
import spotipy
import json
import sys
import spotipy.util as util

class spotify_operations():

    def __init__(self):
        self.spotify = spotipy.Spotify()
        self.spotify_endpoint = "https://api.spotify.com/v1"
        self.username = "1142780915"

    def get_tracks_in_playlist(self, playlist_json):
        data = json.load(playlist_json)
        track_ids = []
        print(len(data["items"]))
        for i in range(0, len(data["items"])):
            track_ids.append(data["items"][i]["track"]["id"])
        return track_ids

    def get_track_metadata(self, trackid):
    	SPOTIPY_CLIENT_ID='c61ea8f273e341faa04681b289894ee6'
    	SPOTIPY_CLIENT_SECRET='83f8d583b70d420186ab8be3c9d9faac'
    	SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

    	scope = 'playlist-modify-private'
    	token = util.prompt_for_user_token(self.username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    	if token:
    		sp = spotipy.Spotify(auth=token)
    		ids = [trackid]
    		metadata = sp.audio_features(ids);
    		return metadata
    		#with open('metadata.json', 'w') as f1:
    		#	json.dump(metadata, f1)
    	else:
    	    print("Can't get token for", trackid)

    def getSongs(userID, playlist, oAuth):
        tracks = []
        params = {'playlist'}
        url = spotify_endpoint + '/users/{}/playlists/{}/tracks'.format(userID, playlist)

if __name__ == "__main__":
    with open('playlist.json') as f:
        so = spotify_operations()
        track_id_list = so.get_tracks_in_playlist(f)
        for track in track_id_list:
            print(so.get_track_metadata(track))
