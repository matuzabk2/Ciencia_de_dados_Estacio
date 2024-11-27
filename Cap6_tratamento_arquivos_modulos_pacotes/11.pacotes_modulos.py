#importando um pacote python
import numpy
#verificando todos os metodos e atributos disponiveis no pacote
dir(numpy)
#usando um dos metodos do pacote numpy
numpy.sqrt(25)
#importando apenas um dos metodos do pacote numpy
from numpy import sqrt
#usando o metodo
sqrt(9)
#imprimindo todos os metodos do pacote math
print(dir(numpy))
#help do metodo sqrt do pacote numpy
help(sqrt)
import random
random.choice(['abacate', 'banana', 'laranja'])
random.sample(range(100), 10)
import statistics
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(dados)
statistics.median(dados)
import os
os.getcwd()
print(dir(os))

#importando o modulo request do pacote urllib, usado para trazer urls
#para dentro do nosso ambiente python
import urllib.request

#variavel resposta armazena o objeto da conezao a url passada como
#parametro
resposta = urllib.request.urlopen('http://python.org')
#objeto resposta
print(resposta)

#chamando o metodo read() do objeto resposta e armazenando o codigo
#html na variavel html
html = resposta.read()
#imprimindo html
print(html)

