#mpl_squares
#2022/10/31
#author:linxu

#绘制简单的折线图
import matplotlib.pyplot as plt
plt.style.use('seaborn')

fig = plt.figure()
ax = fig.add_subplot(111)

input_values = [1,2,3,4,5]
output_values=[1,4,9,16,25]

ax.set(xlim=[0, 4], ylim=[0, 25], title='平方数',
       ylabel='值的平方', xlabel='值')

ax.plot(output_values,color='lightblue',linewidth=3)
ax.tick_params(axis='both',labelsize=14)

plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.show()

