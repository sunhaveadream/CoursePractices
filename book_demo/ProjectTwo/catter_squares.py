#catter_squares
#2022/11/1
#author:linxu
import matplotlib.pyplot as plt
import numpy as np

#绘制散点图
plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(111)
#绘制一个点
# x = 2
# y = 4
#手工绘制一系列的点
# x = [1,2,3,4]
# y = [1,2,3,4]
#自动计算要包含的值
x = range(1,1001)
y = [x**2 for x in x]
#自定义颜色
# plt.scatter(x,y,s=200,color='red',marker='+')
# 颜色映射
plt.scatter(x,y,s=200,c=y,cmap=plt.cm.Blues,marker='+')
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值",fontsize=14)
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
ax.tick_params(axis='both',labelsize=14)

# plt.show()
#自动保存图表
plt.savefig('squares_plot.png',bbox_inches='tight')