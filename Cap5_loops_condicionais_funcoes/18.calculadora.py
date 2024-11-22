# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def soma(x, y):
  return x +y

def subtracao(x, y):
  return x - y

def multiplicacao(x, y):
  return x * y

def divisao(x, y):
  return x / y

#escolha das operações no menu
escolha = input("digite a operação desejada (1, 2, 3, 4). Digite sair para encerrar: ")

while escolha != 'sair':
    numero1 = input("Digite o primeiro numero: ")
    numero2 = input("Digite o segundo numero: ")

    if escolha == '1':
      print("\n")
      print(numero1, "+", numero2, "=", soma(float(numero1), float(numero2)))
    
    elif escolha == '2':
      print("\n")
      print(numero1, "-", numero2, "=", subtracao(float(numero1), float(numero2)))
    
    elif escolha == '3':
      print("\n")
      print(numero1, "*", numero2, "=", multiplicacao(float(numero1), float(numero2)))
    
    elif escolha == '4':
      print("\n")
      print(numero1, "/", numero2, "=", divisao(float(numero1), float(numero2)))
    
    else:
      print("\nOperação inválida!")
  
      

  