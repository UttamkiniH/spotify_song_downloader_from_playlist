import urllib.request as request
import urllib.parse as parse
import re
# from bs4 import BeautifulSoup

def searchFromYoutube(textToSearch1):
    baseQueryUrl = r'https://www.youtube.com/results?search_query='
    baseVideoUrl = r'https://www.youtube.com/watch?v='
    textToSearch = textToSearch1

    reSearchPattern = r"watch\?v=(\S{11})"
    parsedUrlSearch = parse.quote(textToSearch)

    html = request.urlopen(baseQueryUrl+parsedUrlSearch)
    parsedHTML = html.read().decode()
    # print(parsedHTML)
    videoIds = re.findall(reSearchPattern, parsedHTML)
    # print(videoIds)
    try:
        return baseVideoUrl+videoIds[0]
    except Exception as e :
        return 'no'

