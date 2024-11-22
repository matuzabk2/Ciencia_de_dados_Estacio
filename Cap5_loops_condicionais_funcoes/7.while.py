#usando o loop while para imprimir os valores de 0 a 9
#a condiçao tem q deixar de ser verdadeira dentro do loop, senao pode travar o navegador ou mesmo o computador
valor = 0
while valor < 10:
  print(valor)
  valor = valor + 1

#entra no loop somente se a condiçao for verdadeira
valor = 11
while valor < 10:
  print(valor)
  valor = valor + 1
  break
#tambem é possivel usar a clausula else para encerrar o loop while
x = 0
while x < 10:
  print('o valor de x nesta iteração é:', x)
  print('x ainda é menor que 10, somando 1 a x')
  x += 1
else:
  print('loop concluído')
print(x)
print('\n')

#pass,break,continue
#se encontramos o numero 4 interrompemos o loop
valor = 0
while valor < 10:
  if valor == 4:
    break
  else:
    pass
  print(valor)
  valor = valor + 1
print('\n')

#desconsideramos a letra z ao imprimir os caracteres da frase
for letra in "python é zzz incrivel!":
  if letra == 'z':
    continue
  print(letra)
