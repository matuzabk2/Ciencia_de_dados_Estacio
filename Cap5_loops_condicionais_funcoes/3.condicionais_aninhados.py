#condicionais aninhados
idade = 18
if idade > 17:
  print("voce pode dirigir!")

nome = "bob"
if idade > 13:
  if nome == "bob":
    print("ok bob, voce esta autorizado a entrar!")
  else:
    print("desculpe, mas voce nao pode entrar!")

idade = 13
nome = "bob"
if idade >= 13 and nome == "bob":
  print("ok bob, voce esta autorizado a entrar!")

idade = 12 
nome = "bob"
if (idade >= 13) or (nome == "bob"):
  print("ok bob, voce esta autorizado a entrar!")
