#try17-4
#2022/11/6
#author:linxu
import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")
response_dict = r.json()

print(f"Total repositories:{response_dict['total_count']}")

repo_dicts = response_dict['items']
# repo_names, stars,labels =[],[],[]
repo_links, stars,labels =[],[],[]

for repo_dict in repo_dicts:
    # repo_names.append(repo_dict['name'])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type': 'bar',
    # 'x': repo_names,
    'x': repo_links,
    'y': stars,
    'hovertext':labels,
    'marker': {
        'color': stars,
        'line': {'width': 1.5,'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Github上最受欢迎的Python项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
    'title': 'Stars',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
    },
}
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='python_repos.html')