from factory import Doc


#Aqui a gente vai testar todo a logica nates de colocar na classe
#Dps vamos teestar a classe dentro do main

#PROCURAR SIMPRE EM PYPI (PYTHON PACKEKGE INDEX)
 
#PRIMEIRO PASSO
# cpf = str(cpf)
# tamanho_cpf = len(cpf) #Int não tem len
# print(tamanho_cpf)

#SEGUNDO PASSO
# fatia_um = cpf[:3]
# fatia_dois= cpf[3:6]
# fatia_tres = cpf[6:9]
# fatia_quatro = cpf[9:]
# cpf_formatado =f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'
# print(cpf_formatado)

#cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))

# objeto_cpf = Cpf(cpf)
# print(objeto_c

cnpj = 35379838000112
cpf = 15316264754 

objeto_cpf = Doc.cria_documento(cpf)
print(objeto_cpf)

objeto_cnpj = Doc.cria_documento(cnpj)
print(objeto_cnpj)