import requests
from pprint import pprint
url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
heroes = response.json()
#
# superheros = [1,2,3]
# for n in superheros:
# max_int = 0
# superhero = ''




def get_the_smartest_superhero(superheros):
    max_int = 0
    superhero = ''

    for i, hero in enumerate(heroes):
        for s in superheros:
            if s == hero['id']:
                if heroes[i]['powerstats']['intelligence'] > max_int:
                    max_int = heroes[i]['powerstats']['intelligence']
                    superhero = heroes[i]['name']
    return superhero

print(get_the_smartest_superhero([332,149,655]))


    #         for hero in heroes:
    #             if hero['name'] == "Hulk":
    #                 hulk_intelligence += hero['powerstats']['intelligence']
    #             elif hero['name'] == "Captain America":
    #                 captain_america_intelligence += hero['powerstats']['intelligence']
    #             elif hero['name'] == "Thanos":
    #                 thanos_intelligence += hero['powerstats']['intelligence']
    #
    #
    #
    #
    #
    #     if n = hero['id']
    #
    # print(i+1, hero['id'])


# a = heroes[0]['id']
#
# pprint(a)




# def get_the_smartest_superhero(superheros):
#     max_int = superheros
#     return heroes['id']



    # for hero in heroes:
    #     for id_hero in superheros:
    #         if id_hero == hero["id"]:
    #             max_int += hero["id"]['powerstats']['intelligence']
    #         # elif hero['name'] == "Captain America":
    #         #     captain_america_intelligence += hero['powerstats']['intelligence']
    #         # elif hero['name'] == "Thanos":
    #         #     thanos_intelligence += hero['powerstats']['intelligence']
    # return max_int


# print(get_the_smartest_superhero([1,2,3]))














# def get_the_smartest_superhero(superheros):
#     id_hero = superheros
#     he_smartest_superhero = ''
#     max_int = 0
#     for n in id_hero:
#         if heroes['id'] == n:
#             max_int = heroes['id']['powerstats']['intelligence']
#     return max_int
#     # he_smartest_superhero =
#
#
# get_the_smartest_superhero

# print(get_the_smartest_superhero([1,2,4]))

#
#    the_smartest_superhero = ''
#    # ваш код здесь
#    return the_smartest_superhero
#
# id_hero = heroes["id"]
# pprint(id_hero)
# # pprint(heroes["id"])


# for id_hero in heroes["id"]:
#     print(id_hero)



#
# max_int = 0
# for hero in heroes:
#     if hero['powerstats']['intelligence'] > max_int:
#         max_int = hero['powerstats']['intelligence']
#