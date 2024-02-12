
from Persistencia import Persistencia
class Usuario:
    def __init__(self, nome, email, user, telefone, senha):
        self.nome = nome
        if user in Persistencia.get_instance().get_usuarios():
            raise ValueError("User já existe")
        self.user = user
        self.telefone = telefone
        self._carteira = 100
        self.email = email
        self.__senha = senha
        self._estado = EstadoComprador()
        self.produtos = []
        self.anuncios = []

    @property 
    def carteira(self):
        return self._carteira
    
    @carteira.setter
    def carteira(self, novo_valor):
        self._carteira = novo_valor
    
    def mudar_estado(self):
        self.estado.switch(self)

    def listar_produtos(self):
        for produto in self.produtos:
            contador = 1
            print(f"{contador}-{produto.nome}|{produto.descricao}|{produto.tipo}")
            conrador+=1
            

class EstadoDoUser:
        def switch(self, user):
            ...

class EstadoComprador(EstadoDoUser):
    def switch(self, user):
        user._estado = EstadoVendedor()
        print("Modo Vendedor Ativado")

    def cadastrar_produto(self, user, produto):
        user.produtos.append(produto)

    def fazer_anuncio(self, user, produto):
        print("Você não pode fazer um anúncio no estado de Comprador. Mude para o modo Vendedor.")


class EstadoVendedor(EstadoDoUser):
     
    def switch(self, user):
        user._estado = EstadoComprador()
        print("Modo Comprador Ativado")

    def cadastrar_produto(self, user, produto):
        user.produtos.append(produto)

    def fazer_anuncio(self, user, anuncio):
        user.anuncios.append(anuncio)

