import scrapy


class WatchapediaSpider(scrapy.Spider):
    name = "watchapedia"
    allowed_domains = ["pedia.watcha.com"]
    start_urls = ["https://pedia.watcha.com"]

    def parse(self, response):
        pass
