import os

cook_book_bp = os.getcwd()
cook_book_name = input('Введите название кулинарной книги: ')
cook_book_path = os.path.join(cook_book_bp, cook_book_name)
cook_book = {}


def cook_book_file(file_path:str, mode:str):
    with open(file_path, mode, encoding='utf-8') as file:
        while True:
            recipe_name = file.readline().strip()
            cook_book.setdefault(recipe_name, [])
            ingredient_count = file.readline().strip()
            for i in range(int(ingredient_count)):
                ingredient_name, quantity, measure = [val for val in file.readline().strip().split(' | ')]
                cook_book[recipe_name].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            if file.readline() == '':
                break


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            if ingredients['ingredient_name'] not in ingredients_dict:
                ingredients_dict[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                    'quantity': int(ingredients['quantity']) * person_count}
            else:
                ingredients_dict[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
    return ingredients_dict


cook_book_file(cook_book_path, 'r')
dishes = list(input('Введите через запятую блюда для рассчёта ингредиентов: ').split(', '))
person_count = int(input('Введите кол-во персон: '))
print(get_shop_list_by_dishes(dishes, person_count))
