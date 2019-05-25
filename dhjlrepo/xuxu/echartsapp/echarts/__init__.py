from echartsapp.echarts.tutu import dilifenbutu, bossciyun

# 生成所有图表模板的脚本
if __name__ == '__main__':
    [t().render('../templates/'+tstr+'.html') for tstr,t in [('地理分布图',dilifenbutu),
                                                             ('词云图',bossciyun)]]
