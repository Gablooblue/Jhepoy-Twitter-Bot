import tweepy, time, sys, datetime

#Replace these fields with the specified information
CONSUMER_KEY = 'PUT CONSUMER KEY HERE'
CONSUMER_SECRET = 'PUT SECRET CONSUMER KEY HERE'
ACCESS_KEY = 'PUT ACCESS KEY HERE'
ACCESS_SECRET = 'PUT SECRET ACCESS KEY HERE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

cur_time = datetime.datetime.now()
cur_time = cur_time.strftime("%H:%M")

while True:
        api.update_status("TANGINA MO JHEPOY DIZON" " - " + cur_time) 
        time.sleep(1800)
        api.update_status("ANG PANGIT NG PAGMUMUKHA MO" + " - " + cur_time)
        time.sleep(1800)
        api.update_status("NAKITA MO NA BA MUKHA MO SA SALAMIN" + " - " + cur_time)
        time.sleep(1800)
        api.update_status("TINGNAN MO NGA BAHAY KO, VILLAGE YAN" + " - " + cur_time)
        time.sleep(1800)
        api.update_status("MAG-EXTEND KA NA DIYAN, TIME KA NA EH" + " - " + cur_time)
        time.sleep(1800)
