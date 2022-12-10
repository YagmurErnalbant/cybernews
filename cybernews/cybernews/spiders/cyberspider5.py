import scrapy


class Cyberspider5Spider(scrapy.Spider):
    name = 'cyberspider5'
    start_urls = ['http://www.bleepingcomputer.com/']

    def parse(self, response):
        for bleepin in response.css('div.bc_latest_news_text'):
            yield  {
                'Date Published': bleepin.css('li.bc_news_date::text').get(),
                ' ': bleepin.css('div.bc_latest_news_text h4 a::text').get(),
                'Description': bleepin.css('div.bc_latest_news_text p::text').get(),
                'Link': bleepin.css('div.bc_latest_news_text h4 a::attr(href)').get(),
            }

