
class Error (Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message = message


while True:
    try:
        x = int(input('entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('nota nao pode ser maior que 10')
        elif x < 0 :
            raise InputError('nota nao pode menor que zero')
        break
    except ValueError:
        print('valor invalido. deve-se digitar apenas numeros.')
    except InputError as ex:
        print(ex)