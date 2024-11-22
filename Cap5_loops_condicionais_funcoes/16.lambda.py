#definindo uma função - 3 linha de codigo
def potencia(num):
  resultado = num ** 2
  return resultado
print(potencia(5))

#definindo uma função - 2 linhas de codigo
def potencia(num):
  return num ** 2
print(potencia(5))

#definindo uma função - 1 linha de codigo
def potencia(num): return num ** 2
print(potencia(5))

#definindo uma expressão lambda (função anônima)
potencia_lambda = lambda num: num ** 2
print(potencia_lambda(5))

#lembre: operadores de comparação retornam boolean: true or false
par = lambda x: x%2==0
print(par(3))
print(par(4))

first = lambda s: s[0]
print(first ('Python'))

reverso = lambda s: s[::-1]
print(reverso('Python'))

addNum = lambda x, y: x + y
print(addNum(2, 3))
