import os
import pprint
import youtube_dl
import json
import youtube.searchYoutube as searchYt
import sqlite3

def downloadAllSongs() :
    params = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '320',
        }]
    }
    youtube = youtube_dl.YoutubeDL(params)
    # youtube.download() # pass the link of the video to download in form of list

    p = pprint.PrettyPrinter(indent=4)
    # with open('../spotify/toDownload.json', 'r') as fd :
    #     SongDict = json.load(fd)
    conn = sqlite3.connect(r'<your database name>', 
                                check_same_thread=False)
    cur = conn.cursor()
    cur.execute(
        '''
        SELECT * FROM SONGLIST
        '''
    )
    songNames = cur.fetchall()
    # print(songNames)
    # p.pprint(song)
    try :
        os.mkdir('C:\\MUSIC\\Spotify_program')
    except Exception as e:
        print(e)
    os.chdir('C:\\MUSIC\\Spotify_program')

    # tot = []

    for songName in songNames:
        if not songName[-1] :
            # print('not downloaded -->', songName)
            q= songName[0] + songName[1]
            print(songName[0], songName[1])
            result = searchYt.searchFromYoutube(q)
            print([result])   
            if not result == 'no' :
                # print([result])
                cur.execute(
                    '''
                    UPDATE SONGLIST
                    SET DOWNLOADED = ?
                    WHERE ARTIST = ? AND TITLE = ?
                    ''', (True, songName[0], songName[1])
                )
                try :
                    youtube.download([str(result)])
                    conn.commit()
                except :
                    pass
            else :
                print(result)
        else :
            print('already downloaded -->', songName)



# print(len(tot))
# print(k, v)
# for title in titles :
#     cur.execute(
#         '''
#         SELECT * FROM SONGLIST 
#         WHERE ARTIST = ? AND TITLE = ?
#         ''', (artists, title)
#     )
#     songFDb = cur.fetchone()
#     if not songFDb :
#         print('none', songFDb)
#         print(artists, title)
#         break

            # if not songFDb[-1] :
            #     print('not downloaded',songFDb)
        

        #     # 
        # else : 
        #     pass

if __name__ == '__main__' :
    downloadAllSongs()           
