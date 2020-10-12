# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

# Шаблон запроса VLAN в зависимости от режима порта (подставим его далее в input):
vlan_template = {
    'access': 'Введите номер VLAN: ',
    'trunk': 'Введите разрешенные VLANы: '
}

# Get data from user:
int_mode = input('Введите режим работы интерфейса (access/trunk): ')
int_numb = input('Введите тип и номер интерфейса: ')
vlan_s = input(vlan_template[int_mode])

int_templates = {
    'access': [
        "switchport mode access",
        "switchport access vlan {}".format(vlan_s),
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    ],
    'trunk': [
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        "switchport trunk allowed vlan {}".format(vlan_s)
    ]
}

print('\n')
print(f'interface {int_numb}', '\n'.join(int_templates[int_mode]), sep='\n')
