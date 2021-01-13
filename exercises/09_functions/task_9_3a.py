# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from pprint import pprint


def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename, 'r') as conf:
        for line in conf:
            if 'Ethernet'.lower() in line.lower():
                if_name = line.split()[-1]        # извлекаем имя/номер интерфейса
                access_dict.update({if_name: 1})  # и по умолчанию интерфейс записываем в словарь аксессных портов с вланом 1
            elif 'access vlan' in line:    # проверка, что порт аксесный
                acc_vlan = int(line.split()[-1])  # взяли последний элемент (строка с вланом) с конвертацией в число
                access_dict.update({if_name: acc_vlan})  # методом update обновляем интерфейс с нужным вланом вместо 1
            elif 'allowed vlan' in line:   # проверка, что порт транковый
                del access_dict[if_name]   # если транковый, удалить интерфейс из словаря аксессных портов
                tr_vlans = line.split()[-1].split(',')  # взяли последний элемент (строка с вланами) и преобразовали в список
                for i in range(len(tr_vlans)):  # конвертируем элементы списка
                    tr_vlans[i] = int(tr_vlans[i])  # из str -> int
                trunk_dict.update({if_name: tr_vlans})  # методом update добавляем элемент словаря

    result_tuple = (access_dict, trunk_dict)
    return result_tuple


# Проверка работы:
print(get_int_vlan_map('config_sw2.txt'), '\n')
pprint(get_int_vlan_map('config_sw2.txt'))
