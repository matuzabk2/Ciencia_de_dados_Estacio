#loop for aninhado
lista1 = [0,1,2,3,4]
lista2 = [1,2,3]

#loop externo
for elemento_lista1 in lista1:
  #loop interno
  for elemento_lista2 in lista2:
    print('\n', elemento_lista1 * elemento_lista2)
  print('---')

#o numero 47 aparece nas duas listas?

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
#loop externo
for elemento_lista1 in lista1:
  #loop inerno
  for elemento_lista2 in lista2:
    #condicional
    if elemento_lista1 == 47 and elemento_lista2 == 47:
      print("o numero 47 foi encontrado nas duas listas")

#some os numeros pares da primeira lista com os numeros pares da segunda lista
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0

#loop externo
for lista in [lista1, lista2]:
  #loop interno
  for num in lista:
    #condicional
    if num % 2 == 0:
      soma += num
print("a soma dos numeros pares das duas listas é igual a: ",soma)

#listas pode ser concatenas em python
lista1 + lista2

#some os numeros pares da primeira lista com os numeros pares da segunda lista
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0
for num in lista1 + lista2:
  if num %2 == 0:
    soma += num
print("soma dos valores pares: ", soma)

#loop em lista de listas (matrizes)
matriz = [[42,23,34],[100,215,114],[10.1,98.7,12,3]]
maior_numero = 0
#loop externo
for linha in matriz:
  #loop interno
  for num in linha:
    #condicional
    if num > maior_numero:
      maior_numero = num
print("maior numero", maior_numero)

#listando as chaves de um dicionario
dict = {'K1':'Python','K2':'R','K3':'Scala'}
for item in dict:
  print(item)

#imprimindo a chave e valor do dicionario usando o metodo items() para retornar os itens de um dicionario
for k,v in dict.items():
  print(k,v)
