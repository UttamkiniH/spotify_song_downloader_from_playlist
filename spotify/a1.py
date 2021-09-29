import json

import tekore as tk

client_id = '<your client id>'
client_secret = '<your client secret>'
redirect_uri = 'https://example.com/callback/'

def setting_spotify_Object(client_id, client_secret, redirect_uri):
    user_token = tk.prompt_for_user_token(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=tk.scope.every
    )

    print('starting....')
    print('-'*970, '\n')
    spotify = tk.Spotify(user_token)
    # print(spotify.playback_currently_playing())
    return spotify

spotify = setting_spotify_Object(client_id, client_secret, redirect_uri)

def getAllNames():
    global spotify # to use global variable spotify 
    try :
        items = spotify.playlist_items('<your playlist id>')
        tracks = spotify.all_items(items)
    except :
        print('Token expired')
        spotify = setting_spotify_Object(client_id, client_secret, redirect_uri)
        items = spotify.playlist_items('<your playlist id>')
        tracks = spotify.all_items(items)
    with open(r'<your path to songs.json>', 'w') as fd :
        songDict = {}
        for track in tracks :
            print(track.track.name, end="---->")
            print(track.track.artists[0].name)
            if track.track.artists[0].name not in songDict :
                songDict[track.track.artists[0].name] = []
                songDict[track.track.artists[0].name].append(track.track.name)
            else :
                songDict[track.track.artists[0].name].append(track.track.name)
            
        json.dump(songDict, fd, indent=4)
        # break
    # print(items.items[0].track)


if __name__ == '__main__' :
    getAllNames()
