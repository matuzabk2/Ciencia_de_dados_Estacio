texto = "Cientista de dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em python.\n"
texto += "E, claro, devem ser proeficiente em data science.\n"

#importando o modulo os
import os

#criando um arquivo
arquivo = open(os.path.join('C:/Users/gabri/Desktop/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/cientista.txt'), 'w')

#gravando os dados no arquivo
for palavra in texto.split():
  arquivo.write(palavra + ' ')

#fechando o arquivo
arquivo.close()

#lendo o arquivo
arquivo = open('C:/Users/gabri/Desktop/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

