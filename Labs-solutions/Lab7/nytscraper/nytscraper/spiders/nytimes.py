# -*- coding: utf-8 -*-
import scrapy
import unidecode
import re

cleanString = lambda x: '' if x is None else unidecode.unidecode(re.sub(r'\s+',' ',x))

class NytimesSpider(scrapy.Spider):
    name = 'nytimes'
    allowed_domains = ['www.nytimes.com']
    start_urls = ['http://www.nytimes.com/']

    def parse(self, response):
        for article in response.css("section.top-news article.story"):
            yield {
                'section': section_name,
                'appears_ulr': response.url,
                'title': cleanString(article.css('a h2::text, a h2 span::text').extract_first()),
                'article_url': response.url[:-1] + article.css('a::attr(href)').extract_first(),
                'summary': cleanString(''.join(article.css('p::text, ul li::text').extract())),
            }