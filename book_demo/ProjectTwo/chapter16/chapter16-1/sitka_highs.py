#sitka_highs
#2022/11/4
#author:linxu
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = 'D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/sitka_weather_07-2018_simple.csv'
filename = '/ProjectTwoData/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # print(header_row)

    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    dates,highs = [],[]
    for row in reader:
        current_data = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_data)
        highs.append(high)

# print(highs)
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
# ax.set_title('2018.07每日最高温度',fontsize=24)
ax.set_title('2018年每日最高温度',fontsize=24)
ax.set_xlabel('日期',fontsize=16)
ax.set_ylabel('温度',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
fig.autofmt_xdate()
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.show()
