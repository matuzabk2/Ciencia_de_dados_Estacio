#importando a função reduce do modulo functools
from functools import reduce

from IPython.display import Image
Image('C:/Users/gabri/Desktop/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/reduce.png')

#criando uma lista
lista = [47, 11, 42, 13]
print(lista)

#função
def soma(a,b):
  x = a + b
  return x

#usando reduce com uma função e uma lista. a função vai retornar o valor maximo
print(reduce(soma, lista))

#criando uma lista
lst = [47, 11, 42, 13]

#usando a função reduce() com lambda
reduce(lambda x,y: x+y, lst)

#podemos atribuir a expressão lambda a uma variavel
max_find2 = lambda a,b: a if (a > b) else b
print(type(max_find2))

#reduzindo a lista ate o valor maximo, atraves da função criada com a expressão lambda
print(reduce(max_find2, lst))
