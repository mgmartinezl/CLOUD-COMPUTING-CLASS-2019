# -*- coding: utf-8 -*-
import scrapy


class ImdbscraperSpider(scrapy.Spider):
    name = 'imdbscraper'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0096463/fullcredits/']

    def parse(self, response):
        pass
        print(response.css('title::text').get().strip().split(' (')[0])
