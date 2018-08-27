# Author: Asad Iqbal
# Project: Dice Analytics Big Data
# Coding UTF-8

# =============================================================================
#                           IMPORT REQUIRED LIBRARIES
import tweepy
import json
import time
import datetime
# =============================================================================
# Variables for authentication purposes of the Twitter application
consumer_key = "****************************"
consumer_secret = "****************************"
access_key = "****************************"
access_secret = "****************************"
# Hashtag to search and fetch from Twitter
accountvar = "MotoGP"
# print "searching for "+accountvar
# Get the current date and time
t = datetime.datetime.now()
# sorting the acquired date and time into the format we require
a = t.strftime('%Y-%m-%d-%H-%M')
#specifics of the generated output file name
outputfilejson = accountvar+"_"+str(a)+".json"
#Listener class responsible of reciveiving the data
class StdOutListener(tweepy.StreamListener):
# StdOutListener will be called before any of the others once the connection with the Twitter API is made.
    def __init__(self, time_limit=60):
        #set the current time as start time
        self.start_time = time.time()
        #set time limiter to pause stream.Current time limit is 60 seconds
        self.limit = time_limit
        super(StdOutListener, self).__init__()
        # defining the on_data function, this will tell the compiler what to do whenever new data is recieved.
    def on_data(self, data):
        #setting the time limit checker. It will let the stream fetch data as long as the tiem limit has not been reached
        if(time.time() - self.start_time) < self.limit:
            # Loading the fetched encoded JSON tweet into the decoded variable
            print ("data: ", data)
            decoded = json.loads(data)
            try:
                if isinstance(decoded, dict):
                    # decoding the json tweet and loading it in decoded.
                    decoded = json.dumps(decoded)
                    # writing the decoded tweet into the output file
                    outfile.write(decoded)
                    # add a new line after the tweet into the output so that JSON SerDe can read it
                    outfile.write('\n')
                    #print the fetched data into the output file
                    print decoded+'\n'
                    #handling excptions in case there is some error
            except(NameError, KeyError, AttributeError):
                pass
            return True
            # Once the time limit is reached , disconnect the stream
        else:
            time.sleep(10)
            stream.disconnect()
            return False
    # Check for any possibility in connection error with the Twitter API
    def on_error(self, status):
        # display error
        print status
# ======================== MAIN =======================
# Main method , this will always be called first when the code executes
# Initializing authenticity here
if __name__ == '__main__':
    #call the listener class
    l = StdOutListener()
    # authorization handler of the Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    # create a new output file and open it in write back mode
    with open(outputfilejson, 'wb') as outfile:
        print "Showing all new tweets for " + accountvar
        # Initialize the stream with Twitter API
        stream = tweepy.Stream(auth, l)
        # search and filter for the required hashtag
        stream.filter(track=[str("#"+accountvar)])
