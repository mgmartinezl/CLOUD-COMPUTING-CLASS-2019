from scrapy import cmdline

cmdline.execute("scrapy crawl imdbscraper -o imdb.json".split())