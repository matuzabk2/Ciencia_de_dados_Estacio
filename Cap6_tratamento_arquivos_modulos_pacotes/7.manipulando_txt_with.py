#importando o modulo csv
import csv 
with open('C:/Users/gabri/Desktop/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/numeros.csv', 'w') as arquivo:
  writer = csv.writer(arquivo)
  writer.writerow(('nota1', 'nota2', 'nota3'))
  writer.writerow((63,87,92))
  writer.writerow((61,79,76))
  writer.writerow((72,64,91))

#leitura de arquivos csv
with open('C:/Users/gabri/Desktop/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/numeros.csv', 'r', encoding='utf8', newline = '\r\n') as arquivo:
  #cria o objeto de leitura
  leitor = csv.reader(arquivo)
  #loop
  for x in leitor:
    print(x)

#gerando uma lista com dados do arquivo csv
with open('C:/Users/gabri/Desktop/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/numeros.csv', 'r') as arquivo:
  leitor = csv.reader(arquivo)
  dados = list(leitor)
print(dados)

#imprimindo a partir da segunda linha
print("aqui começa")
for linha in dados[1:]:
  print(linha)
