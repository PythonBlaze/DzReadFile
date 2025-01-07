import os
#Пишем функцию которая будет открывать файлы, присваивать их значения переменным, сортировать по количеству строк в них и обьединять их в один. Перед содержимым файла должна быть информация о имени файла и количестве строк в нём.

file_names = ['1.txt', '2.txt', '3.txt']# Список файлов, которые нужно объединить
output_file = 'output.txt'  # Имя итогового файла

file_info = []# Список для хранения информации о файлах

for file_name in file_names:# Проходим циклом по именам файлов  и открываем их
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()#Содержимое файла построчно
        line_count = len(lines)#Количество строк
        file_info.append((file_name, line_count, lines))#Добавляем в список имя файла, количество строк, и содержимое

# Сортировка по количеству строк
file_info.sort(key=lambda x: x[1])# Методом sort изменяем file_info. кей сортирует по лямбда х, где х второй элемент нашего кортежа (количество строк)

# Запись в итоговый файл
with open(output_file, 'w', encoding='utf-8') as out_file:
    for file_name, line_count, lines in file_info:
        out_file.write(f"{file_name}\n")
        out_file.write(f"{line_count}\n")
        out_file.writelines(lines)
        out_file.write("\n")

print(f"Файлы успешно объединены в '{output_file}'")
