# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
#
param_list = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
route_list = ospf_route.split()
print(f'''
{param_list[0]:<20} {route_list[0]:<20}
{param_list[1]:<20} {route_list[1].strip('[]'):<20}
{param_list[2]:<20} {route_list[3].rstrip(','):<20}
{param_list[3]:<20} {route_list[4].rstrip(','):<20}
{param_list[4]:<20} {route_list[5].rstrip(','):<20}
''')
