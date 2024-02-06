from Endereco import Endereco
from Persistencia import Persistencia
class Usuario:
    def __init__(self, nome, email, user, telefone, senha):
        self.nome = nome
        if user in Persistencia.get_instance.get_usuarios:
            return False
        self.user = user
        self.telefone = telefone
        self.email = email
        self.__senha = senha
        self.enderecos = []
        self.estado = None
    
    @property 
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
    
    def mudar_estado(self):
        pass
class EstadoDoUser:
        def switch(self, user):
            ...

class EstadoComprador:
     def switch(self, user):
          user.estado = EstadoVendedor()

class EstadoVendedor:
     def switch(self, user):
          user.estado = EstadoComprador()
          