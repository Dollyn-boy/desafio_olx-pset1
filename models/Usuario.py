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

class Endereco:
    def __init__(self, cep):
        self.cep