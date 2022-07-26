import re           

# #Teste
# padrao = '[0-9][a-z][0-9]'
# texto = '123 1a2 1cc aa1'
# resposta= re.search(padrao, texto)
# print(resposta.group())

# #Teste 2
# padrao = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}' 
# #padrao2 = '\w{5,50}@[a-z]{3,10}.com.br' 
# email = 'jorge123@gmail.com.br'
# resposta = re.search(padrao, email)
# print(resposta.group())

padrao_molde = '(xx)aaaaa-wwww'
padrao = '[0-9]{2}[0-9]{4,5}[-]?[0-9]{4}'
texto = ' Eu gosto do número 212467-6676'
resposta = re.findall(padrao, texto)
print(resposta)