import scrapy
from scrapy.loader import ItemLoader
from noticias.items import QuotesItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css("div.quote")

        for q in quotes:
            loader = ItemLoader(item=QuotesItem(), selector=q)
            loader.add_css("author", ".author::text")
            loader.add_css("quote", ".text::text")
            loader.add_css("tags", ".tag::text")

            yield loader.load_item()

        for a in response.css("li.next a::attr(href)"):
            yield response.follow(a, self.parse)