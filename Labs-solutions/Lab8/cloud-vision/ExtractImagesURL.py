from google.cloud import vision
from google.cloud.vision import types
from bs4 import BeautifulSoup
import requests
import argparse
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

client = vision.ImageAnnotatorClient()
web_detections = []


def annotate(path):
    site = path
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    count = 0
    for url in urls:
        if count < 2:
            if url.startswith('http') or url.startswith('gs:'):
                image = types.Image()
                image.source.image_uri = url
                web_detection = client.web_detection(image=image).web_detection
                count = count + 1
                web_detections.append(web_detection)
    return web_detections


myList = []


def report(annotations):
    if annotations.web_entities:
        print('\n{} Web entities found: '.format(
              len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description.encode('utf8')))
            descrip = entity.description.encode('utf8')
            myList.append(descrip)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    path_help = str('The image to detect, can be web URI, '
                    'Google Cloud Storage, or path to local file.')
    parser.add_argument('image_url', help=path_help)
    args = parser.parse_args()

    container = annotate(args.image_url)
    for i in container:
        report(i)
    wordcount = Counter(myList)
    print(wordcount)
    wordcloud = WordCloud(background_color="white").generate_from_frequencies(wordcount)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    wordcloud.to_file("commonWords.png")



