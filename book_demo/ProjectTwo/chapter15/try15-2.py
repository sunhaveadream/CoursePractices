#try15-2
#2022/11/1
#author:linxu
import matplotlib.pyplot as plt
plt.style.use('seaborn')

fig = plt.figure()
ax = fig.add_subplot(111)
#前5个数的立方
# input_values = [1,2,3,4,5]
# output_values=[1,6,27,64,125]
#前5000个数的立方
input_values = range(1,5001)
output_values = [x**3 for x in input_values]

ax.scatter(input_values,output_values,c=output_values,cmap=plt.cm.Blues,linewidth=3)
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值",fontsize=14)
ax.tick_params(axis='both',labelsize=14)

plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.show()