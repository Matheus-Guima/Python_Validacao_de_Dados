import requests
from acesso_cep import BuscaEndereco

cep = '01001000' 
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r) #Resposta 200 é bom, foi e voltou
#print(r.text) #Recebendo uma string

# a = objeto_cep.acessa_via_cep()
# print(a.text) #Retorna String
# print(a.json()) #O método retorna um dicionário, maias fácil de trabalhar 
# print(dir(a)) # Mostra todos os métodos que tem na classe

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)