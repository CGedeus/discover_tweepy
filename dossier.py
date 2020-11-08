import getpass
import base64
import urllib2
import requests

theUrl = 'https://api.twitter.com/' #updated twitter rest api

def authenticate():
    username = raw_input("Username: ")
    __password = getpass.getpass(prompt = 'Password for {}: '.format(username))

    request = urllib2.Request(theUrl)
    base64string = base64.b64encode('%s:%s' % (username, __password))
    request.add_header("Authorization", "Basic %s" % base64string)   
    result = urllib2.urlopen(request)
    print result.read()

if __name__ == '__main__':
    authenticate()