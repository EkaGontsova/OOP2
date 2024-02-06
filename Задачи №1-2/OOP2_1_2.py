import pprint


def get_cookbook():
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        cook_book = {}
        cook_book_keys = ['ingredient_name', 'quantity', 'measure']
        for line in file:
            dish_name = line.strip()
            ingredients_number = int(file.readline())
            dish_ingredients = []
            for _ in range(ingredients_number):
                ingredients = file.readline().strip().split('|')
                ingredients = dict(zip(cook_book_keys, ingredients))
                dish_ingredients.append(ingredients)
            file.readline()
            cook_book[dish_name] = dish_ingredients
    return cook_book


cook_book = get_cookbook()
pprint.pprint(cook_book, width=100, compact=True)
print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'quantity': int(ingredient['quantity']) * person_count,
                                              'measure': ingredient['measure']}
            else:
                shop_list[ingredient_name]['quantity'] += int(ingredient['quantity']) * person_count
    return shop_list


pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
