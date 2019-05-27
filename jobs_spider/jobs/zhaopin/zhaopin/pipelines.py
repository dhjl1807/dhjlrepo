# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql.cursors import DictCursor

from zhaopin.settings import config


class ZhaopinPipeline(object):

    def __init__(self):
        self.conn = pymysql.Connect(**config)
        self.db_init()

    def db_init(self):
        with self.conn.cursor(cursor=DictCursor) as c:
            c.execute('drop table if exists zhilian_02_log')
            sql = """
                create table zhilian_02_log(id integer primary key auto_increment,
                job_name varchar (200),
                job_company varchar (100),
                job_region varchar (50),
                job_exp varchar (50),
                job_edu varchar (30),
                job_salary varchar (30),
                job_company_type varchar (20),
                job_company_pernum varchar (20)
                )
            """
            c.execute(sql)

    def process_item(self, item, spider):
        with self.conn.cursor(cursor=DictCursor) as c:
            sql = """
                insert into zhilian_02_log(job_name, job_company, job_region, job_exp, job_edu, job_salary, job_company_type, job_company_pernum)
                values (%(job_name)s, %(job_company)s, %(job_region)s, %(job_exp)s, %(job_edu)s, %(job_salary)s, %(job_company_type)s, %(job_company_pernum)s)
            """
            c.execute(sql, args=item)
        self.conn.commit()
        return item
