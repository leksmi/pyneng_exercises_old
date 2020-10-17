# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_add = input('Enter an ip address: ').split('.')

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
