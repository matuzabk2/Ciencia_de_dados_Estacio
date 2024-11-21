#condicional if...else
if 5 > 2:
  print("a sentença é verdadeira")
else:
  print("a sentença é falsa")

  #condicional if...else com variavel
  dia = "terça"
  if dia == "segunda":
    print("hoje fara sol")
  else:
    print("hoje vai chover")

#podemos usar o operador elif para validar mais de uma condição
if dia == "segunda":
  print("Hoje fara sol!")
else:
  print("hoje vai chover!")

#podemos usar o operador elif para validar mais de uma condição
if dia == "segunda":
  print("hoje fara sol!")
elif dia == "terça":
  print("hoje vai chover!")
else:
  print("sem previsao do tempo para o dia selecionado")
