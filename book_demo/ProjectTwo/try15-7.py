#try15-7
#2022/11/3
#author:linxu
from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()+die_3.roll()
    results.append(result)

frequencies = []
max_results = die_1.num_sides+die_2.num_sides+die_3.num_sides
for value in range(2,max_results+1):
    frequence = results.count(value)
    frequencies.append(frequence)

x_values = list(range(2,max_results+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}

my_layout = Layout(title='掷3个八面的骰子1000次的结果', xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d8_d8_d8.html')