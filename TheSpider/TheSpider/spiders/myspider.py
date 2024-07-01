import scrapy


class ThespiderSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        "https://books.toscrape.com/catalogue/page-2.html"
    ]

    def parse(self, response):

        data = {}
        books = response.css('ol.row')
        for book in books:
            for b in book.css('article.product_pod'):
                yield {
                    'Title': b.css('a::attr(title)').getall(),
                    'Price': b.css('div.product_price p.price_color::text').getall()
                }


                # stari nacin
                # data['Title'] = b.css('a::attr(title)').getall()
                # data['Price'] = b.css('div.product_price p.price_color::text').getall()
                # yield data

