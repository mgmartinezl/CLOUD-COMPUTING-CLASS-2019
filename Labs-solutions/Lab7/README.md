# Lab 7 answers

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

