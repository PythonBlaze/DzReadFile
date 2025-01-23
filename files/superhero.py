import requests
from pprint import pprint
url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
heroes = response.json()
# pprint(heroes)
hulk_intelligence = 0
captain_america_intelligence = 0
thanos_intelligence = 0


for hero in heroes:
    if hero['name'] == "Hulk":
        hulk_intelligence += hero['powerstats']['intelligence']
    elif hero['name'] == "Captain America":
        captain_america_intelligence += hero['powerstats']['intelligence']
    elif hero['name'] == "Thanos":
        thanos_intelligence += hero['powerstats']['intelligence']

max_value = max(hulk_intelligence, captain_america_intelligence, thanos_intelligence)

if max_value == hulk_intelligence:
    the_smartest_superhero = 'Hulk'
elif max_value == captain_america_intelligence:
    the_smartest_superhero = "Captain America"
elif max_value == thanos_intelligence:
    the_smartest_superhero = "Thanos"




pprint(f" Самый умный супергерой {the_smartest_superhero}")



# with open("answer.json", 'w') as f:
#     f.write(response.text)


# def get_the_smartest_superhero() -> str:
#     the_smartest_superhero = ''
#     # ваш код здесь
#     return the_smartest_superhero












