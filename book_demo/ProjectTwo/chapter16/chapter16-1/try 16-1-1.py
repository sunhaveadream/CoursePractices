#try 16-1
#2022/11/5
#author:linxu
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '/ProjectTwoData/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index,column_header in enumerate(header_row):
#     print(index,column_header)

    dates,prcps = [],[]
    for row in reader:
        current_data = datetime.strptime(row[2],'%Y-%m-%d')
        prcp = float(row[3])
        dates.append(current_data)
        prcps.append(prcp)

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,prcps,c='blue')

ax.set_title('2018年每日降水量',fontsize=24)
ax.set_xlabel('日期',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('降水量',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.show()