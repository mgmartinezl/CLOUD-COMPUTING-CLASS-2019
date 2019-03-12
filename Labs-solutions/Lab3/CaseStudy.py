import json
from collections import Counter
from TwitterAnalyzer import preprocess, stop

fname = 'MachineLearning.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        if len(line) > 3:
            tweet = json.loads(line)
            # Create a list with all the terms
            terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#') and term not in stop]
            count_all.update(terms_hash)
    # Print the first 10 most frequent words
    print(count_all.most_common(15))

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (6,6)
import matplotlib.pyplot as plt

sorted_x, sorted_y = zip(*count_all.most_common(15))
print(sorted_x, sorted_y)

plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
plt.axis('tight')

#plt.show()
plt.savefig('CaseStudy.png')
