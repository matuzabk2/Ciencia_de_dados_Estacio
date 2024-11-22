import math

#verificando se um numero é primo
def numPrimo(num):
  if (num % 2) == 0 and num > 2: 
    return "este numero nao é primo"
  for i in range(3, int(math.sqrt(num)) + 1, 2):
    if (num % i) == 0:
      return "este numero nao é primo" 
  return "este numero é primo"

print(numPrimo(541))
print(numPrimo(2))

caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"
def lowercase(text):
  return text.lower()
#texto antes da converçao
print(caixa_baixa)

#convertendo a caixa baixa para caixa alta para verificar se o metodo esta funcionando corretamente
lowercased_string = lowercase(caixa_baixa)
print("\n",lowercased_string)
