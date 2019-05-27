# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql.cursors import DictCursor
from qiancheng_2.settings import DB_CONFIG


class Qiancheng2Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)
        self.init_db()

    def init_db(self):
        with self.conn.cursor(cursor=DictCursor) as c:
            c.execute('drop table if exists qiancheng2')
            sql = """
            create table qiancheng2(
            id integer primary key auto_increment,
            job_name varchar(100),
            job_company varchar(100),
            job_addr varchar(50),
            job_experience varchar(50),
            job_edu varchar(30),
            job_salary varchar(30)
            )
            """
            c.execute(sql)

    def process_item(self, item, spider):
        with self.conn.cursor(cursor=DictCursor)as c:
            sql = 'insert into qiancheng2(job_name,job_company,job_addr,job_experience,job_edu,job_salary)' \
                  'values(%(job_name)s,%(job_company)s,%(job_addr)s,%(job_experience)s,%(job_edu)s,%(job_salary)s)'

            c.execute(sql, args=item)
            self.conn.commit()

        return item
