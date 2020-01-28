"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [14, True, 56.34, "str", [1, 3, 4], (5, 4, 3), {"key1": 1, "key2": 2}]

for item in my_list:
    print(type(item))

"""
2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = input("Enter list elements, use ',' for separator: ").split(',')

i = 0
list_len = len(my_list)
isOdd = bool(list_len % 2)

for value in my_list:
    if (i + 1 == list_len) and isOdd:
        break
    if bool(i % 2):
        my_list[i] = my_list[i - 1]
        my_list[i - 1] = value
    i = i + 1
print(my_list)

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict. 
"""

month_number = int(input("Enter month number: "))

months_list = enumerate(["Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Fall",
                         "Fall", "Fall", "Winter"])

for ind, season in months_list:
    if ind == month_number - 1:
        print("List implementation: ", season)

months_dic = {"Winter": [1, 2, 12], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Fall": [9, 10, 11]}

for key, value in months_dic.items():
    if month_number in value:
        print("Dic implementation: ", key)

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове. 
"""

my_list = input("Enter strings elements, use space for separator: ").split()

i = 0
for item in my_list:
    i = i + 1
    print(f"{i}. {item[0:10]}")

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент 
с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. 
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

while True:
    new_element = int(input("Enter new rating element. Type '-1' for exit: "))
    if new_element == -1:
        break
    new_list = my_list.copy()
    new_list.append(new_element)
    new_list.sort(reverse=True)
    print(new_list)


"""
6. Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: 
название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать 
все данные у пользователя.
Пример готовой структуры: 
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. 
Реализовать словарь, в котором каждый ключ — характеристика товара, например название, 
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""

units_list = []
i = 1

while True:
    unit_name = input("Enter unit name: ")
    unit_price = float(input("Enter unit price: "))
    unit_qty = int(input("Enter unit qty: "))
    unit_measure = input("Enter unit measure: ")
    unit_tpl = (i, {"name": unit_name, "price": unit_price, "qty": unit_qty, "measure": unit_measure})
    units_list.append(unit_tpl)
    i = i + 1
    print("New entity added: ")
    print(unit_tpl)

    if input("Enter 'Done' to complete or any key for continue: ") == 'Done':
        break

stat_dict = {}
for key in units_list[0][1].keys():
    stat_dict.update({key: []})

for list_item in units_list:
    for key, value in list_item[1].items():
        if value in stat_dict.get(key):
            break
        stat_dict.get(key).append(value)

print("Final analytics: ")
print(stat_dict)
