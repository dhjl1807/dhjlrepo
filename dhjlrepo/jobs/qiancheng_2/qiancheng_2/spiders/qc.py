# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QcSpider(CrawlSpider):
    name = 'qc'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000%252C00,000000,0000,00,9,99,python,2,1.html']
    page_link = LinkExtractor(restrict_xpaths='//div[@class="dw_page"]//li[@class="bk"]')
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="el"]/p[@class="t1 "]/span'), callback='parse_item', follow=False),
        Rule(page_link, follow=True),
    )

    def parse_item(self, response):
        item = {}
        url = response.xpath('//div[@class="tHeader tHjob"]/div[@class="in"]/div[@class="cn"]')
        item['job_name'] = url.xpath('./h1/@title').get()
        item['job_company'] = url.xpath('./p[@class="cname"]/a/@title').get()
        w = url.xpath('./p[@class = "msg ltype"]')[0].attrib.get('title')
        item['job_addr'] = w.split('|')[0].strip()
        item['job_experience'] = w.split('|')[1].strip()
        item['job_edu'] = w.split('|')[2].strip()
        item['job_salary'] = url.xpath('./strong/text()').extract_first()

        yield item



