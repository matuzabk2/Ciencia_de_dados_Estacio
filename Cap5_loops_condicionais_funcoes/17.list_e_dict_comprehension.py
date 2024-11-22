#list comprehension
#list comprehension que imprime os numeros até 10
[x for x in range(10)]

#list comprehension que imprime os numeros ate 10 e grave em uma lista python
lista_numeros = [x for x in range(10)]
print(lista_numeros)

#list comprehension que imprime numeros menores que 5 em um intervalo de 1 a 10
lista_numeros = [x for x in range(10) if x < 5]
print(lista_numeros) 

#lista de frutas
lista_frutas = ['banana', 'abacate', 'melancia', 'cereja', 'manga']
#nova lista
nova_lista = []

#loop tradicional para buscar as palavras com a letra "M"
for x in lista_frutas:
  if "m" in x:
    nova_lista.append(x)
print(nova_lista)

#mesmo resultado anterior mas com list comprehension
nova_lista = [x for x in lista_frutas if "m" in x]
print(nova_lista)

#dict comprehension
#dicionario de alunos e notas
dict_alunos = {'Bob':68, 'Michel':84, 'Zico':57, 'Ana':93}
#criamos um novo dicionario imprimindo os pares de chave:valor
dict_alunos_status = {k:v for (k,v) in dict_alunos.items()}
print(dict_alunos_status)

#dict comprehension
#dicionarios de alunos e nota
dict_alunos = {'Bob':68, 'Michel':84, 'Zico':57, 'Ana':93}
#criamos um novo dicionario imprimindo apenas os alunos com notas acima de 70, aprovado, senao, reprovado
dict_alunos_status = {k:('Aprovado' if v > 70 else 'reprovado') for (k, v) in dict_alunos.items()}
print(dict_alunos_status)
