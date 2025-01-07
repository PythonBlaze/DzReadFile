def is_closed(file_):
    if file_.closed:
        print('Файл закрыт')
    else:
        print('Файл открыт')



def parse_recipes(file_path):#Создание библиотеки из рецепта
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()#Возвращаем список построчно

    i = 0
    while i < len(lines):#Счетчик
        dish_name = lines[i].strip()#Добавляем в название блюда строку если счётчик равен нулю, плюсуем счётчик
        i += 1
        ingredient_count = int(lines[i].strip())#Добавляем в список ингридиентов
        i += 1

        ingredients = {}
        for _ in range(ingredient_count):#Циклом перебираем список игридиентов
            ingredient_line = lines[i].strip()#Добавляем в строку с ингридиентами строку из рецепта
            ingredient_name, quantity, unit = map(str.strip, ingredient_line.split('|'))#разделяем название ингридиентов, количество и тип по символу |
            ingredients[ingredient_name] = {
                "количество": int(quantity),
                "единица": unit
            }
            i += 1

        cook_book[dish_name] = ingredients
        i += 1  # Пропускаем пустую строку после каждого рецепта

    for dish, ingredients in cook_book.items():
        print(f'Блюдо: {dish}')
        for ingredient_name, details in ingredients.items():
            print(f'  Ингредиент: {ingredient_name}, Количество: {details["количество"]}, Единица: {details["единица"]}')
        print()  # Пустая строка между блюдами

    return cook_book

# Путь к файлу с рецептами
file_path = 'recipes.txt'
cook_book = parse_recipes(file_path)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:  # Проверяем, существует ли блюдо в cook_book
            for ingredient, details in cook_book[dish].items():
                # Рассчитываем общее количество ингредиента, учитывая количество персон
                total_quantity = details['количество'] * person_count

                # Если ингредиент уже есть в списке, увеличиваем его количество
                if ingredient in shop_list:
                    shop_list[ingredient]['quantity'] += total_quantity
                else:
                    # Добавляем новый ингредиент в словарь
                    shop_list[ingredient] = {
                        'measure': details['единица'],
                        'quantity': total_quantity
                    }

    return shop_list





dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shopping_list = get_shop_list_by_dishes(dishes, person_count)
print("{")
for ingredient, details in shopping_list.items():
    print(f"  '{ingredient}': {{'measure': '{details['measure']}', 'quantity': {details['quantity']}}},")
print("}")




