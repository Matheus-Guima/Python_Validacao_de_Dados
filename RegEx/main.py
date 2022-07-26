from TelefonesBr import TelefonesBr
import re

telefone = "2124676676"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

#padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([-])?([0-9]{4})'
#resposta = re.search(padrao, telefone)
#print(resposta.group())