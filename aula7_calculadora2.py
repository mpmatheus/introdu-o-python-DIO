class Calculadora:
    def __init__(self):
       pass

    def soma (self, valor_a, valor_b) : 
        return valor_a + valor_b

    def subtracao (self, valor_a, valor_b) :
        return valor_a - valor_b

    def multiplicacao (self, valor_a, valor_b) :
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b) :
        return valor_a / valor_b

calculadora = Calculadora ()
print ('soma: {}'.format (calculadora.soma(10, 2)))
print ('subtracao: {}'.format (calculadora.subtracao(5, 3)))
print ('multiplicacao: {}'.format (calculadora.multiplicacao(10, 5)))
print ('divisao: {}'.format (calculadora.divisao(100, 2)))