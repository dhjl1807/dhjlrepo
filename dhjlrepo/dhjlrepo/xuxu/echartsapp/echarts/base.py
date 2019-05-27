import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sqlalchemy import create_engine
import pymysql


# conn = create_engine('mysql+pymysql://xuxu:xuxu@10.12.152.89/xuxu?charset=utf8')
class ZhiLian:
    def __init__(self):  # 读取智联数据
        conn = create_engine('mysql+pymysql://xuxu:xuxu@10.12.152.89/xuxu?charset=utf8')
        zl = pd.read_sql('select * from zhilian_01', conn)
        self.zl = zl.set_index('id')

    def samples_zl(self):  # 对智联数据进行处理
        data = self.zl[['job_region', 'job_edu', 'job_exp', 'job_company_type', 'job_company_pernum', 'job_salary']]
        data_ = data.copy()
        data_.loc[:, 'job_region'] = data['job_region'].map(lambda item: item.split('-')[0])
        data_.loc[:, 'job_exp'] = data['job_exp'].map(lambda item: item if item else np.NaN)
        data_.dropna(axis=0, how='any', inplace=True)
        return data_

    def dili_data(self):  # 地理分布图数据：选取城市数据（Python工作岗位数量）
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


class Job:
    def __init__(self):
        conn = create_engine('mysql+pymysql://xuxu:xuxu@10.12.152.89/xuxu?charset=utf8')
        boss = pd.read_sql('select * from job_info', conn)
        self.boss = boss.set_index('id')

    def sss(self):
        data = self.boss
        print(data['city'].unique())

    def qingxi(self):  # 清洗 city education years # 去重复
        data_ = self.boss.copy()[
            ['company', 'company_detail', 'scale', 'stage', 'positions', 'skill', 'city', 'education', 'years',
             'salary']]
        # p_education
        data_.loc[:, 'education'] = self.boss['education'].map(
            lambda item: item.replace('及以上', '').replace('暂无信息', '').replace('学历', '')).map(
            lambda item: np.nan if item == '' else item)
        # years
        exp_map = {'无': '不限', '无工作': '不限', '不限': '不限', '1年以内': '1年以下', '1年以下': '1年以下', '1年': '1-3年',
                   '2年': '1-3年', '1-3年': '1-3年', '3-4年': '3-5年', '3-5年': '3-5年', '5-7年': '5-7年', '5-10年': '5-10年',
                   '10年以上': '10年', '应届毕业生': '应届', '应届生': '应届'}
        data_.loc[:, 'years'] = self.boss['years'].map(lambda item: item.replace('经验', '')).map(exp_map)
        return data_

    def rule_salary(self):  # 规范化 salary # 统一值格式
        data = self.qingxi()

        def clear(item):  # 清洗 salary 数据
            item = item.replace('千', 'K').replace('k', 'K').split('·')[0]
            if '万' in item:  # 0.6-1.5万   1万-1.5万   8K-1.2万   1万及以上
                w = []
                s = None
                for i in item.split('-'):
                    if 'K' not in i:
                        if '万' in i:
                            k = float(i.split('万')[0]) * 10
                            s = i.split('万')[-1]
                        else:
                            k = float(i) * 10
                        w.append(str(k))
                    else:
                        w.append(str(float(i.split('K')[0])))
                item = '-'.join(w) + 'K'
                if s:
                    item += s
            elif 'K' in item:  # 8-10K   10K-20K   1K以下
                w = []
                s = None
                for j in item.split('-'):
                    s = j.split('K')[-1]
                    k = float(j.split('K')[0])
                    w.append(str(k))
                item = '-'.join(w) + 'K'
                if s:
                    item += s
            else:  # 200元   面议
                item = np.nan
            return item

        data_ = data.copy()
        data_.loc[:, 'salary'] = data['salary'].map(clear)
        return data_

    def get_salary_avg(self):  # 计算 salary 的平均值
        data = self.rule_salary()

        def getavg(item):  # 得到 salary 平均值 # 默认已经处理过 NaN
            if item.split('K')[-1] != '':
                return float(item.split('K')[0])
            s = [float(i) for i in item.split('K')[0].split('-')]
            return sum(s) / len(s)

        data_ = data.copy()
        data_.dropna(how='any', inplace=True)
        data_1 = data_.copy()
        data_.loc[:, 'salary'] = data_1['salary'].map(getavg)
        return data_

    def salary_trans(self):  # 将 salary 转化成自定义的额区间值
        data = self.get_salary_avg()
        salary_map = {
            (0, 3): '3K以下',
            (3, 5): '3-5K',
            (5, 10): '5-10K',
            (10, 15): '10-15K',
            (15, 20): '15-20K',
            (20, 25): '20-25K',
            (25, 50): '25-50K',
            (50, 100): '50-100K',
            (100, 1000): '100K以上'
        }

        def transsalary(item):
            for k, v in salary_map.items():
                if k[0] <= item < k[-1]:
                    return v

        data_ = data.copy()
        data_['salary'] = data['salary'].map(transsalary)
        return data_

    def get_data(self):  # 提取 city education years salary
        data = self.qingxi()
        data_ = data.iloc[:, -4:]
        return data_

    def shuzhihua(self):  # 将 city education years 数值化
        data = self.get_data()
        self.city_map = {k: v + 1 for v, k in enumerate(data['city'].unique())}
        self.edu_map = {k: v + 1 for v, k in enumerate(data['education'].unique())}
        self.year_map = {k: v + 1 for v, k in enumerate(data['years'].unique())}
        data_ = data.copy()
        data_.loc[:, 'city'] = data['city'].map(self.city_map)
        data_.loc[:, 'education'] = data['education'].map(self.edu_map)
        data_.loc[:, 'years'] = data['years'].map(self.year_map)
        return data_

    def citysalary_data(self, city='西安'):  # 工资分布区间图数据
        data = self.salary_trans()
        data_ = (lambda city: data if city == '全国' else data[data['city'] == city])(city)
        keys = ['3K以下', '3-5K', '5-10K', '10-15K', '15-20K', '20-25K', '25-50K', '50-100K', '100K以上']
        values = [(i, int(data_['salary'].value_counts()[i])) for i in keys if
                  i in data_['salary'].unique()]  # 只能是python的基本int型
        d = [[i[0] for i in values], [i[1] for i in values]]
        return city, d

    def edusalary_data(self, edu='本科'):  # 薪资对比图数据
        data = self.get_salary_avg()
        # '本科', '学历不限', '硕士', '大专', '高中', '博士', '中专', '中技'
        cities = ['北京', '上海', '广州', '深圳', '杭州', '武汉', '城都', '西安', '郑州', '重庆']
        data_ = (lambda item, edu: data[(data['city'] == item) & (data['education'] == edu)])
        values = [(i, data_(i, edu)['salary'].mean()) for i in cities if i in data['city'].unique()]  # 只能是python的基本int型
        d = [i for i in values if i[1] is not np.nan]
        return edu, d

    def yearsalary(self, city='西安'):  # 经验工资分布图
        data = self.salary_trans()
        data_ = (lambda city: data if city == '全国' else data[data['city'] == city])(city)
        keys = ['3K以下', '3-5K', '5-10K', '10-15K', '15-20K', '20-25K', '25-50K', '50-100K', '100K以上']
        v = {}
        for year in ['不限', '应届', '1年以下', '1-3年', '3-5年', '5-7年', '5-10年', '10年']:
            data_1 = (lambda city: data_[data_['years'] == city])(year)
            values = [(i, int(data_1['salary'].value_counts()[i]) if i in data_1['salary'].unique() else 0) for i in
                      keys]  # 只能是python的基本int型
            v[year] = [i[-1] for i in values]
        d = [keys, v]
        return city, d


if __name__ == '__main__':
    # print(ZhiLian().dili_data())
    # print(Boss().ciyun_data())
    # print(Job().salary_trans().head())
    # print(Job().get_data().head())
    # print(Job().citysalary_data('北京'))
    # print(Job().edusalary_data('硕士'))
    # print(Job().yearsalary('北京'))
    Job().sss()
