import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['example.com']  # Domínio inicial
    start_urls = ['http://example.com']  # URL inicial

    def parse(self, response):
        # Extrair todos os links da página
        links = response.css('a::attr(href)').getall()

        # Processar os links
        for link in links:
            yield {
                'url': link,
                'content': response.css('::text').get()
            }

        # Recursivamente seguir links por até 5 níveis
        if self.depth < 5:
            for link in links:
                yield response.follow(link, self.parse, cb_kwargs={'depth': self.depth + 1})
