#criando uma função
def verificaPar(num):
  if num % 2 == 0:
    return True
  else:
    return False
  
#chamando a função e passando um numero como parametro. retornara
#falso se for impar e true se for par
verificaPar(35)

#falso se for impar e tru se for par
verificaPar(10)
lista = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
print(lista)
print("\n")
#a função filter() retorna um iterator
filter(verificaPar, lista)
print(list(filter(verificaPar, lista)))
print("\n")
print(list(filter(lambda x: x%2==0, lista)))
print("\n")
print(list(filter(lambda num: num > 8, lista)))
