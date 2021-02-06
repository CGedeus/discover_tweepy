import csv
import tweepy

class OAuthenticate:

    def __init__(self):
        '''
        Get tokens/keys from external file
        '''
        self.__key_token_list = []

        with open('secret_keys.csv', 'r') as fin:
            column = csv.reader(fin)
            header = (next(column))

            for data in header:
                self.__key_token_list.append(data)

    def main(self):
        auth = tweepy.OAuthHandler(self.__key_token_list[0], self.__key_token_list[1])
        auth.set_access_token(self.__key_token_list[2], self.__key_token_list[3])

        api = tweepy.API(auth)

        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text.encode('utf-8'))

if __name__ == '__main__':
    OAuthenticate = OAuthenticate()
    OAuthenticate.main()