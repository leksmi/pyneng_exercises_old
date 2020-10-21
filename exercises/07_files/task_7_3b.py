# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

file_data = 'CAM_table.txt'
vlan_info = input('Введите номер vlan: ')

with open(file_data, 'r') as f:
    result_list = []
    for line in f:
        if not line.strip():
            continue
        line_list = line.split()
        if line_list[0].isdigit(): # Если первый элемент число (номер влана) то используем эту строку
            line_list.pop(2)       # Удаляем лишнее поле
            result_list.append(line_list)

# Преобразуем первую колонку из str в int для дальнейшей сортировки:
for line in result_list:
    line[0] = int(line[0])

# Сортировка по первому элементу (по умолчанию метода) который теперь - число. Список заменяется новым !:
result_list.sort()

# Окончательный вывод через форматирование:
for line in result_list:
    if line[0] == int(vlan_info):
        print(f'{line[0]:<7} {line[1]:<20} {line[2]:<10}')
