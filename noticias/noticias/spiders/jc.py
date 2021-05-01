import scrapy, json
from noticias.items import NoticiasItem
from scrapy.loader import ItemLoader


class JcSpider(scrapy.Spider):
    name = 'jc'
    allowed_domains = ['jc.ne10.uol.com.br/']
    start_urls = ['http://jc.ne10.uol.com.br/']

    def parse(self, response):
        noticias = response.css("article")

        for noticia in noticias:
            loader = ItemLoader(item=NoticiasItem(), selector=noticia)
            loader.add_css("titulo", "h1.title::text")
            loader.add_css("tema", "span.hat::text")

            yield loader.load_item()
