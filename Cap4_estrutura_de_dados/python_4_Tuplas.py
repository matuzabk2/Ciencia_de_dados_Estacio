#criando uma tupla
tupla1 = ("geografia",23, "elefantes", 9.8, 'python')

#imprimindo a tupla
print(tupla1)

#tuplas nao suportam append
#tupla1.append("chocolate")

#tuplas nao suportam delete de um item especifico ex:
#del tupla["elefantes"]

#tuplas podem ter um unico item
tupla1 = ("chocolate")
print(tupla1)
tupla1 = ("geografia", 23, "elefantes", 9.8, 'python')
print(tupla1[0])

#verificando o comprimento da tupla
len(tupla1)

#slicing, da mesma forma que se faz com listas
tupla1[1:]
print(tupla1.index('elefantes'))

#tuplas nao suportam atribuiçao de item ex:
#tupla[1] = 21

#deletando a tupla
#del tupla1
print(tupla1)

#criando uma tupla
t2 = ('A', 'B', 'C')

#tuplas nao suportam atribuiçao de itens
#t2[0] = ''

#usando a funçao list() converter uma tupla para lista
lista_t2 = list(t2)
print(lista_t2)
lista_t2.append('D')

#usando a funçao tuple() para converter uma lista em tupla
t2 = tuple(lista_t2)
print(t2)
