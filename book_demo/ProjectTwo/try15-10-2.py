#try15-10-2
#2022/11/3
#author:linxu
from plotly import offline
from plotly.graph_objs import Scatter,Layout
import plotly.graph_objs as go

from random_walk import RandomWalk
class RandomWalk:
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers=range(rw.num_points)
    point_numbers = range(rw.num_points)
    trace = go.Scatter(x=rw.x_values, y=rw.y_values, mode='markers')
    data = [trace]
    x_axis_config = {'title': 'x轴坐标'}
    y_axis_config = {'title': 'y轴坐标'}
    my_layout = Layout(title='使用Plotly通过可视化来模拟随机漫步的情况',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout},
                 filename='random_walk.html')
