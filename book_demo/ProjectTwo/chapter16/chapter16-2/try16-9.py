#try16-9
#2022/11/5
#author:linxu
import csv
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from datetime import datetime

filename = 'D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    datas,longitudes,latitudes,brightnesses = [],[],[],[]
    for row in reader:
            current_data = datetime.strptime(row[5], '%Y-%m-%d')
            longitude = float(row[1])
            latitude = float(row[0])
            brightness = float(row[2])

            datas.append(current_data)
            longitudes.append(longitude)
            latitudes.append(latitude)
            brightnesses.append(brightness)
data = pd.DataFrame(
    data=zip(longitudes,latitudes,brightnesses,datas),columns=['经度','纬度','火灾强度','时间']
)
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球火灾图',
    size='火灾强度',
    size_max=10,
    color='火灾强度',
    hover_name='时间',
)
fig.write_html('global_fires.html')
fig.show()
