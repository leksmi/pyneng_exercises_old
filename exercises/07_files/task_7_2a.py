# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

file_data = argv[1]
with open(file_data, 'r') as f:
    for line in f:
        marker = True
        for deny_word in ignore:
            if deny_word in line:
                marker = False
        if line.startswith('!') or (not marker):
            continue
        else:
            print(line.rstrip())

