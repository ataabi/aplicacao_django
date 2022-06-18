# def msg_azul(msg):
#     return f'\033[34m{msg}\033[m'
#
# print(msg_azul('esta mensagem esta em azul'))

def cores(msg: str, int, cor: str = None) -> str:
    if cor is None:
        return msg

    if cor == 'White':
        return f'\033[30m{msg}\033[m'
    elif cor == 'Red':
        return f'\033[31m{msg}\033[m'
    elif cor == 'Green':
        return f'\033[32m{msg}\033[m'
    elif cor == 'Yellow':
        return f'\033[33m{msg}\033[m'

    elif cor == int():
        return f'\033[{cor}m{msg}\033[m'

    elif '\033' in cor:
        return f'{cor}{msg}\033[m'

def triangulo(reta1: float, reta2: float, reta3: float) ->float:
    if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
        print('Esses segmentos formam um triangulo')
        if reta1 == reta2 == reta3:
            print('Esse triangulo é EQUILÁTERO')
        elif reta1 != reta2 != reta3 != reta1:
            print('Esse triangulo é ESCALENO')
        else:
            print('Esse triangulo é ISÓSCELES')
    else:
        print('Esses segmentos não formam um triangulo')

if __name__ == '__main__':

    from math import sqrt

    n1 = sqrt(9)
    print(n1)

    n2 = 9 * 9
    print(n2)