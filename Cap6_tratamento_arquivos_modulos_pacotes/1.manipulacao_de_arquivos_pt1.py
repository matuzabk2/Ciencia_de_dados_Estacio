import os
#abrindo o arquivo para leitura
arquivo1 = open("/workspaces/Ciencia_de_dados_Estacio/Cap6_ tratamento_arquivos_modulos_pacotes/Arquivos/arquivo1.txt", "r")

#lendo o conteúdo do arquivo
#testando o clear pro terminal não ficar cheio de informação haha (fins didaticos)
os.system('clear')
print("\n")
#lendo arquivo
print(arquivo1.read())
print("\n")
#tipo do arquivo
print(type(arquivo1))
#contar o numero de caracteres do arquivo
print(arquivo1.tell())
#lendo arquivo
print(arquivo1.read())
#retornar para o inicio do arquivo
print(arquivo1.seek(0,0))
#lendo os primeiros 23 caracteres do arquivo
print("\n")
print(arquivo1.read(23))
print("\n")
#usando read pra ver q o "cursos" esta aonde parou q seria no final dos ultimos 23 caracteres
print(arquivo1.read())
