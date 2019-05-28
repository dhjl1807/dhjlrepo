# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request

from city_json import parse_city


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com']
    citylists = parse_city()
    start_urls = ['https://www.zhipin.com/c' + cityID + '/?query=python&ka=sel-city-' + cityID for cityID in
                  ('100010000', '101010100', '101020100', '101280100', '101280600', '101210100', '101030100',
                   '101110100', '101190400', '101200100', '101230200', '101250100', '101270100', '101180100',
                   '101040100')]

    def parse(self, response):
        with open('bszp.html', 'wb') as f:
            f.write(response.body)

        li_nodes = response.xpath('//div[@class="job-list"]//ul/li')
        for li_node in li_nodes:
            item = {}
            item['job_name'] = li_node.xpath('.//div[@class="job-title"]/text()').extract_first()
            item['job_region'] = li_node.xpath('.//div[@class="info-primary"]//p/text()').extract_first()
            item['job_company'] = li_node.xpath(
                './/div[@class="info-company"]//h3[@class="name"]/a/text()').extract_first()

            job_ex_edu_t = li_node.xpath('.//div[@class="company-text"]/p/text()').extract()
            job_ex_edu = [x.strip() for x in job_ex_edu_t if x.strip() != '']
            if len(job_ex_edu) == 3:
                item['job_company_type'] = job_ex_edu[0].strip()
                item['job_company_financ'] = job_ex_edu[1].strip()
                item['job_company_pernum'] = job_ex_edu[2].strip()
            else:
                item['job_company_type'] = job_ex_edu[0].strip()
                item['job_company_financ'] = None
                item['job_company_pernum'] = job_ex_edu[1].strip()

            item['job_salary'] = li_node.xpath('.//h3[@class="name"]//span/text()').extract_first()
            item['job_exp'] = li_node.xpath('.//div[@class="info-primary"]//p/text()[2]').extract_first().strip()
            item['job_edu'] = li_node.xpath('.//div[@class="info-primary"]//p/text()[3]').extract_first()

            yield item

        page_url = response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract_first()
        page_url = 'https://www.zhipin.com' + page_url
        yield Request(page_url, callback=self.parse)

    print('-----爬取完成-----')
