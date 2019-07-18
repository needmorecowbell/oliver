import requests
import json
from pprint import pprint




def getTopPlayedArtists(user,n=10):
    params = {
        "user":user,
        "limit":n
    }
    url = "http://ws.audioscrobbler.com/2.0/?method=library.getartists&api_key="+config['key']+"&format=json"
    results = requests.get(url, params=params).json()

    padding = 50

    print("Artist".ljust(padding)+"Playcount")

    for artist in results["artists"]["artist"]:
        print(artist["name"].ljust(padding)+ artist["playcount"])

def getTopPlayedTracks(user,n=10, period="overall"):
    params = {
        "user":user,
        "limit":n,
        "period":period
    }
    url = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user="+user+"&api_key="+config['key']+"&format=json"
    results = requests.get(url, params=params).json()

    # overall | 7day | 1month | 3month | 6month | 12month

    padding = 50

    print("Track".ljust(padding)+"Artist".ljust(padding)+"Playcount")

    for track in results["toptracks"]["track"]:
        print(track["name"].ljust(padding)+track["artist"]["name"].ljust(padding)+ track["playcount"])

def getLastPlayedTracks(user,n=10):
    params = {
        "user":user,
        "limit":n
    }
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user="+user+"&api_key="+config['key']+"&format=json"
    results = requests.get(url, params=params).json()

    # overall | 7day | 1month | 3month | 6month | 12month

    padding = 50

    print("Track".ljust(padding)+"Artist".ljust(padding)+"Date")
    for track in results["recenttracks"]["track"]:
        print(track["name"].ljust(padding)+track["artist"]["#text"].ljust(padding)+ track["date"]["#text"])


if __name__ == '__main__':
    config = None
    with open('keys.json') as cfg:
        config = json.load(cfg)

    print("Getting Top 10 Listened Tracks This Week\n")

    getTopPlayedTracks("amusciano",n=10,period="7day")

    print("\n\n")
    print("Getting Top 10 Listened Tracks All Time\n")
    getTopPlayedTracks("amusciano",n=10,period="overall")

    print("\n\n")
    print("Getting Top 10 Listened Artists All Time\n")
    getTopPlayedArtists("amusciano",n=10)

    print("\n\n")
    print("Getting Last 10 Tracks Played\n")
    getLastPlayedTracks("amusciano",n=10)
