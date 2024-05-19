from pprint import pprint


#Task_1
def read_cook_book(file):
    with open(file, encoding='utf-8') as file:
        cook_book = {}
        for text in file.read().split('\n\n'):
            name, count, *args = text.split('\n')
            ingredients = []
            for arg in args:
                ingredient_name, quantity, measure = arg.split(' | ')
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            cook_book[name] = ingredients
        return cook_book


print(read_cook_book('recipes.txt'))

#Task_2


def get_shop_list_by_dishes(dishes, person_count):
    cookbook = read_cook_book('recipes.txt')
    cook_dict = {}
    for dish, ingredients in cookbook.items():
        if dish in dishes:
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name not in cook_dict:
                    cook_dict[ingredient_name] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    cook_dict[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
    return cook_dict

pprint(get_shop_list_by_dishes(['Запеченный картофель','Утка по-пекински'], 1))


#Task_3


files_list = ['1.txt', '2.txt', '3.txt']
content_list = []
for file in files_list:
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
        content_list.append((file, len(lines), lines))

content_list.sort(key=lambda x: x[1])

with open('result_file.txt', 'a', encoding='utf-8') as result_file:
    for file_name, line_count, lines in content_list:
        result_file.write(file_name + '\n')
        result_file.write(str(line_count) + '\n')
        result_file.writelines(lines)
        result_file.write('\n')
with open('result_file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)