#testando tempo de execucao
import time
start_time = time.time()

#encontrando numeros primos entre 2 e 30 usando loop for e while
#variavel para armazenar numeros primos
primos = []

#loop for para percorrer numeros de 2 a 30
for num in range(2, 31):
  #variavel para verificar se o numero é primo
  eh_primo = True
  #loop while para verificar se o numero é primo
  i = 2
  while i <= num // 2:
    if num % i == 0:
      eh_primo = False
      break
    i += 1
  #adicionando o numero primo à lista
  if eh_primo:
    primos.append(num)

#imprimindo os numeros primos
print(primos)

#encontrando numeros primos entre 2 e 30 usando lop for e while (outro exemplo)
#loop for para percorrer numeros de 2 a 30
for i in range(2, 31):
  #variavel de controle
  j = 2
  #contador
  valor = 0
  #loop while para verificar se o numero é primo
  while j < i:
    if i % j == 0:
      valor = 1
      j = j + 1
    else:
      j = j + 1
  
  if valor == 0:
    print(str(i) + " é um número primo.")
    valor = 0
  else:
    valor = 0

#testando tempo de execucao
print("Process finished --- %s seconds ---" % (time.time() - start_time))
