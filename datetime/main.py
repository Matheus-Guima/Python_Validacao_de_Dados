from datetime import date, datetime, timedelta
from datas_br import DatasBr

#TEM DUAS CLASSES LEGAIS  
#dattetime.datetime - Retorna uma hora 
#Exemplo:
# print(datetime.today())

# cadastro = DatasBr()
# print(cadastro)

# hoje = datetime.today()
# hoje_formatado = hoje.strftime('%d/%m/%Y %H:%M') #Vira String
# print(hoje_formatado)

#TIMEDELTA
# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1, hours=20) #Faz esse tipo de soma 

# print(amanha - hoje)
 
hoje = DatasBr()
print(hoje.tempo_cadastro())

