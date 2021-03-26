# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

def ping_ip_addresses(ip_list):
    reach_ip = []
    unreach_ip = []
    for ip_add in ip_list:
        result = subprocess.run(f'ping -n -c 3 {ip_add}'.split(), stdout=subprocess.PIPE, encoding='utf-8')
        if 'ttl' in result.stdout.lower():
            reach_ip.append(ip_add)
        else:
            unreach_ip.append(ip_add)
    # print(f'Reachable IPs : {reach_ip}', f'\nUnreachable IPs : {unreach_ip}')
    return reach_ip, unreach_ip

ip_addresses = ['10.252.136.210', '10.252.136.211', '10.252.136.212', '10.252.136.213', '10.252.136.214', '10.252.136.215']

print(ping_ip_addresses(ip_addresses))