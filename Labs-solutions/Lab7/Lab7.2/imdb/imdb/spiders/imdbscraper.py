# -*- coding: utf-8 -*-
import scrapy


class ImdbscraperSpider(scrapy.Spider):
    name = 'imdbscraper'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0096463/fullcredits/',
                  # 'https://www.imdb.com/name/nm0000228/?ref_=ttfc_fc_cl_t10'
                  ]

    def parse(self, response):
        actors = response.xpath('//table[@class = "cast_list"]//tr').extract()
        # response.xpath('//td[not(@class)]/a').extract()

        firstline = True
        for actor in actors:
            if len(actor.split("alt=")) > 1:
                yield {

                    'movie_id': response.xpath('//meta[@property = "pageId"]/@content').extract_first(),
                    'movie_name': response.css('title::text').get().strip().split(' (')[0],
                    'movie_year': response.xpath('normalize-space(//span[@class = "nobr"])').extract_first(),
                    'actor_name': actor.split("alt=")[1].split("title")[0].replace('"', '').strip(),
                    'actor_id': actor.split("name/")[1].split("/")[0],

                    #'role_name': actor.split("<td>")[1].split("/characters")[1].split(">")[1].split("<")[0]
                }
