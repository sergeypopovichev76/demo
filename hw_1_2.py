from pprint import pprint

# -*- coding: utf-8 -*-
file = 'recipes.txt'


def cook_book_made(file):
    """
    Задача № 1
    """
    cook_book = dict()
    cook_recipe = {}
    cook_ingridients = {}

    with open(file, encoding='utf-8') as recipes:
        for line in recipes:
            cook_recipe[line.strip()] = []
            for i in range(int(recipes.readline().strip())):
                cook_ingridients['ingredient_name'], cook_ingridients['quantity'], cook_ingridients['measure'] = \
                    recipes.readline().strip().split('|')
                cook_ingridients['quantity'] = int(cook_ingridients['quantity'])
                for k in cook_recipe.keys():
                    cook_recipe[k].append(cook_ingridients)
                cook_ingridients = dict()
            cook_book = cook_book | cook_recipe
            cook_recipe = dict()
            recipes.readline()
    return cook_book


cook_book = cook_book_made(file)


def get_shop_list_by_dishes(dishes: list, person_count: int):
    """
        Задача № 2
    """
    product_basket = {}
    for dish in dishes:
        if dish in cook_book:
            for item in range(len(cook_book[dish])):
                if cook_book[dish][item]['ingredient_name'] not in product_basket:
                    product_basket.setdefault(cook_book[dish][item]['ingredient_name'],
                                              {'measure': cook_book[dish][item]['measure'],
                                               'quantity': cook_book[dish][item]['quantity'] * person_count})
                else:
                    product_basket[cook_book[dish][item]['ingredient_name']]['quantity'] += \
                        cook_book[dish][item]['quantity'] * person_count

    return product_basket


pprint(cook_book, width=100)
print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
