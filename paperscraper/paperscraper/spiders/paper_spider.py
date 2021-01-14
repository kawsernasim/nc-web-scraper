# -*- coding: utf-8 -*-
import scrapy
from ..items import *


class PaperSpider(scrapy.Spider):
    name = 'paper_spider'
    #allowed_domains = ['pastpapersz.com/']
    start_urls = ['http://www.pastpapersz.com/edexcel/igcse-mathematics-b/']

    def parse(self, response):
      items = PaperscraperItem()
      divs = response.css('div.one_half')
      for div in divs:
       title = div.css('h4::text').extract()
       link = div.css( 'a').xpath('@href').extract()

       items['title'] = year
       #items['papers']= paper
       #items['session'] = session
       items['link'] = link
       yield items
