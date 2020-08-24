# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
#
vlans1 = command1.split()[-1].split(',')
vlans2 = command2.split()[-1].split(',')
vlans1_set = set(vlans1)
vlans2_set = set(vlans2)
vlans_unique = sorted(list(vlans1_set & vlans2_set))
print('Общие вланы с сортировкой (решение): ', vlans_unique)
