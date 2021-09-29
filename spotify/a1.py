import json

import tekore as tk

client_id = '7cfedd8d098e4c0999279f490724b0c9'
client_secret = '85ae732f98c74c0bb62b584647df7156'
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
        items = spotify.playlist_items('4d3JNEzPpLo9nrDhQLtVkt')
        tracks = spotify.all_items(items)
    except :
        print('Token expired')
        spotify = setting_spotify_Object(client_id, client_secret, redirect_uri)
        items = spotify.playlist_items('4d3JNEzPpLo9nrDhQLtVkt')
        tracks = spotify.all_items(items)
    with open(r'C:\Users\vital\OneDrive\Desktop\ENGINEERING\python\song downloader\spotify\toDownload.json', 'w') as fd :
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
