#try17-2
#2022/11/6
#author:linxu
from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids=r.json()
submission_dicts=[]

for submission_id in submission_ids[:30]:
    url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    # print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    submission_dict={
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
repo_links,conmments,labels=[],[],[]
for submission_dict in submission_dicts:
    repo_name=submission_dicts[0]
    repo_url=submission_dict['hn_link']
    repo_link=f"<a href='{repo_url}'>{repo_name}<\a>"
    label=f"By:{repo_name}<br />"
    conmments.append(submission_dict['comments'])
    repo_links.append(repo_url)
    labels.append(label)

data = [{
    'type':'bar',
    'x':repo_links,
    'y':conmments,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]

my_layout = {
    'title':'Hacker News上当前最活跃的讨论',
    'xaxis': {'title':'submission'},
    'yaxis': {'title':'Comments'},
}

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='HackerNews_Comments.html')