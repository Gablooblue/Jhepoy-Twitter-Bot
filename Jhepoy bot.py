import tweepy, time, sys

#Replace these fields with the specified information
CONSUMER_KEY = 'PUT CONSUMER KEY HERE'
CONSUMER_SECRET = 'PUT SECRET CONSUMER KEY HERE'
ACCESS_KEY = 'PUT ACCESS KEY HERE'
ACCESS_SECRET = 'PUT SECRET ACCESS KEY HERE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    for x in range (0,4):
        api.update_status("TANGINA MO JHEPOY DIZON")
        time.sleep(900)
    api.update_status("ANG PANGIT NG PAGMUMUKHA MO")    
