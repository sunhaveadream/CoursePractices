#try16-4
#2022/11/5
#author:linxu、
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '/ProjectTwoData/sitka_weather_2018_simple.csv'
filename = '/ProjectTwoData/death_valley_2018_simple.csv'
place_name=''
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')
    dates, highs, lows = [], [], []
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
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='green',alpha=1)
ax.set_title('2018年每日最高温度和最低温度',fontsize=24)
ax.set_xlabel('日期',fontsize=16)
ax.set_ylabel('温度',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
fig.autofmt_xdate()
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.show()