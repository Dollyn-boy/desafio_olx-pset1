import pycep_correios

class Usuario:
    def __init__(self, nome, email, user, telefone, senha):
        self.nome = nome
        self.user = user
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.enderecos = []
    
    def inserir_enderoco(self, cep):
        self.enderecos.append(Endereco(cep))
    
    def lista_enderecos(self):
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