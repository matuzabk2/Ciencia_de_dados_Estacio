#variavel global
var_global = 10 #esta é, uma variavel global
#função nao recomendada
def multiplica_numeros(num1, num2):
  var_global = num1 * num2 #esta é uma variavel local, mas usei a global pra ver o problema na usuabilidade
  print(var_global)
multiplica_numeros(5,25)
print(var_global) #esta imprime 10 pois a variavel global não foi alterada fora da funçao
