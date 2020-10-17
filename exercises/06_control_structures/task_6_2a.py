# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip_add = input('Enter an ip address: ').split('.')

if len(ip_add) != 4:
    print('Неправильный IP-адрес !')
    exit(1)
for oct in ip_add:
    if not oct.isdigit():
        print('Неправильный IP-адрес !')
        exit(1)
    if (int(oct) < 0 or int(oct) > 255):
        print('Неправильный IP-адрес !')
        exit(1)

octs_sum = int(ip_add[0]) + int(ip_add[1]) + int(ip_add[2]) + int(ip_add[3])

if octs_sum == 0:   # check for sum 0
    print('The ip address is *unassigned* :', '.'.join(ip_add))
elif octs_sum == 1020:  # check for sum 1020
    print('The ip address is *local broadcast* :', '.'.join(ip_add))
elif (int(ip_add[0]) >= 1) and  (int(ip_add[0]) <= 223):
    print('The ip address is *unicast* :', '.'.join(ip_add))
elif (int(ip_add[0]) >= 224) and  (int(ip_add[0]) <= 239):
    print('The ip address is *multicast* :', '.'.join(ip_add))
else:
    print('The ip address is *unused* :', '.'.join(ip_add))

