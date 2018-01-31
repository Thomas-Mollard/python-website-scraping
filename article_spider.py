import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"
    start_urls = ['http://blog.theodo.fr/2018/02/scrape-websites-5-minutes-scrapy']

    def parse(self, response):
        content = response.xpath(".//div[@class='entry-content']/descendant::text()").extract()
        yield {'article': ''.join(content)}

