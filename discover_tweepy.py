import tweepy

def main:
    auth = tweepy.OAuthHandler('gFeFomO5gld5cx2dq6qWDfLKp', 'XrtYhEPi5oo4nH1FrkZ4ohJWsIrTmAQ3vZJBQD9bHgQz09jYcr')
    auth.set_access_token('1318734464898433024-TIkLQh4RKLeYJI7EdnDVkKXDN84iP1', '36KN1CRpbkzRBfltWQ4t5F5Go5kjPas94eIVweUCr9Bih')

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text.encode('utf-8'))

if __name__ == '__main__':
    main()