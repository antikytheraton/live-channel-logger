import json
import requests
import time
from settings import API, DATABASE
from db_logger import DatabaseLogger

from requests.exceptions import ConnectionError, SSLError

class PullData(object):
    def __init__(self):
        self.headers = {'Client-Id': API['CLIENTID']}
        self.offset = 0
        self.batch = 1
        self.total_values = 0

    def run(self):
        db_logger = DatabaseLogger(DATABASE['HOST'], DATABASE['NAME'], DATABASE['USER'], DATABASE['PASSWORD'])
        data = []

        print "I'll begin the scrapping."
        while True:
            twitch_api_url = 'https://api.twitch.tv/kraken/streams/?stream_type=live&limit=100&offset='+str(self.getOffset()) #&language=en
            try:
                data = (json.loads(requests.get(twitch_api_url, headers=self.getHeaders()).text)['streams']) 
            except (ValueError, ConnectionError,KeyError ,SSLError):
                time.sleep(5)
            except KeyboardInterrupt:
                print "Closing scrapper gracefully!"
                db_logger.close()
            
            for stream in data:
                if not db_logger.track_exists(stream['channel']['name'], self.batch):
                    db_logger.log_stream(self.batch, stream)
                    self.increaseTotalViews()
            
            print "Collecting Data! Values: ", self.getTotalViews()
            print "Current page Value: ", self.getOffset()
            self.nextOffset()
            
            if not data:
                print "Finished Batch!"
                self.resetOffset()
                self.nextBatch()

    def nextBatch(self):
        self.batch += 1

    def nextOffset(self):
        self.offset += 50
    
    def getOffset(self):
        return self.offset
    
    def getTotalViews(self):
        return self.total_values
    
    def getHeaders(self):
        return self.headers

    def resetOffset(self):
        self.offset = 0
    
    def increaseTotalViews(self):
        self.total_values += 1