#try15-10
#2022/11/3
#author:linxu
import matplotlib.pyplot as plt
from chapter15.die import Die

fig = plt.figure()
ax = fig.add_subplot(111)

die =Die()
results=[die.roll() for roll_num in range(1000)]
frequencies = [results.count(value) for value in range(1,die.num_sides+1)]
values = [value for value in range(1,die.num_sides+1) ]
ax.plot(values,frequencies,linewidth=2,color='blue')
ax.set_title('使用Matplotlib掷骰子',fontsize=24)
ax.set_xlabel=('结果')
ax.set_ylabel=('结果的频率')
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.show()