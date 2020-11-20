# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а СЛОВАРЬ:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: СПИСОК команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from pprint import pprint

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

# Итоговый СЛОВАРЬ для заполнения:

# intf_vlan_mapping - словарь с парами интерфейс:[его вланы]
# trunk_template - список команд для интерфейса
def generate_trunk_config(intf_vlan_mapping, trunk_template):  #
    config_dict = {}
    for intf in intf_vlan_mapping:  # Перебираем интерфейсы (элементы словаря пары имя_интерфейса + вланы в нем)
        config_trunk = []
        config_trunk.append(f'interface {intf}')
        # Перебираем команды для интерфейса
        for command in trunk_template:
            # Проверка на необходимость подставить список вланов
            if command.endswith('allowed vlan'):
                # Так как в задании вланы в словаре заданы списком из int, преобразовываем его в str:
                vlans = str(intf_vlan_mapping[intf]).strip('[]')
                config_trunk.append(f'{command} {vlans}')
            else:
                config_trunk.append(command)
        intf_dict = {intf: config_trunk}
        config_dict.update(intf_dict)

    return config_dict

#pprint(generate_trunk_config(trunk_config, trunk_mode_template))
