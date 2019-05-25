from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo, WordCloud
from pyecharts.globals import ChartType, SymbolType

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
    ciyun = Boss().ciyun_data() # 生成词云图数据
    c = (
        WordCloud()
        .add("", ciyun, word_size_range=[1, 20])
        .set_global_opts(title_opts=opts.TitleOpts(title="BOSS网-城市岗位热度"))
    )
    return c

if __name__ == '__main__':
    # dilifenbutu().render('../templates/地理分布图.html')
    # bossciyun().render('../templates/词云图.html')
    print(bossciyun().render_notebook())