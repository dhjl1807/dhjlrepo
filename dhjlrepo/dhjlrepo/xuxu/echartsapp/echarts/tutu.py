from pyecharts import options as opts
from pyecharts.charts import Geo, WordCloud, Bar, Funnel

from echartsapp.echarts.base import *


def dilifenbutu() -> Geo:
    dili = ZhiLian().dili_data()  # 生成地理分布图数据
    c = (
        Geo()
            .add_schema(maptype="china")
            #  .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
            .add("各城市Python岗位数量", dili)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(min_=0, max_=300),
            title_opts=opts.TitleOpts(title="Python岗位分布地理示例"),
        )
    )
    return c


def bossciyun() -> WordCloud:
    ciyun = Boss().ciyun_data()  # 生成词云图数据
    c = (
        WordCloud()
            .add("", ciyun, word_size_range=[1, 20])
            .set_global_opts(title_opts=opts.TitleOpts(title="BOSS网-城市岗位热度"))
    )
    return c


# x 工资区间 y 权值
def citysalary(city) -> Bar:
    city, data = Job().citysalary_data(city)
    c = (
        Bar()
            .add_xaxis(data[0])
            .add_yaxis("各工资区间权重", data[1])
            .set_global_opts(title_opts=opts.TitleOpts(title="工资分布区间图", subtitle=city))
    )
    return c


def edusalary(edu) -> Funnel:
    edu, d = Job().edusalary_data(edu)
    c = (
        Funnel()
            #         .add("商品", [list(z) for z in zip(Faker.choose(), Faker.values())])
            .add("不知道是啥", d)
            .set_global_opts(title_opts=opts.TitleOpts(title="主要城市薪资对比", subtitle=edu))
    )
    return c


# x 工资区间 y 权值
def yearsalary(city) -> Bar:
    city, data = Job().yearsalary(city)
    c = (
        Bar()
            .add_xaxis(data[0])
            .add_yaxis("不限", data[1]['不限'])
            .add_yaxis("应届", data[1]['应届'])
            .add_yaxis("1年以下", data[1]['1年以下'])
            .add_yaxis("1-3年", data[1]['1-3年'])
            .add_yaxis("3-5年", data[1]['3-5年'])
            .add_yaxis("5-7年", data[1]['5-7年'])
            .add_yaxis("5-10年", data[1]['5-10年'])
            .add_yaxis("10年", data[1]['10年'])
            .set_global_opts(title_opts=opts.TitleOpts(title="经验工资分布图", subtitle=city))
    )
    return c


if __name__ == '__main__':
    # dilifenbutu().render('../templates/地理分布图.html')
    # bossciyun().render('../templates/词云图.html')
    # citysalary().render('../templates/工资分布区间图.html')
    # edusalary('本科').render('../templates/薪资对比图.html')
    yearsalary('北京').render('../templates/经验工资分布图.html')
    pass
