# -*- coding: utf-8 -*-
import time

import pymysql
import requests
from urllib import parse

from pymysql.cursors import DictCursor

from lgw01.header import get_headers

config = {
    'user': 'root',
    'password': 'dong',
    'port': 3306,
    'host': 'localhost',
    'db': 'mydb',
    'charset': 'utf8'
}
conn = pymysql.connect(**config)
batch_count = 0
page = 0


def get(url, params, headers):
    global page
    page += 1
    print('请求URL:', url)
    print('请求第' + str(page) + '页')
    response = requests.post(url, data=params, headers=headers)
    data = response.json()
    parse_data(data)


def parse_data(data):
    item = {}
    try:
        results = data['content']['positionResult']['result']
        for result in results:
            item['job_name'] = result['positionName']
            item['job_region'] = result['district']
            item['job_format_time'] = result['createTime']
            item['job_company'] = result['companyShortName']
            item['job_company_type'] = result['industryField']
            item['job_company_financ'] = result['financeStage']
            item['job_company_pernum'] = result['companySize']
            item['job_salary'] = result['salary']
            item['job_exp'] = result['workYear']
            item['job_edu'] = result['education']
            save(item)
        time.sleep(0.2)
    except KeyError as e:
        print(e)


def save(item):
    with conn.cursor(cursor=DictCursor) as c:
        sql = """
            insert into lgw(job_name, job_region, job_format_time, job_company, job_company_type, job_company_financ, job_company_pernum, job_salary, job_exp, job_edu)
            values (%(job_name)s, %(job_region)s, %(job_format_time)s, %(job_company)s, %(job_company_type)s, %(job_company_financ)s, %(job_company_pernum)s, %(job_salary)s, %(job_exp)s, %(job_edu)s)
        """
        c.execute(sql, args=item)

    conn.commit()


if __name__ == '__main__':

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '25',
        'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC',
        'User-Agent': get_headers(),
        'Host': 'www.lagou.com',
        'Origin': 'https: // www.lagou.com',
        'Cookie': 'JSESSIONID=ABAAABAAAGGABCB4B5AE7CCF18AC112EA05FB87366CC9CD; user_trace_token=20190522083703-1892ab9b-44fa-45e2-9b70-3dee70eb8f61; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558485427; _ga=GA1.2.1957178602.1558485427; _gid=GA1.2.824223490.1558485427; LGUID=20190522083705-b8fbd1ab-7c29-11e9-a111-5254005c3644; TG-TRACK-CODE=search_code; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ade87ddba5f8-0c349575f02b92-e353165-1049088-16ade87ddbb4e4%22%2C%22%24device_id%22%3A%2216ade87ddba5f8-0c349575f02b92-e353165-1049088-16ade87ddbb4e4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LGSID=20190522190300-29fa5724-7c81-11e9-a116-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FPython%2F3%2F%3FfilterOption%3D3; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3Fpx%3Ddefault%26city%3D%25E5%258C%2597%25E4%25BA%25AC; SEARCH_ID=d93bbab9b11c4f1a84f26273eb13558e; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558523032; LGRID=20190522190349-47097cb9-7c81-11e9-a6b4-525400f775ce; X_HTTP_TOKEN=aa76d906f8ab66d41303258551a050d0ec6812d843'
    }

    for city in ['北京', '上海', '深圳', '广州', '天津', '成都', '杭州', '武汉', '大连', '长春',
                 '南京', '济南', '青岛', '苏州', '沈阳', '西安', '郑州', '长沙', '重庆', '哈尔滨',
                 '无锡', '宁波', '福州', '厦门', '石家庄', '合肥', '惠州', '太原', '昆明', '乌鲁木齐']:
        start_url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=' + parse.quote(
            city) + '&needAddtionalResult=false'
        print('提取' + city + '城市招聘信息')
        for i in range(1, 31):
            params = {
                'first': False,
                'pn': i,
                'kd': 'Python'
            }
            get(start_url, params, headers)
