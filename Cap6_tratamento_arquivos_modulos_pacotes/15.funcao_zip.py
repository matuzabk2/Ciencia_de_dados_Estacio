#criando duas listas
x = [1,2,3]
y = [4,5,6]

#unindo as listas. retorna um iterator

#perceba que zip retorna tuplas. neste caso, uma lista de tuplas
print(list(zip(x,y)))

#atenção quando as sequencias tiverem numero diferente de elementos
print(list(zip('ABC', 'xy')))
#criando duas listas
a = [1,2,3]
b = [4,5,6,7,8]
print(list(zip(a,b)))

#criando 2 dicionarios
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

#zip vai unir as chaves
print(list(zip(d1,d2)))

#zip pode unir os valores (itens)
print(list(zip(d1, d2.values())))

#criando uma função para trocar valores entre 2 dicionarios
def trocaValores(d1, d2):
  dicTemp = {}
  for d1key, d2val in zip(d1, d2.values()):
    dicTemp[d1key] = d2val
  return dicTemp
print(trocaValores(d1, d2))
