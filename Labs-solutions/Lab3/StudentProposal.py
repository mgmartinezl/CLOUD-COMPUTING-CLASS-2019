import os
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from TwitterAnalyzer import *


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('DonaldTrump.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


consumer_key = os.environ['CONSUMER-KEY']
consumer_secret = os.environ['CONSUMER-SECRET']
access_token = os.environ['ACCESS-TOKEN']
access_secret = os.environ['ACCESS-SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['Trump', 'Donald', 'DonaldTrump', 'POTUS'])

stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', '’', 'I', '…']

with open('DonaldTrump.json', 'r') as f:
    count_tokens = Counter()
    count_hash = Counter()
    count_freq_terms = Counter()
    for line in f:
        if len(line) > 2:
            tweet = json.loads(line)
            tokens = preprocess(tweet['text'])
            hash_tags = [term for term in preprocess(tweet['text']) if term.startswith('#')]
            terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#', '@'))]
            # Update the counters
            count_tokens.update(tokens)
            count_hash.update(hash_tags)
            count_freq_terms.update(terms_only)
        #print(count_tokens.most_common(5))
        print(count_hash.most_common(5))
        print(count_freq_terms.most_common(5))

