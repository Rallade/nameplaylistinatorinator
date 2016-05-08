#!/usr/bin/env python

import requests
import spotipy
import json

class spotify_operations():

    def __init__(self):
        self.spotify = spotipy.Spotify()
        self.spotify_endpoint = "https://api.spotify.com/v1"

    def get_tracks_in_playlist(self, playlist_json):
        data = json.load(playlist_json)
        print(data["items"][0]["track"]["id"])


    def getSongs(userID, playlist, oAuth):
        tracks = []
        params = {'playlist'}
        url = spotify_endpoint + '/users/{}/playlists/{}/tracks'.format(userID, playlist)

if __name__ == "__main__":
    with open('playlist.json') as f:
        so = spotify_operations()
        so.get_tracks_in_playlist(f)
