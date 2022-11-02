#try15-9
#2022/11/3
#author:linxu
from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll()+die_2.roll() for roll_num in range(1000)]

max_results = die_1.num_sides+die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_results+1)]

x_values = list(range(2,max_results+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}

my_layout = Layout(title='掷2个八面的骰子1000次的结果', xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d8_d8.html')