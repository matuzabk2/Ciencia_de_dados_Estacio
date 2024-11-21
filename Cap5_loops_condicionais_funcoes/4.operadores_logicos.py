#operadores logicos
idade = 18
nome = "bob"
if idade > 17:
  print("voce pode dirigir\n")

idade = 18
if idade > 17 and nome == "bob":
  print("autorizado\n") 


#operador and - retorna true se ambas as declaraçoes forem verdadeiras.
#operador or - retorna true se uma das declaraçoes for verdadeira.
#operador not - inverte o resultado, retorna false se o resultador for true.


#operador and
numero = 4
if (numero > 2) and (numero % 2 == 0):
  print("isso esta sendo impresso porque as duas condicoes são verdadeiras!\n")


#operador and
numero = 4
if (numero > 5) and (numero % 2 == 0):
  print("isso esta sendo impresso porque as duas condiçoes sao verdadeiras\n")
else:
  print("isso esta sendo impresso porque uma das duas condiçoes é falsa\n")


#operador or
numero = 4
if (numero > 5) or (numero % 2 == 0):
  print("isso esta sendo impresso porque as duas condiçoes sao verdadeiras\n")


#operador not
numero = 4
if not(numero > 5) and (numero % 2 == 0):
  print("isso esta sendo impresso porque as duas condiçoes sao verdadeiras\n")
else:
  print("isso esta sendo impresso porque as condiçoes sao verdadeiras\n")


# operador and, or e not
numero = 4
if ((numero > 5) and (numero % 2 == 0)) or (numero == 4):
  print("isso esta sendo impresso porque as duas primeiras condiçoes sao verdadeiras ou a terceira é verdadeira!\n")


#exemplo com o uso de variaveis
disciplina = 'data science'
nota_final = 70
if disciplina == 'data science' and nota_final >= 70:
  print("voce foi aprovado\n")
else:
  print('lamento, acho que voce precisa estudar mais\n')


#usando mais de uma condiçao na clausula if
disciplina = 'data science'
nota_final = 60
if disciplina == 'data science' and nota_final >= 70:
  print('voce foi aprovado!\n')
else:
  print('lamento, acho que voce precisa estudar mais\n')

#usando mais de uma condiçao na clausaula if e introduzindo placeholders
disciplina = 'data science'
nota_final = 90
semestre = 2
if disciplina == 'data science' and nota_final >= 80 and semestre != 1:
  print('voce foi aprovado em %s com media final %r! \n' % (disciplina, nota_final))
else:
  print('lamento, acho que voce precisa estudar mais! \n')
