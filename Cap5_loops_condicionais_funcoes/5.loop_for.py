#criando uma tupla e imprimindo cada um dos valores
tp = (2,3,4)
for i in tp:
  print(i)

#criando uma lista e imprimindo cada um dos valores
ListaDeStrings = ["Data", "Science","Academy"]
for i in ListaDeStrings:
  print(i)

#imprimindo os valores no intervalo entre 0 e 5(exclusive) RANGE
for contador in range(0,5):
  print(contador)

#imprimindo os numeros pares da lista de numeros
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
  if num %2 == 0:
    print(num)

#listando os numeros no intervalor entrte 0 a 100, com incremento em 2
for i in range(0,101,2):
  print(i)

#string tambem sao sequencias
for caracter in 'python é uma linguagem de programaçao divertida!':
  print(caracter)
