import json
import requests
from pprint import pprint


file_path = r"C:\Users\Blaze\Desktop\Netology\DzReadFile\private\key_yandex.json"
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        key = json.load(f)
        pprint(key)
except FileNotFoundError:
    print("Файл не найден. Проверьте путь к файлу.")
except json.JSONDecodeError:
    print("Ошибка декодирования JSON. Проверьте содержимое файла.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

# def translate_word(word):
#     with open ("C:\Users\Blaze\Desktop\Netology\DzReadFile\private\keys.md) as f:
#         key = json.load(f)
#         print(json_data)
#     url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"
#     params = {
#     'key': 'dict.1.1.20250122T175007Z.d00e3f517a7fb16b.c8f6d1ab66c953cdbacfddfdd4caab4276f11c68',
#     'lang': 'ru-en',
#     'text': word,
#     }
#     response = requests.get(url, params=params)
#     trans_word = ''
#
# # pprint(response.text)
# # pprint(response.json())
#     word_trans = response.json()['def']
# # word2 = word1['def']
#
#     for lvl1 in word_trans:
#         for lvl2 in lvl1['tr']:
#             trans_word += lvl2['text']
#             break
#     return trans_word
# word = input('ВВедите слово: ')
# print(translate_word(word))



# word = input('Введите слово :')
# #
# with open("translate.json", 'w', encoding=utf-8) as f:
#     f.write(response.text)

# translated_world = response.json()["def"]

# with open("translate.json", 'w') as f:
#     f.write(response.text)





