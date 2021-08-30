from aula7_televisao import Televisao #importar somente a classe televisao do arquivo
from aula7_calculadora1 import Calculadora 
from aula8_contador_letras import contador_letras, teste #importar mais de uma classe do arquivo



if __name__ == "__main__": # so roda essa parte se for o arquivo main
    televisao = Televisao ()
    print (televisao.ligada)
    televisao.power ()
    print (televisao.ligada)
    calculadora = Calculadora (5, 10)
    print (calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print ('total de letras da lista: {}'.format(total_letras))
    print (teste())
