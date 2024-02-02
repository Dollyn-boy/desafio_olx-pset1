import pycep_correios

class Usuario:
    def __init__(self, nome, email, user, telefone, senha):
        self.nome = nome
        self.user = user
        self.telefone = telefone
        self.email = email
        self.__senha = senha
        self.enderecos = []
    
    @property 
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
    
    def inserir_enderoco(self, cep):
        self.enderecos.append(Endereco(cep))
    
    def lista_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(f"{endereco.cidade}, {endereco.uf}, {endereco.bairro}")

class Endereco:
    def __init__(self, cep):
        try:
            endereco = pycep_correios.consultar_cep(cep)
            self.cidade = endereco['cidade']
            self.uf = endereco['uf']
            self.bairro = endereco['bairro']
        except pycep_correios.CEPInvalido as exc:
            print(exc) 