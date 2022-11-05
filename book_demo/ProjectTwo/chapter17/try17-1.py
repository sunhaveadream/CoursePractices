#try17-1
#2022/11/6
#author:linxu
import requests

url = 'https://api.github.com/search/repositories?q=language:JavaScript&sort=stars'
# url = 'https://api.github.com/search/repositories?q=language:Ruby&sort=stars'
# url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'
# url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
# url = 'https://api.github.com/search/repositories?q=language:perl&sort=stars'
# url = 'https://api.github.com/search/repositories?q=language:Haskell&sort=stars'
# url = 'https://api.github.com/search/repositories?q=language:Go&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")
response_dict = r.json()

print(f"Total repositories:{response_dict['total_count']}")

repo_dicts = response_dict['items']
repo_names, stars =[],[]

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
