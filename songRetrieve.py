#!/usr/bin/env python

import requests

spotify_endpoint = "https://api.spotify.com/v1/"

def getSongs(userID, playlist):
    tracks = []
    params = {'playlist'}
    url = spotify_endpoint + '/users/{}/playlists/{}/tracks'.format(userID, playlist)
