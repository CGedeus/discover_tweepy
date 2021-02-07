import csv
import tweepy
import argparse

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

    def user_data(self, oauth, arg):
        '''
        Get user data
        '''
        api = tweepy.API(oauth)
        for tweet in tweepy.Cursor(api.search,q="from:" + arg.handle + " " + arg.tag).items():
            print(tweet)

    def main(self):
        '''
        Authenticate into API:
            - consumer_key
            - consumer_secret
            - access_token
            - access_token_secret
        '''
        auth = tweepy.OAuthHandler(self.__key_token_list[0], self.__key_token_list[1])
        auth.set_access_token(self.__key_token_list[2], self.__key_token_list[3])
        api = tweepy.API(auth)
        return auth


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Specified arguments to querying data')
    parser.add_argument('--handle', metavar = 'handle', type = str, help = 'Twitter Handle')
    parser.add_argument('--tag', metavar = 'tag', type = str, help = '#HASHTAG')
    args = parser.parse_args()

    OAuthenticate = OAuthenticate()
    oauth = OAuthenticate.main()
    OAuthenticate.user_data(oauth, args)