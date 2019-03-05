import nltk
nltk.download('punkt')
nltk.download('stopwords')
from collections import Counter
from nltk.corpus import stopwords
import re


def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
       text = tf.read()
       lowers = text.lower()
       no_punctuation = re.sub(r'[^\w\s]', '', lowers)
       tokens = nltk.word_tokenize(no_punctuation)
       # the lambda expression below this comment
       # stores stopwords in a variable for eficiency:
       # it avoids retrieving them from ntlk for each iteration
       sw = stopwords.words('english')
       filtered = [w for w in tokens if not w in sw]
       count = Counter(filtered)
       return count


tokens = get_tokens()
count = Counter(tokens)
print(count.most_common(10))
print(len(count))