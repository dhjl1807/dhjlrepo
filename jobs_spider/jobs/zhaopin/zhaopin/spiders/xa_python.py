# -*- coding: utf-8 -*-
import json
import logging
import random

import scrapy
from scrapy import Request


class XaPythonSpider(scrapy.Spider):
    name = 'xa_python'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['https://sou.zhaopin.com/?jl=' + cityID + '&kw=python&kt=3'
                  for cityID in
                  ('530', '538', '765', '763', '531', '801', '653', '736', '854', '635', '719', '551', '703', '749',
                   '639', '681', '565', '613', '600', '682', '636', '622', '664', '654', '773', '702', '576', '655')]

    keywords = ['python', '数据', '数据', '算法', '人工智能', 'jango', 'lask', '运维']
    page = 0

    def parse(self, response):
        # 保存网页
        # with open('zhaopin.html', 'wb') as f:
        #     f.write(response.body)

        item = {}
        # 解析数据
        jobs_div = '//div[@class="contentpile__content__wrapper clearfix"]'
        job_nodes = response.xpath(jobs_div)

        for job_node in job_nodes:
            job_a = job_node.xpath('.//a[1]')[0]
            # job_href = job_a.xpath('./@href').extract_first()

            job_name_xpath = './/span[@class="contentpile__content__wrapper__item__info__box__jobname__title"]/text()'
            job_name = job_a.xpath(job_name_xpath).extract_first()
            if not job_name:
                item['job_name'] = None
            else:
                if not [kw for kw in self.keywords if kw in job_name]:
                    # if 'python' in job_name or 'Python' in job_name \
                    #         or '数据' in job_name or '算法' in job_name \
                    #         or '人工智能' in job_name or 'django' in job_name \
                    #         or 'flask' in job_name or '运维' in job_name:
                    if job_name[-1] == '(' or job_name[-1] == '（':
                        item['job_name'] = job_name[:-1]
                    else:
                        item['job_name'] = job_name
                else:
                    continue

            job_company_xpath = './/a[@class="contentpile__content__wrapper__item__info__box__cname__title company_title"]/@title'
            item['job_company'] = job_a.xpath(job_company_xpath).extract_first()

            job_aee = job_a.xpath('.//ul[@class="contentpile__content__wrapper__item__info__box__job__demand"]')
            item['job_region'] = job_aee.xpath('./li[1]/text()').extract_first()
            item['job_exp'] = job_aee.xpath('./li[2]/text()').extract_first().strip()
            item['job_edu'] = job_aee.xpath('./li[3]/text()').extract_first()

            job_salary_xpath = './/p[@class="contentpile__content__wrapper__item__info__box__job__saray"]/text()'
            item['job_salary'] = job_a.xpath(job_salary_xpath).extract_first()

            job_company_type_xpath = job_a.xpath(
                './/div[@class="contentpile__content__wrapper__item__info__box__job__comdec"]')
            item['job_company_type'] = job_company_type_xpath.xpath('./span[1]/text()').extract_first().strip()
            item['job_company_pernum'] = job_company_type_xpath.xpath('./span[2]/text()').extract_first().strip()

            yield item

        # 请求下一页
        if self.page < 10:
            self.page += 1
            next_url = response.url + '&p=%s' % self.page

            yield Request(next_url, callback=self.parse)
