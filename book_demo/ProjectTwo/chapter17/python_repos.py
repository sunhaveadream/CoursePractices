#python_repos
#2022/11/5
#author:linxu

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")
response_dict = r.json()

# print(response_dict.keys())
print(f"Total repositories:{response_dict['total_count']}")

repo_dicts = response_dict['items']
repo_names, stars =[],[]
# print(f"Repositories returned: {len(repo_dicts)}")
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
# print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

