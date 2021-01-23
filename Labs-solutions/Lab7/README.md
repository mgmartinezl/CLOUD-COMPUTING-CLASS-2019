# Lab 7 - Web Scrapping

## Names: Sara Díaz - Gabriela Martinez

### Task 7.1: Extract selected information from a newspaper webpage
#### Q71: Add the above code to your scrapy-lab repository. Add the nytimes.json, containing the output of your execution, to the Lab7 folder of your answers repository. 

The link to our repository for this task: https://github.com/sdiazben/scrapy-lab
The json file can be found here: https://github.com/sdiazben/scrapy-lab/blob/master/nytscraper/nytimes.json

A preview from the file is as follows:
```
[
{"section": "Briefings", "appears_ulr": "https://www.nytimes.com/", "title": "Listen to 'The Daily'", "article_url": "https://www.nytimes.com/2019/04/11/podcasts/the-daily/netanyahu-israel-election-trump-palestinians.html", "summary": "Benjamin Netanyahu won. The two-state solution lost."},
{"section": "Briefings", "appears_ulr": "https://www.nytimes.com/", "title": "The 'In Her Words' Newsletter", "article_url": "https://www.nytimes.com/2019/04/09/sports/soccer/abby-wambach-soccer-wolfpack.html", "summary": "Abby Wambach's leadership lessons: Be the wolf."},
{"section": "Briefings", "appears_ulr": "https://www.nytimes.com/", "title": "The Book Review Podcast", "article_url": "https://www.nytimes.com/2019/04/05/books/review/podcast-midnight-in-chernobyl-nuclear-accident-adam-higginbotham.html", "summary": "Adam Higginbotham talks about his new history of the Chernobyl disaster."},
{"section": "Top Stories", "appears_ulr": "https://www.nytimes.com/", "title": "Do You Know Who's Watching You?", "article_url": "https://www.nytimes.com/interactive/2019/opinion/internet-privacy-project.html", "summary": "As companies and governments gain new powers to follow people across the internet and around the world, the boundaries of privacy are in dispute.The Times is embarking on this months-long Opinion project to explore the technology and where it's taking us."},
{"section": "Top Stories", "appears_ulr": "https://www.nytimes.com/", "title": "Your Neighbor's Doorbell Is Judging You", "article_url": "https://www.nytimes.com/interactive/2019/04/10/opinion/internet-data-privacy.html", "summary": "Facial recognition technology is spreading fast, with alarming consequences."},
{"section": "Top Stories", "appears_ulr": "https://www.nytimes.com/", "title": "When it comes to your privacy, where would you draw the line?", "article_url": "https://www.nytimes.com/interactive/2019/04/10/opinion/privacy-survey.html", "summary": ""},
{"section": "Top Stories", "appears_ulr": "https://www.nytimes.com/", "title": "Julian Assange, WikiLeaks Founder, Is Arrested in London", "article_url": "https://www.nytimes.com/2019/04/11/world/europe/julian-assange-wikileaks-ecuador-embassy.html", "summary": "Mr. Assange took refuge in the Ecuadorean Embassy in 2012. He faces a British charge of skipping bail and is wanted in the United States on charges of releasing secret documents."}
]
```

### Task 7.2: Obtain a subset of the movie industry to do some research
#### Q72: Add the code of the new spider your scrapy-lab repository. Add the imdb.json, containing the output of your execution, to the Lab7 folder of your answers repository. 

The new code for the scraper is as follows and can be found at: https://github.com/sdiazben/scrapy-lab/tree/master/imdb/spiders

```
# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class ImdbscraperSpider(scrapy.Spider):
    name = 'imdbscraper'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0096463/fullcredits/']

    def parse(self, response):
        actors = response.xpath('//table[@class = "cast_list"]//tr').extract()
        movie_year = str(
            response.xpath('normalize-space(//span[@class = "nobr"])').extract_first().replace("(", "").replace(")",
                                                                                                                ""))
        for actor in actors:
            if movie_year.find("198") == 0:
                if len(actor.split("<td>")) > 1:
                    if len(actor.split("<td>")[1].split('character">'))>1:
                        if len(actor.split("<td>")[1].split('character">')[1].split("\n")) > 1:
                                if len(actor.split("<td>")[1].split('character">')[1].split("\n")[1].split(">")) > 1:
                                    role_n = actor.split("<td>")[1].split('character">')[1].split("\n")[1].strip().split(">")[1].split("<")[0]
                                else:
                                    role_n = actor.split("<td>")[1].split('character">')[1].split("\n")[1].strip()
                        else:
                            role_n = actor.split("<td>")[1].split('character">')[1].strip().split(" \n")[0]
                else:
                    role_n = ""

                if len(actor.split("alt=")) > 1:
                    yield {

                        'movie_id': response.xpath('//meta[@property = "pageId"]/@content').extract_first(),
                        'movie_name': response.css('title::text').get().strip().split(' (')[0],
                        'movie_year': str(response.xpath('normalize-space(//span[@class = "nobr"])').extract_first()
                            .replace("(", "").replace(")", ""))[:4],
                        'actor_name': actor.split("alt=")[1].split("title")[0].replace('"', '').strip(),
                        'actor_id': actor.split("name/")[1].split("/")[0],
                        'role_name': role_n
                    }

                    # Create request
                    url = "https://" + self.allowed_domains[0] + actor.split('href="')[1].split('"')[0]

                    yield response.follow(url, callback=self.parse_actor)

    def parse_actor(self, response):
        # yield {'birth_date':
        # response.xpath('//script[@type = "application/ld+json"]').extract_first().split('"birthDate":')[1].split('"')[1]}

        movies = response.xpath('//div[@class = "filmo-category-section"]/div').extract()


        for movie in movies:
            if str(movie.split('"year_column">')[1].split("\n")[1]).strip().find("198") == 0 and "actor" in str(movie):
                url = "https://" + self.allowed_domains[0] + movie.split('href="')[1].split('"')[0]
                yield Request(url, callback=self.parse)
```

The imdb json file is within this repository at: https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/Lab7.2/imdb/imdb.json

A preview of the json file is as follows:
```
[
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Harrison Ford", "actor_id": "nm0000148", "role_name": "Jack Trainer"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Sigourney Weaver", "actor_id": "nm0000244", "role_name": "Katharine Parker"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Melanie Griffith", "actor_id": "nm0000429", "role_name": "Tess McGill"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Alec Baldwin", "actor_id": "nm0000285", "role_name": "Mick Dugan"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Joan Cusack", "actor_id": "nm0000349", "role_name": "Cyn"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Philip Bosco", "actor_id": "nm0097842", "role_name": "Oren Trask"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Nora Dunn", "actor_id": "nm0004887", "role_name": "Ginny"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Oliver Platt", "actor_id": "nm0001624", "role_name": "Lutz"}
]
```

### Task 7.3: Study the obtained data using the Elastic Stack
#### Q73: Take a screenshot of the Kibana Dashboard showing the above plots without filters. Set a couple of filters, take screetshots. Add all the screenshots to the Lab7 folder of your answers repository.

For this task, we used the following Python script to connect to Elasticsearch and load the json file into a new Kibana index:

```
from elasticsearch import Elasticsearch, helpers
import os
import uuid
import json

ELASTIC_API_URL_HOST = os.environ['ELASTIC_API_URL_HOST']
ELASTIC_API_URL_PORT = os.environ['ELASTIC_API_URL_PORT']
ELASTIC_API_USERNAME = os.environ['ELASTIC_API_USERNAME']
ELASTIC_API_PASSWORD = os.environ['ELASTIC_API_PASSWORD']

es = Elasticsearch(host=ELASTIC_API_URL_HOST,
                   scheme='https',
                   port=ELASTIC_API_URL_PORT,
                   http_auth=(ELASTIC_API_USERNAME, ELASTIC_API_PASSWORD))

count = 1
for file in os.listdir("C:\\Users\\gabim\\PycharmProjects\\elasticsearchScraper"):
    if file.endswith('.json'):
        json_file = open(file).read()
        print(json_file)
        data = json.loads(json_file)
        if len(data)>1:
            for d in data:
                es.index(index='imdb', doc_type='json', id=uuid.uuid4(), body=d)

es.indices.refresh(index='imdb')

if es.indices.exists(index="imdb"):
    print("idbm index exists!")
```

The following dashboard was created using the Elasticsearch and Kibana 6.7 cloud version:
![Dashboard](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/MoviesDashboard.PNG)

We applied some filters on it to explore behavior:
* First, we wanted to know all the information related to movies and years in which Frank Welter took place, the actor with the highest number of records according to the tag cloud.
![Frank](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/FrankWelker_Filter.PNG)
![FrankMovies](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/FrankWelker_Filter2.PNG)

* Additionally, we also filtered the information for the movie "Working Girl":
![WorkingGirl](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/WorkingGirl_Filter.PNG)

* Finally, we looked for movies filmed in 1982:
![1982](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/1982Movies_Filter.PNG)

### What is your question? 
#### "Which are the most common star signs of the actors for the time period studied?"
Change the code according to your question, create a new view and add it to the Dashboard. Take a screenshot of the new plot.

To answer this question, our scraper code has changed to the following and can be found at: https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/Lab7.3/imdb/imdb/spiders/imdbscraper2.py

```
# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.item import Item

# Class item to pass information between requests
class MyItem(Item):
    movie_id = scrapy.Field()
    movie_name = scrapy.Field()
    movie_year = scrapy.Field()
    actor_name = scrapy.Field()
    actor_id = scrapy.Field()
    role_name = scrapy.Field()
    star_sign = scrapy.Field()

#Script with modifications
class Imdbscraper2Spider(scrapy.Spider):
    name = 'imdbscraper2'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0096463/fullcredits/']

    #Parse movie page
    def parse(self, response):
        actors = response.xpath('//table[@class = "cast_list"]//tr').extract()
        movie_year = str(
            response.xpath('normalize-space(//span[@class = "nobr"])').extract_first().replace("(", "").replace(")",
                                                                                                                ""))
        for actor in actors:

            if movie_year.find("198") == 0:
                if len(actor.split("<td>")) > 1:
                    if len(actor.split("<td>")[1].split('character">')) > 1:
                        if len(actor.split("<td>")[1].split('character">')[1].split("\n")) > 1:
                            if len(actor.split("<td>")[1].split('character">')[1].split("\n")[1].split(">")) > 1:
                                role_n = \
                                    actor.split("<td>")[1].split('character">')[1].split("\n")[1].strip().split(">")[
                                        1].split("<")[0]
                            else:
                                role_n = actor.split("<td>")[1].split('character">')[1].split("\n")[1].strip()
                        else:
                            role_n = actor.split("<td>")[1].split('character">')[1].strip().split(" \n")[0]
                else:
                    role_n = ""

                if len(actor.split("alt=")) > 1:
                    url = "https://" + self.allowed_domains[0] + actor.split('href="')[1].split('"')[0]

                    item = MyItem()
                    scrap_other_movie = Request(url, callback=self.parse_movie)

                    item["movie_id"] = response.xpath('//meta[@property = "pageId"]/@content').extract_first()
                    item['movie_name'] = response.css('title::text').get().strip().split(' (')[0]
                    item['movie_year'] = str(response.xpath('normalize-space(//span[@class = "nobr"])').extract_first()
                                         .replace("(", "").replace(")", ""))[:4]
                    item['actor_name'] = actor.split("alt=")[1].split("title")[0].replace('"', '').strip()
                    item['actor_id'] = actor.split("name/")[1].split("/")[0]
                    item['role_name'] = role_n

                    scrap_other_movie.meta['item'] = item
                    yield scrap_other_movie

    # Parse actor additional info. (star sign) and get his/her movies
    def parse_movie(self, response):
        item = response.meta['item']
        item['star_sign'] = response.xpath('normalize-space(//div[@id = "dyk-star-sign"]/a)').extract_first()
        yield item

        movies = response.xpath('//div[@class = "filmo-category-section"]/div').extract()

        for movie in movies:
            if str(movie.split('"year_column">')[1].split("\n")[1]).strip().find("198") == 0 and "actor" in str(movie):
                url = "https://" + self.allowed_domains[0] + movie.split('href="')[1].split('"')[0]
                yield Request(url, callback=self.parse)
```

A preview the new json file, which is available at: https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/Lab7.3/imdb/imdb2.json, is as follows:

```
[
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Philip Bosco", "actor_id": "nm0097842", "role_name": "Oren Trask", "star_sign": "Libra"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "James Lally", "actor_id": "nm0482466", "role_name": "Turkel", "star_sign": "Libra"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Oliver Platt", "actor_id": "nm0001624", "role_name": "Lutz", "star_sign": "Capricorn"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Nora Dunn", "actor_id": "nm0004887", "role_name": "Ginny", "star_sign": "Taurus"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Alec Baldwin", "actor_id": "nm0000285", "role_name": "Mick Dugan", "star_sign": "Aries"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Harrison Ford", "actor_id": "nm0000148", "role_name": "Jack Trainer", "star_sign": "Cancer"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Amy Aquino", "actor_id": "nm0032628", "role_name": "Alice Baxter", "star_sign": "Pisces"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Sigourney Weaver", "actor_id": "nm0000244", "role_name": "Katharine Parker", "star_sign": "Libra"},
{"movie_id": "tt0096463", "movie_name": "Working Girl", "movie_year": "1988", "actor_name": "Olympia Dukakis", "actor_id": "nm0001156", "role_name": "Personnel Director", "star_sign": "Gemini"}
]
```

Similarly to what we did before, we uploaded this new json file to Elasticsearch and Kibana to obtain or new plot to answer our question:

![Signs](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab7/Star_Signs.PNG)

From the previous, we can see that Leo and Aquarius are the most popular signs (both with more than 10% of share amongst the actors), followed by Aries and Cancer with approximately 9% of the cast belonging to them.

#### Q75: How long have you been working on this session? What have been the main difficulties you have faced and how have you solved them?
We have been working on this assignment a total of 15 hours. Main difficulties have been related to:
* Understanding how to access html code with scrapy for specific use cases (such as the nytimes page or the imdb website).
* Connecting successfully to Elasticsearch and creating the index patterns in Kibana
* Understanding how Kibana manages visualizations.
