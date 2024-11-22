#abrindo arquivo csv e lendo os dados
f = open("/workspaces/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/salarios.csv", "r")
data = f.read()
rows = data.split("\n")
#print(rows)

#dividindo um arquivo em colunas
f = open("/workspaces/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/salarios.csv", 'r')
data = f.read()
rows = data.split("\n")
full_data = []
for row in rows:
  split_row = row.split(",")
  full_data.append(split_row)
print(full_data)
