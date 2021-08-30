
lista = [12, 10, 7, 5] #lista e criada entre chaves
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
lista_animal [0] = "macaco" #mudar um valor especifico da lista
print(lista_animal)

tupla = (1, 10, 12, 14) #a tupla e criada entre parenteses, a tupla nao é possovel alterar os valores
print(len(tupla)) #acessar numero de elementos que tem na lista

tupla_animal = tuple(lista_animal) #converte uma lista em uma tupla
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla) #converte tupla em lista
print(type(lista_numerica))
lista_numerica [0] = 100
print(lista_numerica)




#print (lista_animal[1])
#print(max(lista_animal))
# nova_lista = lista_animal * 3
# print(nova_lista)

# lista.sort()  #ordenar a lista por ordem numerica
# lista_animal.sort() #ordenar a lista por ordem alabetica
# print(lista)
# print(lista_animal)
# lista_animal.reverse() #ordenar a lista por ordem reversa
# print(lista_animal)



# if 'lobo' in lista_animal:
#     print('exite um lobo na lista')
# else:
#     print('nao existe um lobo na lista, sera incluido')
#     lista_animal .append('lobo')   #.append adiciona uma variavel na lista
#     print(lista_animal)

# lista_animal.pop()      #remove a ultima posicao da lista
#lista_animal.pop(1)       #remove atravez da posicao estabelecia
#lista_animal .remove('elefante')   #remover um elemento que eu ja conheco

#print(lista_animal)