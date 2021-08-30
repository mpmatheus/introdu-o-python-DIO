# a = 10
# b = 5
a = int(input('entre com primeiro valor: '))#variavel declarada e string necessario converter para numero inteiro
b = int(input('entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

soma = str(soma) #converte a variavel soma de inteiro para string
print('soma: {soma}. \nsubtracao: {subtracao}. \nmultiplicacao: {multiplicacao}.\ndivisao: {divisao}. \nresto: {resto}'.format(soma=soma, subtracao=subtracao, multiplicacao=multiplicacao, resto=resto, divisao=divisao)) #\n quebra de linha, nao sendo necessario fazer outro print
# print('soma: ' + soma) #com as 2 variaveis como string a soma contatena o resultado
# print('subtracao: ' + subtracao)
# print(multiplicacao)
# print(divisao)
# print(int(divisao)) #converte de variavel float para inteiro
# print(resto)

# x = '1' #salva a variavel x como string
# soma2 = int(x) + 1 #converte a variavel x para inteiro e faz a soma
# print(soma2)
