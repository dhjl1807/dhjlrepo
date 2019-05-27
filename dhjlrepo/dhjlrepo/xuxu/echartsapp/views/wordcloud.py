# -*- coding: utf-8 -*-
from os import path
import matplotlib.pyplot as plt
import pymysql
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import jieba


class sqlHelper(object):
    def __init__(self, host, user, password, database):
        # 打开数据库连接
        self.db = pymysql.connect(host, user, password, database, charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    # 析构函数关闭连接
    def __del__(self):
        self.cursor.close()
        # 关闭数据库连接
        self.db.close()

    def getAll(self, table_name):
        sql = "SELECT * FROM %s" % table_name
        print('sql=', sql)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except:
            print("出现异常")


def create_wordcloud(request, table_name='job_info'):
    img_table = table_name
    flag = False
    if table_name == '前程无忧':
        table_name = 'qiancheng2'
    elif table_name == 'Boss直聘':
        table_name = 'boss_01'
    elif table_name == '智联招聘':
        table_name = 'zhilian_01'
    else:
        flag = True
        table_name = 'job_info'

    exist_img = path.dirname(path.dirname(path.dirname(__file__)))
    # pj = path.join(exist_img, 'static\images\{}.png'.format(img_table))
    # print(pj)
    esixted_img = path.exists(path.join(exist_img, 'static\images\{}.png'.format(img_table)))
    # print(esixted_img)
    if esixted_img:
        print('词云图是否存在？', esixted_img)
        pass
    else:
        print('词云图是否存在？', esixted_img)
        sql = sqlHelper("10.12.152.89", "xuxu", "xuxu", "xuxu")
        datas: tuple = sql.getAll(table_name)
        print('开始加载文本')
        text = ''
        if flag:
            for data in datas:
                # 前程无忧  1 --> 工作岗位
                # Boss直聘  1 --> 工作岗位
                # 智联招聘  1 --> 工作岗位
                # 8对应拉招聘公司的职位要求描述
                if not data[8]:
                    continue
                else:
                    text += data[8]
        else:
            for data in datas:
                if not data[1]:
                    continue
                else:
                    text += data[1]

        text = text.replace("'", "")

        text = " ".join(jieba.cut(text))

        d = path.dirname(__file__)
        font = path.join(path.dirname(__file__), "xingshu.ttf")

        background = np.array(Image.open(path.join(d, "Python-logo.png")))  # background 是一个三维数组
        wc = WordCloud(background_color="white", max_words=200, font_path=font, width=300, height=150,
                       mask=background, max_font_size=300, min_font_size=20,
                       margin=2).generate(text)
        img_path = '../xuxu/static/images/{}.png'.format(img_table)
        wc.to_file(img_path)
        print('词云生成成功！')

    image = '/static/images/{}.png'.format(img_table)
    url = image
    title = img_table
    if title == '综合展示':
        title = ''
    else:
        pass

    alt = img_table + '词云图'
    return JsonResponse({
        'url': url,
        'title': title,
        'alt': alt
    })

# if __name__ == '__main__':
#     create_wordcloud('job_info')
