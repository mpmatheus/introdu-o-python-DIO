class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma (self) : 
        return self.valor_a + self.valor_b

    def subtracao (self) :
        return self.valor_a - self.valor_b

    def multiplicacao (self) :
        return self.valor_a * self.valor_b

    def divisao (self) :
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora (10, 2)
    print ('valor a: {}'.format (calculadora.valor_a))
    print ('valor b: {}'.format (calculadora.valor_b))
    print ('soma: {}'.format (calculadora.soma()))
    print ('subtracao: {}'.format (calculadora.subtracao()))
    print ('multiplicacao: {}'.format (calculadora.multiplicacao()))
    print ('divisao: {}'.format (calculadora.divisao()))












# #definicao
# def soma (a, b) : #faz uma definiçao que tem 2 parametros
#     return a + b #o que essa definicao vai retornar

# def subtracao (a, b) :
#     return a - b

# def multiplicacao (a, b) :
#     return a * b

# def divisao (a, b) :
#     return a / b

# print ('soma: {}'.format (soma(1, 2))) #chama a definicao colocando o valor dos 2 parametros
# print ('soma: {}'.format (soma(3, 4)))
# print ('subtracao: {}' .format (subtracao(10, 2)))
# print ('multiplicacao: {}'.format (multiplicacao (10 ,2)))
# print ('divisao: {}'.format (divisao(10 ,2)))