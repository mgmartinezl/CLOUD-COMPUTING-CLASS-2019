# Lab 8 answers

## Names: Sara Díaz - Gabriela Martinez

### Classify images

The script ImageAnalyzer.py was created as follows and can be accessed [here](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab8/cloud-vision/ImageAnalyzer.py). This code, through the _annotate_ and _report_ classes extracts the URL of the first 100 images found in a generic URL, which then are processed by the cloud vision API from Google that extracts potential labeling and corresponding probabilities for each picture. Furthermore, this codes also generates a word cloud with the most frequent terms associated to the pictures found.

```
from google.cloud.vision import types
from google.cloud import vision
from bs4 import BeautifulSoup
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
import argparse

client = vision.ImageAnnotatorClient()
web_detections = []
myList = []


def annotate(path):
    site = path
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    count = 0
    for url in urls:
        if count < 100:
            if url.startswith('http') or url.startswith('gs:'):
                image = types.Image()
                image.source.image_uri = url
                web_detection = client.web_detection(image=image).web_detection
                count = count + 1
                web_detections.append(web_detection)
    return web_detections


def report(annotations):
    if annotations.web_entities:
        print('\n{} Web entities found: '.format(
              len(annotations.web_entities)))
        for entity in annotations.web_entities:
            print('Description: {}'.format(entity.description.encode('utf8')))
            print('Score      : {}'.format(entity.score))
            descrip = entity.description.encode('utf8')
            myList.append(descrip)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('image_url')
    parser.add_argument('wc_name')
    args = parser.parse_args()
    container = annotate(args.image_url)
    for i in container:
        report(i)
    wordcount = Counter(myList)
    wordcloud = WordCloud(background_color="white").generate_from_frequencies(wordcount)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    wordcloud.to_file(args.wc_name)
```

To run the previous code from the command line, we passed as parameters:
* The URL to process
* The name of PNG file to be generated from the search.

The examples run were the following and considered three different URLs that contained images about dogs, cats and pandas:
```
python ImageAnalyzer.py "https://pixabay.com/fr/images/search/dogs/" "wordCloudDogs.png"
python ImageAnalyzer.py "https://pixabay.com/fr/images/search/cats/" "wordCloudCats.png"
python ImageAnalyzer.py "https://pixabay.com/fr/images/search/pandas/" "wordCloudPandass.png"
```

The corresponding word clouds to each URL were:
![Dogs](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab8/cloud-vision/wordCloudDogs.png)  
![Cats](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab8/cloud-vision/wordCloudCats.png)  
![Pandas](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab8/cloud-vision/wordCloudPandas.png)  
