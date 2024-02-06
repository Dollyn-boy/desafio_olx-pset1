
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
        self.estado = EstadoComprador()
        self.produtos = []
        self.anuncios = []

    @property 
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
    
    def mudar_estado(self):
        self.estate.switch(self)

class EstadoDoUser:
        def switch(self, user):
            ...

class EstadoComprador:
    def switch(self, user):
        user.estado = EstadoVendedor()
        print("Modo Vendedor Ativado")

    def cadastrar_produto(self, user, produto):
        user.produtos.append(produto)

    def fazer_anuncio(self, user, produto):
        print("Você não pode fazer um anúncio no estado de Comprador. Mude para o modo Vendedor.")


class EstadoVendedor:
     
    def switch(self, user):
        user.estado = EstadoComprador()
        print("Modo Comprador Ativado")

    def cadastrar_produto(self, user, produto):
        user.produtos.append(produto)

    def fazer_anuncio(self, user, anuncio):
        user.anuncios.append(anuncio)
