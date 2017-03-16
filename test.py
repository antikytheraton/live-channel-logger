import json
import requests
import time
from settings import API
from db_logger import DatabaseLogger

from requests.exceptions import ConnectionError, SSLError

def get_streams(offset):
    headers = {'Client-Id': API['CLIENTID']}
    n = 0
    data = []
    twitch_api_url = 'https://api.twitch.tv/kraken/streams/?stream_type=live&limit=100&offset=' + str(offset)
    try:
        raw = (json.loads(requests.get(twitch_api_url, headers=headers).text)['streams']) 
    except (ValueError, ConnectionError, SSLError):
        time.sleep(5)
    
    if raw:
        for stream in raw:
            print stream
    else:
        print "----------------------------------"
        print "| There's no one but us chicken. |"
        print "----------------------------------"

def get_live_streams_number():
    ''' Pulls the amount of life channels on Twitch. '''

    twitch_api_url = 'https://api.twitch.tv/kraken/streams/summary/?language=en'
    headers = {'Client-Id': API['CLIENTID']}
    try:
        return json.loads(requests.get(twitch_api_url, headers=headers).text)['channels']
    except (ValueError, ConnectionError, SSLError):
        time.sleep(5)
        print get_streams()


def testDB():
    db = DatabaseLogger('localhost', 'streams', 'streams', 'admin123')
    print db.track_exists('boxbox', 1)

print get_live_streams_number()
#get_streams(30000)


