import pandas as pd
arquivo = open("C:/Users/gabri/Desktop/Ciencia_de_dados_Estacio/Cap6_tratamento_arquivos_modulos_pacotes/Arquivos/salarios.csv")
print(pd.__version__)

#criando um data frame com pandas
df = pd.read_csv(arquivo)
print(df.head())
df['Position Title'].value_counts()
