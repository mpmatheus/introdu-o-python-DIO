a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('voce digitou errado. primeiro bimestre: '))
b = int(input('segundo bimestre: '))
if b > 10:
    b = int(input('voce digitou errado. segundo bimestre: '))
c = int(input('terceiro bimestre: '))
if c > 10:
    c = int(input('voce digitou errado. terceiro bimestre: '))
d = int(input('quarto bimestre: '))
if d > 10:
    d = int(input('voce digitou errado. quarto bimestre: '))
media = (a + b + c + d) / 4
print ('media: {} '.format(media) )




 
# #compara as 4 notas e retorna o valor da media 
# a = int(input('primeiro bimestre: '))
# b = int(input('segundo bimestre: '))
# c = int(input('terceiro bimestre: '))
# d = int(input('quarto bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print ('media: {}'.format (media))
# else:
#     print('foi informada alguma nota errada')


# #compara 2 numeros e retorna se pelo menos 1 é par
# a = int(input('entre com primeiro valor: '))
# b = int(input('entre com segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b ==0:
#     print('foi digitado um numero par')
# else:
#     print('nenhum numero par foi digitado')



# compara se o numero é par
# a = int(input('entre com primeiro valor: '))
# resto = a % 2
# if resto == 0: #== serve para comparar 
#     print('numero é par')
# else:
#     print('numero é impar')


# compara 3 numeros para mostrar qual o maior
# a = int(input('primeiro valor: '))
# b = int(input('segundo valor: '))
# c = int(input('terceiro valor: '))
# if a > b and a > c: #comparando as variaveis a com b c para saber SE a é maior
#     print('o maior numero é: {}' .format (a))
# elif b > a and b > c:# SE a nao for maior faz um else+if=elif para comparar se b é maior
#     print('o maior numero é: {}'.format (b))
# else:#senao for nem a nem b sobra c 
#     print('o maior numero é: {}'.format(c))
# print('final do programa')