#trabalhando com dicionarios
#isso é uma lista
estudantes_lst = {"pedro", 24, "ana", 22, "ronaldo", 26, "janaina", 25}
print(type(estudantes_lst))

#isso é um dicionario
estudantes_dict = {"pedro":24, "ana":22, "ronaldo":26, "janaina":25}
print(type(estudantes_dict))
print(estudantes_dict["pedro"])
estudantes_dict["marcelo"] = 23
print(estudantes_dict)
#del estudantes_dict
#print(estudantes_dict)

estudantes = {"pedro":24, "ana":22, "ronaldo":26, "janaina":25}
print(estudantes)
print(len(estudantes))

estudantes.keys()

estudantes.values()

estudantes.items()

estudantes2 = {"camila":27, "adriana":28, "roberta":26}
print(estudantes2)
estudantes.update(estudantes2)

dic1 = {}
dic1["chave_um"] = 2
print(dic1)
dic1[10] = 5
print(dic1)
dic1[9,13] = "python"
print(dic1)
dic1["teste"] = 5
print(dic1)
dict1 = {}
print(dict1)

dict2 = {}
dict2["key1"] = "data science"
dict2["key2"] = 10
dict2["key3"] = 100
print(dict2)

a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]
print(a,b,c)

#dicionario de listas
dict3 = {'chavel':1230, 'chave2':[22,453,73.4],'chave3':['picanha','fraldinha','alcatra']}
print(dict3)
print(dict3['chave2'])

#acessando um item da lista, dentro do dicionario
print(dict3['chave3'][0].upper())

#operaçoes com itens da lista, dentro do dicionario
var1 = dict3['chave2'][0] - 2
print(var1)

#duas operaçoes no mesmo comando, para atualizar um iten dentro da lista
dict3['chave2'][0] -= 2
print(dict3)

#criando dicionarios aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'dict aninhado em python'}}}
print(dict_aninhado)
dict_aninhado['key1']['key2_aninhada']['key3_aninhada']
