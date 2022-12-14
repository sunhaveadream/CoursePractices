#eq_world_map
#2022/11/5
#author:linxu
import json
import plotly.express as px
import pandas as pd

# for key in px.colors.named_colorscales():
#     print(key)

# filename='D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/eq_data_1_day_m1.json'
# filename='D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/eq_data_7_day_m1.json'
filename='D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_date = json.load(f)

all_eq_date = all_eq_date['features']

mags,titles,lons,lats = [],[],[],[]
for eq_dict in all_eq_date:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()

fig = px.scatter(
    # x=lons,
    # y=lats,
    # labels={'x':'经度','y':'纬度'},
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)
fig.write_html('global_earthquakes.html')
fig.show()

