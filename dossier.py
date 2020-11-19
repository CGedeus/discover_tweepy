import json
import base64
import getpass
import urllib2

TWITTER_REST_API = 'https://www.twitter.com/'

class twitterAPI:

    def __init__(self):
        self.username = raw_input("Username: ")
        self.__password = getpass.getpass(prompt = 'Password for {}: '.format(self.username))

    def authenticate(self, theUrl):

        base64string = base64.b64encode('%s:%s' % (self.username, self.__password))
        request = urllib2.Request(theUrl)
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        payLoad = result.read()
        print payLoad


if __name__ == '__main__':
    twitterAPI = twitterAPI()
    twitterAPI.authenticate(TWITTER_REST_API)
