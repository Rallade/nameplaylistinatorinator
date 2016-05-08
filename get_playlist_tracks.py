import sys
import urllib
import json
import spotipy
import spotipy.util as util

def get_playlist_tracks()
    SPOTIPY_CLIENT_ID='c61ea8f273e341faa04681b289894ee6'
    SPOTIPY_CLIENT_SECRET='83f8d583b70d420186ab8be3c9d9faac'
    SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

    scope = 'playlist-modify-private'

    if len(sys.argv) > 2:
        username = sys.argv[1]
        playlist_id = sys.argv[2]
    else:
        print("Usage: %s username playlist_id..." % (sys.argv[0],))
        sys.exit()

    token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    if token:
    	sp = spotipy.Spotify(auth=token)
    	sp.trace = False
    	playlist = sp.user_playlist_tracks(username, playlist_id)
    	with open('playlist.json', 'w') as f1:
    		json.dump(playlist, f1)
    else:
        print("Can't get token for", username)
