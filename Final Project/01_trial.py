import tweepy

auth = tweepy.OAuthHandler('LGagr7jJ6io6RyWZvwt9Tc38R', 'rvVxEb1suQrm2m53CEaPUsGtKshwgn6a4OKJmiMzBfzHj569Y7')
access_token = open('/Users/garch/Downloads/tokens/final_access_token.txt', 'r')
access_token_secret = open('/Users/garch/Downloads/tokens/final_access_token_secret.txt', 'r')

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status('tweepy + oauth!')
