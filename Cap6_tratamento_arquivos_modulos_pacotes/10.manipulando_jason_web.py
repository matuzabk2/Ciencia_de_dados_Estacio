#imprimindo um arquivo json copiado da internet
import json
from urllib.request import urlopen
responde = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(responde)[0]
print(dados)

print('Título: ', dados['title'])
print('URL: ', dados['url'])
print('Duração: ', dados['duration'])
print('Número de Visualizações: ', dados['stats_number_of_plays'])

