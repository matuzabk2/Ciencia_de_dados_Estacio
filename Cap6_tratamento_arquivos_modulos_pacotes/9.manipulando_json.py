#criando um dicionario: 'chave': valor ,
dict_guido = {'nome': 'guido van rossum',
              'linguagem':'python',
              'similar':['c','modula-3','lisp'],
              'users':1000000}
for k,v in dict_guido.items():
  print(k,v)

#importando o modulo JSON
import json

#convertendo o dicionario para um objeto
print(json.dumps(dict_guido))

#criando um arquivo JSON
with open('C:/Users/gabri/Desktop/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/dados.json','r') as arquivo:
  texto = arquivo.read()
  dados = json.loads(texto)
print(dados)
