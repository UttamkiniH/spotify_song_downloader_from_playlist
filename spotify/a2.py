import json
import sqlite3

def addToDB() :
    conn = sqlite3.connect(r'<your database pathname>', check_same_thread=False)
    cur = conn.cursor()

    try :
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS SONGLIST(
                ARTIST  VARCHAR(20),
                TITLE   VARCHAR(20),
                DOWNLOADED  BOOLEAN,
                PRIMARY KEY(ARTIST, TITLE)
            )
            '''
        )
        conn.commit()
    except Exception as e :
        pass

    with open(r'<your json path name>', 'r') as fd :
        conn = sqlite3.connect(r'<your database>', check_same_thread=False)
        cur = conn.cursor()
        SongDict = json.load(fd)
        for artists, titles in SongDict.items() :
            for title in titles :
                try :
                    print(artists, title)
                    cur.execute(
                        '''
                        INSERT INTO SONGLIST(ARTIST, TITLE, DOWNLOADED)
                        VALUES(?, ?, ?)
                        ''', (artists, title, False)
                    )
                    conn.commit()
                except Exception as e :
                    print(e)
        
if __name__ == '__main__' :
    addToDB()
