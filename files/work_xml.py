import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    parser = ET.XMLParser(encoding="utf-8")#просто декодировщик
    tree = ET.parse(file_path, parser)#открываем файл
    root = tree.getroot()#ДЖобираемся до корня через команду гетрут
    news_list = root.findall("channel/item")#с помощью команды файндалл ищем всё что есть у корня по данному адресу
    word_count = {}  # Словарь для подсчета слов
    top_words_max_len = []  # Список слов длиннее чем word_max_len
    for news in news_list:#Циклом перебираем все новости
        for word in news.find("description").text.split():  # Список слов в новостях #командой текст преобразуем  новость с тегом дескрипшен в читаемые буквы, команда файнд ищет данные с тегом дескрипшен
            if len(word) > word_max_len:  # Если длина слова больше word_max_len

                top_words_max_len.append(word)
                word_count[word] = word_count.get(word, 0) + 1  # Увеличиваем счетчик для слова

            # Сортируем слова по количеству повторений
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    top_sorted_words = sorted_words[:top_words_amt]
    top_words = [word for word, count in top_sorted_words]
    return top_words

print(read_xml("newsafr.xml"))