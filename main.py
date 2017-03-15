from pullData import PullData
from settings import API

# We get the Client ID to connect with Twitch API
headers = {'Client-Id': API['CLIENTID']}

def main():
    
    print "The script will start pulling data!"
    scrapper = PullData()
    scrapper.run()


if __name__ == "__main__":
    main()