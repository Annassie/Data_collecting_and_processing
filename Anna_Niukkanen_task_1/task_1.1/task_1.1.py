from pprint import pprint
import requests


url = 'https://api.github.com/users/Annassie/repos'

#user = 'Annassie'
#repo = 'repos'

response = requests.get(url)

j_data = response.json()

for repos in j_data:
    print(f"Repos of the user {repos.get('owner').get('login')} are {repos.get('name')}")


#pprint(j_data)