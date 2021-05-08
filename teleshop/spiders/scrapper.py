import scrapy
from teleshop.items import TeleshopItem

class ScrapperSpider(scrapy.Spider):
    name = 'scrapper'
    allowed_domains = ['telefonesimportados.netlify.app']
    start_urls = ['https://telefonesimportados.netlify.app/']
    produto = '//*[@class="single-product-area"] /div[@class="container"]/div[@class="row"][1]//div[@class="col-md-3 col-sm-6"]'
    imagem = './div[@class="single-shop-product"]//div[@class="product-upper"]/img/@src'
    nome = './div[@class="single-shop-product"]//h2/a/text()'
    preço = './div[@class="single-shop-product"]//div[@class="product-carousel-price"]//ins/text()'
    nextt = '//a[@aria-label="Next"]/@href'
    

    def parse(self, response):
        for quote in response.xpath(self.produto):
            yield self.parse_item(quote)

        next_page = response.xpath(self.nextt).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, quote): 
        image = self.start_urls[0]+quote.xpath(self.imagem).extract_first(),
        nome = quote.xpath(self.nome).extract_first(),
        preço = quote.xpath(self.preço).extract_first(),        

        teleshopitem = TeleshopItem(nome=nome, image=image, preço=preço)
        return teleshopitem        