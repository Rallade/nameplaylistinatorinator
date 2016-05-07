#!/usr/bin/env python

import requests
import spotipy

class spotify_operations:

    def __init__(self):
        spotify = spotipy.Spotify()

        spotify_endpoint = "https://api.spotify.com/v1"

    def getSongs(userID, playlist, oAuth):
        tracks = []
        params = {'playlist'}
        url = spotify_endpoint + '/users/{}/playlists/{}/tracks'.format(userID, playlist)
