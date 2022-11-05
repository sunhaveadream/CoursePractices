#try16-2
#2022/11/5
#author:linxu

import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather_data(filename,dates,highs,lows,date_index,high_index,low_index):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            current_data = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f'Missinf data for {current_data}')
            else:
                dates.append(current_data)
                highs.append(high)
                lows.append(low)

filename = 'D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/sitka_weather_2018_simple.csv'
dates,highs,lows = [],[],[]
get_weather_data(filename,dates,highs,lows,date_index=2,high_index=5,low_index=6)

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.15)

filename = 'D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/death_valley_2018_simple.csv'
dates,highs,lows = [],[],[]
get_weather_data(filename,dates,highs,lows,date_index=2,high_index=4,low_index=5)

ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.15)

plt.title('2018年锡特卡和死亡谷每日最高温度和最低温度比较',fontsize=24)
plt.xlabel('日期',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('温度',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.ylim(10,130)
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.show()