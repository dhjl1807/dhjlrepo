from echartsapp.echarts.tutu import dilifenbutu, bossciyun, citysalary, edusalary, yearsalary

# 生成所有图表模板的脚本
if __name__ == '__main__':
    [t().render('../templates/'+tstr+'.html') for tstr,t in [('地理分布图',dilifenbutu),
                                                             ('词云图',bossciyun),
                                                             ('工资分布区间图',citysalary),
                                                             ('薪资对比图',edusalary),
                                                             ('经验工资分布图',yearsalary)]]
