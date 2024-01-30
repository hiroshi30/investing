import os


info = dict()
balance = dict()


def load_info(name='info.txt'):
    if os.path.exists(name):
        global info
        info = dict()
        with open(name, 'r', encoding='utf-8') as file:
            types_count = int(file.readline())
            for i in range(types_count):
                file.readline()
                _type, assets_count = file.readline().split()
                assets_count = int(assets_count)
                info[_type] = dict()
                for j in range(assets_count):
                    asset = file.readline().split(', ')
                    if _type == 'BANK':
                        info[_type][asset[0]] = [float(asset[1]), int(asset[2])]
                    elif _type == 'CRYPTOCURRENCY':
                        info[_type][asset[0]] = [asset[1], asset[2], float(asset[3]), float(asset[4]), int(asset[5])]
    else:
        print(f'load_info() no such file {name}')


def save_info(name='info.txt'):
    with open(name, 'w', encoding='utf-8') as file:
        file.write(f'{len(info)}\n')
        for _type in info:
            file.write(f'\n{_type} {len(info[_type])}\n')
            for asset in info[_type]:
                if _type == 'BANK':
                    file.write(f'{asset}, {info[_type][asset][0]}, {info[_type][asset][1]}\n')
                elif _type == 'CRYPTOCURRENCY':
                    file.write(f'{asset}, {info[_type][asset][0]}, {info[_type][asset][1]}, {info[_type][asset][2]}, {info[_type][asset][3]}, {info[_type][asset][4]}\n')


def load_balance(name='balance.txt'):
    if os.path.exists(name):
        global balance
        balance = dict()
        with open(name, 'r', encoding='utf-8') as file:
            types_count = int(file.readline())
            for i in range(types_count):
                file.readline()
                _type, assets_count = file.readline().split()
                assets_count = int(assets_count)
                balance[_type] = dict()
                for j in range(assets_count):
                    asset = file.readline().split()
                    balance[_type][asset[0]] = float(asset[1])
    else:
        print(f'load_balance() no such file {name}')


def save_balance(name='balance.txt'):
    with open(name, 'w', encoding='utf-8') as file:
        file.write(f'{len(balance)}\n')
        for _type in balance:
            file.write(f'\n{_type} {len(balance[_type])}\n')
            for asset in balance[_type]:
                file.write(f'{asset} {balance[_type][asset]}\n')


if __name__ == '__main__':
    load_info()
    save_info('test_load_info.txt')

    load_balance()
    save_balance('test_load_balance.txt')
