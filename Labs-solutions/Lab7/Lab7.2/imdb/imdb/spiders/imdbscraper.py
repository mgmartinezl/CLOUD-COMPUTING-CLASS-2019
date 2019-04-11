# -*- coding: utf-8 -*-
import scrapy


class ImdbscraperSpider(scrapy.Spider):
    name = 'imdbscraper'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/']

    def parse(self, response):
        pass
