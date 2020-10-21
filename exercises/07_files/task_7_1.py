# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

route_params = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
# route_dict = dict.fromkeys(route_params)
# print(route_dict)
# Open file with context manager:
with open('ospf.txt', 'r') as f:
    for line in f:
        line_list = line.split()
        line_list.remove('O')
        line_list.remove('via')
        # print(line_list)
        for i in range(len(route_params)):
            print(f'{route_params[i]:<25} {line_list[i].strip(","):<25}')
        print('\n')


