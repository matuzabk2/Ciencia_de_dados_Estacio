#abrindo arquivo para gravação
arquivo2 = open("/workspaces/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/arquivo2.txt", "w")

#como abrimos o arquivo apenas para gravação, nao podemos usar comando de leitura
print(arquivo2.read())

#gravando arquivo
arquivo2.write("Aprendendo a programar em Python!")
arquivo2.close()

#lendo arquivo gravado
arquivo2 = open("/workspaces/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/arquivo2.txt", "r")
print(arquivo2.read())

#acrescetando conteudo
arquivo2 = open("/workspaces/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/arquivo2.txt", "a")
arquivo2.write(" E a metodologia de ensino da data science academy facilita o aprendizado!.")
arquivo2.close()

#
