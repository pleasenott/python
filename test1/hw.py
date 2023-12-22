from pyecharts.charts import Map	#地图
from pyecharts import options as opts  #初始化配置项
map=Map(init_opts=opts.InitOpts(width='900px',height='800px'))
map.add(series_name='城市',data_pair=[('海淀区',650),('朝阳区',234),('房山区',134),('昌平区',68),('丰台区',123),('西城区',500),('大兴区',54),('东城区',21),('石景山区',9),('通州区',55),('顺义区',257)],maptype='北京')
map.set_global_opts(title_opts=opts.TitleOpts(title='北京各**需求量'),visualmap_opts=opts.VisualMapOpts(max_=680))
map.render('北京各区**需求量.html')
