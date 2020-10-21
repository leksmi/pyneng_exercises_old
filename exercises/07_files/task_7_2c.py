# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

file_data = argv[1]
file_target = argv[2]

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
