import sys
from twython import Twython
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


#This is default hashtag
HASH_TAG = u'#asahikawa_python'

if __name__ == '__main__':
    api.update_status(status=sys.argv[1])


