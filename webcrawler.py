import tweepy
import csv
import time

consumer_key = "	wxEo63n98b9eVoCiMdzpfPOqe"
consumer_secret = "CQmUD9lZilXKHFHgKCZGZVuqjKh3Gi3nT0AWaT2AuFU34ohi3G"
access_token="	840288921225437184-swOf0qeYK8kmR2ri2P9yxhyP7W6QsA9"
access_token_secret="DHXFavqiGBpPzDkDtXx18gOEmNzVHMsXrwZPrebGvSry5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

arquivo1 = csv.writer(open("base_teste.csv", "w"))
arquivo2 = csv.writer(open("base_teste_json.json", "w"))

row = []

for status in tweepy.Cursor(api.search, q="#twitter").items():
    print(status)


statuses = tweepy.Cursor(api.search.q="#Orlando", since="2017-03-05", until="2017-03-13", lang="pt").items()


while True:
    try:
        status = statuses.next()
        print (status)
    except tweepy.TweepError:
        print("Aguarde 15 minutes")
        time.sleed(60*15)
        continue
    except StopIteration:
        print ("Acabou")
        break
        