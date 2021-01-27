import tweepy

class OAuthenticate:

    def __init__(self):
        self.__consumer_key = 'gFeFomO5gld5cx2dq6qWDfLKp'
        self.__consumer_secret = 'XrtYhEPi5oo4nH1FrkZ4ohJWsIrTmAQ3vZJBQD9bHgQz09jYcr'
        self.__access_token = '1318734464898433024-TIkLQh4RKLeYJI7EdnDVkKXDN84iP1'
        self.__access_token_secret = '36KN1CRpbkzRBfltWQ4t5F5Go5kjPas94eIVweUCr9Bih'

    def main(self):
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
        auth.set_access_token(self.__access_token, self.__access_token_secret)

        api = tweepy.API(auth)

        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text.encode('utf-8'))

if __name__ == '__main__':
    OAuthenticate = OAuthenticate()
    OAuthenticate.main()