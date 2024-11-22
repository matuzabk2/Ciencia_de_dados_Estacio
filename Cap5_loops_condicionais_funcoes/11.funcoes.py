print('hello world')

#definindo uma função
def primeiraFuncao():
  print('hello world')
print(primeiraFuncao())

#definindo uma função
def primeiraFuncao():
    nome = 'bob'
    print('hello %s' %(nome))
primeiraFuncao()


#definindo uma função com parametro
def segundaFuncao(nome):
  print('hello %s' %(nome))
segundaFuncao('aluno')

#função para imprimir numeros
def imprimeNumeros():
  #loop
  for i in range(0, 5):
    print("numero " + str(i))
imprimeNumeros()

#funçao para somar numeros
def addnum(firstnum, secondnum):
  print("primerio numero: " + str(firstnum))
  print("segundo numero: " + str(secondnum))
  print("soma: ", firstnum + secondnum)
#chamando a funçao e passando parametros
addnum(4, 7)

#chamando a funçao e passando outros parametros
addnum(45, 3)

#funçoes com numero variavel de argumentos
def printVarInfo(arg1, *vartuple):
  #imprimindo o valor do primeiro argumento
    print("o parametro passado foi:", arg1)
    #imprimindo o valor do segundo argumento
    for item in vartuple:
        print("o parametro passado foi:", item)
    return;
#fazendo chamada a função usando apenas 1 argumento
printVarInfo(10)
printVarInfo('chocolate', 'morango')
printVarInfo('data', 'science','academy')
