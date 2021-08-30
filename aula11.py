

from typing import final


lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read ()
    divisao = 10 / 0
    numero = lista[1]
    # x = a
    # print('fechando arquivo')
    # arquivo.close()

except ZeroDivisionError:
    print('nao é possivel realizar uma divisao por zero')
except ArithmeticError:
    print ('houve um erro ao realizar a operacao aritmetica')
except IndexError :
    print('erro ao acessasr um indice errado da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
except: # se nao colocar nada ele trata todos os erros como um erro generico
    print('erro desconhecido')

else:
    print('executa quando nao houver nenhum erro')
finally:
    print('sempre executa')
    print('fechando arquivo')
    arquivo.close()