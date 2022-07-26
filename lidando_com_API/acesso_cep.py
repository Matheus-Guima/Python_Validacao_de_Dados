import requests

class BuscaEndereco:
    
    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.cep_e_Valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP Inválido!!') 
        
    def __str__(self) -> str:
        return self.format_cep()       
            
    
    def cep_e_Valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False 
        
    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
    
    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )