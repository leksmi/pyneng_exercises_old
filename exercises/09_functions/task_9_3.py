# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает КОРТЕЖ из двух СЛОВАРЕЙ:
* словарь портов в режиме Access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}
* словарь портов в режиме Trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один ПАРАМЕТР config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint


def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename, 'r') as conf:
        for line in conf:
            if 'Ethernet'.lower() in line.lower():
                if_name = line.split()[-1]
            elif 'access vlan' in line:  # проверка, что порт аксесный
                acc_vlan = int(line.split()[-1])  # взяли последний элемент (строка с вланом) с конвертацией в число
                access_dict.update({if_name: acc_vlan})  # методом update добавляем элемент словаря
            elif 'allowed vlan' in line:  # проверка, что порт транковый
                tr_vlans = line.split()[-1].split(
                    ',')  # взяли последний элемент (строка с вланами) и преобразовали в список
                for i in range(len(tr_vlans)):  # конвертируем элементы списка
                    tr_vlans[i] = int(tr_vlans[i])  # из str -> int
                trunk_dict.update({if_name: tr_vlans})  # методом update добавляем элемент словаря

    result_tuple = (access_dict, trunk_dict)
    return result_tuple


# Проверка работы:
print(get_int_vlan_map('config_sw1.txt'), '\n')
pprint(get_int_vlan_map('config_sw1.txt'))
