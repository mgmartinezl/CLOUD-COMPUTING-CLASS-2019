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
