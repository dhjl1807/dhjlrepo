# -*- coding: utf-8 -*-
from os import path
import matplotlib.pyplot as plt
import pymysql
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import jieba


class sqlHelper(object):
    def __init__(self, host, user, password, database):
        # 打开数据库连接
        self.db = pymysql.connect(host, user, password, database, use_unicode=True, charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    # 析构函数关闭连接
    def __del__(self):
        self.cursor.close()
        # 关闭数据库连接
        self.db.close()

    def getAll(self, table_name):
        sql = "SELECT * FROM %s" % table_name
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")


def create_wordcloud(table_name):
    sql = sqlHelper("10.12.152.89", "xuxu", "xuxu", "xuxu")
    datas: tuple = sql.getAll(table_name)
    print('开始加载文本')
    text = ''
    for data in datas:

        # 9对应拉招聘公司的职位要求描述
        if not data[8]:
            continue
        else:
            text += data[8]

    text = text.replace("'", "")

    items = [i for i in jieba.cut(text)]  # jieba.cut(text) 将text的元素一个个切出返回列表

    text = " ".join(jieba.cut(text))

    d = path.dirname(__file__)
    font = path.join(path.dirname(__file__), "xingshu.ttf")

    background = np.array(Image.open(path.join(d, "Python-logo.png")))  # background 是一个三维数组
    print('加载图片成功！')
    wordcloud: WordCloud = WordCloud(background_color="white", max_words=200, font_path=font, width=300, height=150,
                                     mask=background, max_font_size=500,
                                     margin=2).generate(text)
    plt.imshow(wordcloud.recolor(), interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.imshow(background, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    print('生成词云成功!')


if __name__ == '__main__':
    create_wordcloud('job_info')
