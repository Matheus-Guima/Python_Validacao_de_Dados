from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        
        if tipo_documento == 'cpf':
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!!") 
        elif(self.tipo_documento == 'cnpj'):
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!!")
        else:
            raise ValueError('Documento inválido')     
                      
    
    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('Quantidade de dígitos inválida!!') 
        
    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(cnpj)
        else:
            raise ValueError('Quantidade de dígitos invála!!')    
    
    def format_Cpf(self):
        mascara = CPF() 
        return mascara.mask(self.cpf)
        # fatia_um = self.cpf[:3]
        # fatia_dois= self.cpf[3:6]
        # fatia_tres = self.cpf[6:9]
        # fatia_quatro = self.cpf[9:] 
        # return(f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}')
    
    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)       
    
    def __str__(self) -> str:
        if self.tipo_documento == 'cpf':
            return self.format_Cpf()
        elif self.tipo_documento =='cnpj':
            return self.format_cnpj()