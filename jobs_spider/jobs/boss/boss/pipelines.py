# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymysql.cursors import DictCursor

from boss.settings import DB_CONFIG


class BossPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(**DB_CONFIG)
        self.init_db()
        self.batch_count = 0

    def init_db(self):
        with self.conn.cursor(cursor=DictCursor) as c:
            c.execute('drop table if exists boss_01')
            sql = """
                create table boss_01(
                id integer primary key auto_increment,
                  job_name varchar (200),
                  job_region varchar (100),
                  job_company varchar (100),
                  job_company_type varchar (50),
                  job_company_financ varchar (30),
                  job_company_pernum varchar (30),
                  job_salary varchar (30),
                  job_exp varchar (30),
                  job_edu varchar (20)
                )
            """
            c.execute(sql)

    def process_item(self, item, spider):
        with self.conn.cursor(cursor=DictCursor)as c:
            sql = 'insert boss_01(job_name, job_region, job_company, job_company_type, job_company_financ, job_company_pernum, job_salary, job_exp, job_edu)' \
                  'values(%(job_name)s, %(job_region)s, %(job_company)s, %(job_company_type)s, %(job_company_financ)s, %(job_company_pernum)s, %(job_salary)s, %(job_exp)s, %(job_edu)s) '
            c.execute(sql, args=item)
            self.conn.commit()

        return item

# class BossPipeline(object):
#     def __init__(self):
#         self.csv_filename = 'shenzhen.csv'
#         self.existed_header = False
#
#     def process_item(self, item, spider):
#         with open(self.csv_filename,'a',encoding='utf8')as f:
#             writer = csv.DictWriter(f,fieldnames=item.keys())
#             if not self.existed_header:
#                 writer.writeheader()
#                 self.existed_header = True
#
#             writer.writerow(item)
#         return item
