import tweepy
import csv
import time

consumer_key = "wxEo63n98b9eVoCiMdzpfPOqe"
consumer_secret = "CQmUD9lZilXKHFHgKCZGZVuqjKh3Gi3nT0AWaT2AuFU34ohi3G"
access_token="840288921225437184-swOf0qeYK8kmR2ri2P9yxhyP7W6QsA9"
access_token_secret="DHXFavqiGBpPzDkDtXx18gOEmNzVHMsXrwZPrebGvSry5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

arquivo1 = csv.writer(open("base_teewts.csv", "w"))
# arquivo2 = open("base_teste_json.json", "w")

row = []

statuses = tweepy.Cursor(api.search, q="doria", since="2017-03-10", until="2017-03-15", lang="pt").items()
#, lang="pt"


while True:
  try:
    status = statuses.next()

    print(str(status).encode('ascii', 'ignore').decode('ascii'))
    #print("'" + str(status.encode("ascii")) + "'")


    # row = str(status.user.screen_name), str(status.created_at), str(status.text), status.geo
    row = str(str(status.text).encode('ascii', 'ignore').decode('ascii')), ""

    arquivo1.writerow(row)

    # arquivo2.write(str(status))
    # arquivo2.write("\n")

  except tweepy.TweepError as e:
    print (e.api_code)
    print("Aguarde 15 minutes")
    time.sleep(60*15)
    continue
  except StopIteration:
    print ("Acabou")
    break