# -*- coding: utf-8 -*-
import scrapy


class ImdbscraperSpider(scrapy.Spider):
    name = 'imdbscraper'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0096463/fullcredits/']

    def parse(self, response):
        pass
        yield {
            'movie_id': response.xpath('//meta[@property = "pageId"]/@content').extract_first(),
            'movie_name': response.css('title::text').get().strip().split(' (')[0],
            'movie_year':response.css('title::text').get().split(' (')[1].split(')')[0],

              }
