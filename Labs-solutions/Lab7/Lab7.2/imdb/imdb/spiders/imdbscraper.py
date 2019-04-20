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
                        'movie_year': response.xpath('normalize-space(//span[@class = "nobr"])').extract_first()
                            .replace("(", "").replace(")", ""),
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
