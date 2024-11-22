#fazendo split dos dados
def split_string_palavras(text):
  return text.split()
texto = "esta função será bastante util para separar grandes volumes de dados."
#isso divide a sting em uma lista de palavras
print(split_string_palavras(texto))
#podemos atribuir o output de uma função para uma variavel
token = split_string_palavras(texto)
print(token)

#fazendo split dos dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
      print(letra)
split_string_letras(texto)
