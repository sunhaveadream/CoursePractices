#eq_explore_data
#2022/11/5
#author:linxu
import json


filename='D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_date = json.load(f)

# readable_file = 'D:/PycharmProjects1/CoursePractice/book_demo/ProjectTwo/ProjectTwoData/readable_eq_data.json'
# with open(readable_file,'w') as f:
#     json.dump(all_eq_date,f,indent=4)

all_eq_date = all_eq_date['features']
# print(len(all_eq_date))

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
# print(mags[:10])
# print(titles[:2])
# print(lons[:5])
# print(lats[:5])
