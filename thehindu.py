# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:16:10 2020

@author: Akshay-Laptop
"""


import scrapy
class QuotestutorialItem(scrapy.Item):
    news=scrapy.Field()
    

class QuoteSpider(scrapy.Spider):
    name='the_hindu'
    start_urls=['https://www.thehindu.com/business/Economy/']
    
    def parse(self,response):
        
        items=QuotestutorialItem()
        
            
        news=response.xpath('//div[@class="Other-StoryCard"]/a/text()').extract()
        
        items['news']=news
        
        yield items

