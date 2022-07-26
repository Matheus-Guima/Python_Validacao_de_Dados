#Factory Fica responsável por chamar a classe certa 

from validate_docbr import CPF, CNPJ

#Factory
class Doc:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida!!')

class DocCpf:
    def __init__(self, documento) -> None:
        documento = str(documento)
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')
    
    def __str__(self) -> str:
        return self.formata()        
    
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento) 
    
    def formata(self):
        mascara = CPF() 
        return mascara.mask(self.cpf) 
    
    
class DocCnpj:
    def __init__(self, documento) -> None:
        documento = str(documento)
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')
    
    def __str__(self) -> str:
        return self.formata()        
        
    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)            

