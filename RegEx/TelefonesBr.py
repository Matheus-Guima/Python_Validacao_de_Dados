import re

class TelefonesBr:
    def __init__(self, telefone) -> None:
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Numero de telefone inválido!')
        
    def __str__(self) -> str:
        return self.format_numero()    
    
    def valida_telefone(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, telefone) #Retorna uma lista, se a lista estiver cheia vai ser true se não, false 
        if resposta:
            return True
        else:
            False
            
    def format_numero(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        if resposta.group(1) == None:
            return f'({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'    
        return f'+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'
                