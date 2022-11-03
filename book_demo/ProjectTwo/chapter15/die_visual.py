#die_visual
#2022/11/3
#author:linxu
from chapter15.die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

die_1 = Die()
die_2 = Die(10)
results = []
# for roll_num in range(100):
for roll_num in range(50000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
# print(results)

frequencies = []
max_result = die_1.num_sides+die_2.num_sides
#掷1个六面的骰子
# for value in range(1,die.num_sides+1):
#掷2个六面的骰子
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# x_values = list(range(1,die.num_sides+1))
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}

# my_layout = Layout(title='掷1个六面的骰子100次的结果', xaxis=x_axis_config,yaxis=y_axis_config)
# offline.plot({'data':data, 'layout':my_layout},filename='d6.html')

# my_layout = Layout(title='掷2个六面的骰子100次的结果', xaxis=x_axis_config,yaxis=y_axis_config)
my_layout = Layout(title='掷1个六面的骰子和1个10面的骰子50000次的结果', xaxis=x_axis_config,yaxis=y_axis_config)
# offline.plot({'data':data,'layout':my_layout},filename='d6.html')
# offline.plot({'data':data,'layout':my_layout},filename='d6_d6.html')
offline.plot({'data':data,'layout':my_layout}, filename='d6_d10.html')