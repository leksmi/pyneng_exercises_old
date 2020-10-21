# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

file_data = argv[1]
file_target = 'config_sw1_cleared.txt'
with open(file_data, 'r') as f, open(file_target, 'w') as ftarget:
    for line in f:
        marker = True
        for deny_word in ignore:
            if deny_word in line:
                marker = False
        if not marker:
            continue
        else:
            ftarget.write(line)
