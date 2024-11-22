#criando uma lista de listas
#
listas = [[1,2,3],[10,15,14],[10.1,8.7,2.3]]
#imprimindo a lista
print(listas)
#atribuindo um item da lista a uma variavel
a = listas[0]
print(a) 

b = a[0]
print(b)

list1 = listas[1]
print(list1)

valor_1_0 = list1[2]
print(valor_1_0)

valor_1_2 = list1[2]
print(valor_1_2)

list2= listas[2]
print(list2)

valor_2_0 = list2[0]
print(valor_2_0)

#operaçoes com listas
a = listas[0][0]
print(a)

b = listas[1][2]
print(b)

c = listas[0][2] + 10
print(c)

d = 10
print(d)

#concatenando listas
lista_s1 = [34,32,56]
print(lista_s1)

lista_s2 =[21,90,51]
print(lista_s2)

#concatenando listas
lista_total = lista_s1 + lista_s2
print(lista_total)

#operador in
#criando uma lista
lista_teste_op = [100, 2, -5, 3.4]
#verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)
#verificando se o valor 100 pertence a lista
print(100 in lista_teste_op)

#funçoes built-in
#criando uma lista
lista_numeros = [10,20,50, -3.4]

#funçao len() retorna o comprimento da lista
len(lista_numeros)

#funçao max() retorna o valor maximo da lista
min(lista_numeros)

#criando uma lista
lista_formacoes_dsa = ["analista de dados", "cientista de dados", "engenheiro de dados"]

#adicionando um item a lista
lista_formacoes_dsa.append("engenheiro de IA")
print(lista_formacoes_dsa)
lista_formacoes_dsa.append("engenheiro de IA")
print(lista_formacoes_dsa)
print(lista_formacoes_dsa.count("engenheiro de IA"))

#criando uma lista vazia
a = []
print(a)
a.append(10) 
print(a)
a.append(50)
print(a)

old_list = [1,2,5,10]
new_list = []

#copíando os itens de uma lista para outra
for item in old_list:
  new_list.append(item)
print(new_list)

cidades = ['recife', 'manaus', 'salvador']
cidades.extend(['fortaleza,' 'palmas'])
print(cidades)

cidades.index('rio de janeiro')
print(cidades)

cidades.insert(2,110)
print(cidades)

#remove um item da lista
cidades.remove(110)
print(cidades)

#reverte a lista
cidades.reverse()
#imprime a lista
print(cidades)

x = [3, 4, 2, 1]
