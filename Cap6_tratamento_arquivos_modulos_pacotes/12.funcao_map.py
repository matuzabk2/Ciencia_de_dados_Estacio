#Função python que retorna um numero ao quadrado
def potencia(x):
  return x ** 2
numeros = [1, 2, 3, 4, 5]
numero_ao_quadrado = list(map(potencia,numeros))
print(numero_ao_quadrado)

#criando duas funções
#função 1 - recebe uma temperatura como parametro e retorna a temperatura em fahrenheit
def fahrenheit(T):
  return ((float(9)/5)*T + 32)

#função 2 - recebe uma temperatura como parametro e retorna a temperatura em celsius
def celsius(T):
  return(float(5)/9)*(T-32)

#criando uma lista
temperaturas = [0, 22.5, 40, 100]

#aplicando a função a cada elemento da lista de temperaturas
#em python 3, a função map() retornar um iterator
print(map(fahrenheit, temperaturas))

#Função map() retornando a lista de temperaturas convertidas em fahrenheit
print(list(map(fahrenheit, temperaturas)))

#usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
  print(temp)

#convertendo para celsius
map(celsius, temperaturas)
print(list(map(celsius, temperaturas)))

#usando expressão lambda
map(lambda x: (5.0/9)*(x - 32), temperaturas)
print(list(map(lambda x: (5.0/9)*(x - 32), temperaturas)))

#somando os elementos de 2 lista
a = [1,2,3,4]
b = [5,6,7,8]
print(list(map(lambda x,y:x+y, a, b)))
#somando os elementos de 3 listas
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
print(list(map(lambda x, y, z : x + y + z, a ,b, c)))
