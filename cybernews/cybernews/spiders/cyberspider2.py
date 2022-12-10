import scrapy

class Cyberspider2Spider(scrapy.Spider):
    name = 'cyberspider2'
    start_urls = ['https://cyware.com/category/malware-and-vulnerabilities-news']

    def parse(self, response):
        for articles in response.css('div.cy-panel__body'):
                yield {
                    'Date Published': articles.css('span.cy-card__meta::text').get(),
                    ' ': articles.css('h1.cy-card__title::text').get().replace('\n', ' '),
                    'Description': articles.css('div.cy-card__description::text').get(),
                    'Link': articles.css('a[target=_blank]').attrib['href'],
                }
