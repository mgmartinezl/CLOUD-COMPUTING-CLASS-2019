from scrapy import cmdline

cmdline.execute("scrapy crawl imdbscraper2 -o imdb2.json".split())