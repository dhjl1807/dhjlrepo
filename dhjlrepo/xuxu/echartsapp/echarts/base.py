import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# import matplotlib.pyplot as plt
# %matplotlib inline
from sqlalchemy import create_engine
import pymysql

# conn = create_engine('mysql+pymysql://xuxu:xuxu@10.12.152.89/xuxu?charset=utf8')
class ZhiLian:
    def __init__(self): # 读取智联数据
        conn = create_engine('mysql+pymysql://xuxu:xuxu@10.12.152.89/xuxu?charset=utf8')
        zl = pd.read_sql('select * from zhilian_01', conn)
        self.zl = zl.set_index('id')

    def samples_zl(self): # 对智联数据进行处理
        data = self.zl[['job_region', 'job_edu', 'job_exp', 'job_company_type', 'job_company_pernum', 'job_salary']]
        data_ = data.copy()
        data_.loc[:, 'job_region'] = data['job_region'].map(lambda item: item.split('-')[0])
        data_.loc[:, 'job_exp'] = data['job_exp'].map(lambda item: item if item else np.NaN)
        data_.dropna(axis=0, how='any', inplace=True)
        return data_

    def dili_data(self): # 地理分布图数据：选取城市数据（Python工作岗位数量）
        data = self.samples_zl()
        citys = data['job_region'].unique()
        count = lambda item: data[data['job_region'] == item].shape[0]
        faker = [[city, count(city)] for city in citys]
        return faker

class Boss:
    def __init__(self):
        conn = create_engine('mysql+pymysql://xuxu:xuxu@10.12.152.89/xuxu?charset=utf8')
        boss = pd.read_sql('select * from boss', conn)
        self.boss = boss.set_index('id')

    def samples_boss(self):
        data_ = self.boss.copy()
        data_['job_addr'] = self.boss['job_addr'].map(lambda item: item.split(' ')[0])
        return data_

    def ciyun_data(self):
        data = self.samples_boss()
        faker = [(data.loc[i].job_name,
                  np.array(data.loc[i].job_salary.split('·')[0].replace('K', '').split('-')).astype(np.float).mean())
                 for i in data.index]
        return faker


if __name__ == '__main__':
    print(ZhiLian().dili_data())
    print(Boss().ciyun_data())