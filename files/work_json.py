import json
from pprint import pprint

def read_json(file_path, word_max_len=6, top_words_amt=10):
#     sorted_words = []
#     top_sorted_words = []#Список слов
#     word_dict = {}#Словарь чтобы сделать ключ-значение, чтобы по одному клучу поститать общее количество одинаковых слов
#     top_words_max_len = []  # Список слов длиннее чем word_max_len
#     with open(file_path, 'r', encoding='utf-8') as f:
#         json_data = json.load(f)
#         news_list = json_data["rss"]["channel"]["items"]
#         for news in news_list:#Список новостей
#             for word_in_news in news["description"].split():#список слов в новостях
#                 if len(word_in_news) > word_max_len:#если длина слова больше  word_max_len
#                     top_words_max_len.append(word_in_news)
#                     for top_word_max_len in top_words_max_len:#перебираем список слов длинее 6
#                         word_dict[top_word_max_len] = word_dict.get(top_word_max_len, 0) + 1#Отправляем слова в словарь чтобы отсортировать по количеству повторений
#         sorted_words = sorted(word_dict.items(), key=lambda item: item[1])[::-1]#Сортируем слова в обратном порядке
#         top_sorted_words = sorted_words[:top_words_amt]
#         top_words = [word for word, count in top_sorted_words]
#         print(top_words)

################################################################
    word_count = {}  # Словарь для подсчета слов
    top_words_max_len = []  # Список слов длиннее чем word_max_len
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        news_list = json_data["rss"]["channel"]["items"]
        for news in news_list:  # Перебираем список новостей
            for word in news["description"].split():  # Список слов в новостях
                if len(word) > word_max_len:  # Если длина слова больше word_max_len
                    top_words_max_len.append(word)
                    word_count[word] = word_count.get(word, 0) + 1  # Увеличиваем счетчик для слова

            # Сортируем слова по количеству повторений
        sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
        top_sorted_words = sorted_words[:top_words_amt]
        top_words = [word for word, count in top_sorted_words]
    return top_words
file_path = "newsafr.json"
read_json(file_path, word_max_len=6, top_words_amt=10)