import json
import re
import string
from collections import Counter
from nltk.corpus import stopwords

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT']


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


with open('ArtificialIntelligenceTweets.json', 'r') as f:
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
        print(count_tokens.most_common(10))
        print(count_hash.most_common(10))
        print(count_freq_terms.most_common(10))






