# function Return
def configure_intf(intf_name, ip, mask):
    config_if = f'interface {intf_name}\n'
    config_ip = f'ip address {ip} {mask}'
    return config_if, config_ip

result = configure_intf('Gi0/1', '10.10.10.1', '255.255.255.252')
intf, ip_add = configure_intf('Gi0/1', '10.10.10.1', '255.255.255.252')

# print(result, '\n')

# -----------------------------
# Функции Параметры и Аргументы
# Параметры - переменные при создании функции (в скобках)
# Аргументы - сами данные которые передаем при вызове функции
def check_passwd(username, password):
    if len(password) < 8:
        print('Password is too short!')
        return False
    elif username in password:
        print('Username in Password!')
        return False
    else:
        print(f'Password for user {username} is OK !')
        return True

# check_pass_res = check_passwd('someuser', 'someuser12345')
# print(check_pass_res)

# Параметры со значением по умолчанию: имя_параметра=значение_по_умолчанию
# Тогда при вызове функции их можно не указывать (уже есть значение по умолчанию) или переопределить на свое
def check_passwd_1(username, password, min_len=8):
    if len(password) < min_len:
        print('Password is too short!')
        return False
    elif username in password:
        print('Username in Password!')
        return False
    else:
        print(f'Password for user {username} is OK !')
        return True

# print(check_passwd_1('user', 'password', 5))

def check_passwd_2(username, password, min_len=8, check_username=True):
    if len(password) < min_len:
        print('Password is too short!')
        return False
    elif check_username and username in password:
        print('Username in Password!')
        return False
    else:
        print(f'Password for user {username} is OK !')
        return True

# print(check_passwd_2('admin', 'administrator11', 10, True))  # Тут все позиционные, важен порядок
# print(check_passwd_2('admin', 'administrator11', min_len=10, check_username=False)) # смешанный вариант, позиционные д.б. слева

# ---
# Аргументы переменной длинны
# 1. Позиционные. На месте *args можно указать любое кол-во арг-в, в т.ч. НИОДНОГО!
def sum_arg(a, *args):
    print(a, args)
    return a + sum(args)

#print(sum_arg(10, 20, 50))
#print(sum_arg(5, 12, 18, 200))
#print(sum_arg(55))

def sum_arg_1(*args):
    print(args)
    return sum(args)

print(sum_arg_1(5, 15, 25))

# 2. Ключевые аргументы переменной длины (словарь)00
# Указывают с помощью ** (принято **kwargs)
def sum_kargs(a, **kwargs):
    print(a, kwargs)
    return a + sum(kwargs.values())

#print('Summ of **kwargs: ', sum_kargs(a=5, c=15, d=30, f=10))

# Распаковка аргументов
# 1. Позиционных (упорядоченных)
# На примере строкового метода .format()
items = [1, 2, 3]
print('One: {} Two: {} Three: {}'.format(items[0], items[1], items[2]))
# Распаковкой:
print('One: {} Two: {} Three: {}'.format(*items))

def config_interface(intf_name, ip_address, mask):
    interface = f'interface {intf_name}'
    no_shut = 'no shutdown'
    ip_addr = f'ip addres {ip_address} {mask}'
    result = [interface, no_shut, ip_addr]
    return result

print(config_interface('Gi0/0', '10.10.10.1', '255.255.255.252'))

# Если данных (параметров интерфейсов в этом примере) много:
interfaces_info = [['Fa0/1', '10.0.1.1', '255.255.255.0'],
                   ['Fa0/2', '10.0.2.1', '255.255.255.0'],
                   ['Fa0/3', '10.0.3.1', '255.255.255.0'],
                   ['Fa0/4', '10.0.4.1', '255.255.255.0'],
                   ['Lo0', '10.0.0.1', '255.255.255.255']]

# Тогда каждый элемент списка нужно "распаковать" звездой:
for info in interfaces_info:
    print(config_interface(*info))

# Проверка IP адреса:
# 1. Функция проверки валидности адреса
import ipaddress
def check_ip(ip_address, verbose=False):
    try:
        ipaddress.ip_interface(ip_address)
        return True
    except ValueError as err:
        if verbose:
            print(err)
        return False

# 2. Функция проверки группы (списка) адресов
def return_correct_ip(*ip_addr):
    print(ip_addr)
    correct = []
    for ip in ip_addr:
        if check_ip(ip):
            correct.append(ip)
    return  correct

ip1 = '10.1.1.1/30'
ip2 = '192.168.1.0/24'
ip3 = '10.256.1.1/30'
ip4 = '192.168.1.1/30'
print(return_correct_ip(ip1, ip2, ip3, ip4))

