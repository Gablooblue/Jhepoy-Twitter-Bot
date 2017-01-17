import tweepy, time, sys, datetime

#Replace these values
CONSUMER_KEY = 'PUT CONSUMER KEY HERE'
CONSUMER_SECRET = 'PUT SECRET CONSUMER KEY HERE'
ACCESS_KEY = 'PUT ACCESS KEY HERE'
ACCESS_SECRET = 'PUT SECRET ACCESS KEY HERE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	cur_time = datetime.datetime.now()
	cur_time = cur_time.strftime("%H:%M")
	api.update_status("It's " + cur_time + " and it's time to beat energy gap ")
	sleep(900)
