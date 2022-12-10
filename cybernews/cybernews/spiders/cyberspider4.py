import scrapy


class Cyberspider4Spider(scrapy.Spider):
    name = 'cyberspider4'
    start_urls = ['http://thehackernews.com/']

    def parse(self, response):
        for hackernews in response.css('div.body-post'):
                yield {
                    'Date Published': hackernews.css('div.item-label::text').get(),
                    ' ': hackernews.css('div.clear h2.home-title::text').get(),
                    'Description': hackernews.css('div.home-desc::text').get(),
                    'Link': hackernews.css('a::attr(href)').get(),
                } 
