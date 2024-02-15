
from .GerenciadorDeUsuario import GerenciadoDeUsuario

class Usuario:
    def __init__(self, nome, email, user, telefone, senha, estado):
        self.nome = nome
        if user in GerenciadoDeUsuario.get_instance().get_usuarios():
            raise ValueError("User já existe")
        self.user = user
        self.telefone = telefone
        self._carteira = 0
        self.email = email
        self._senha = senha
        self._estado = estado
        self.produtos = []
        self.anuncios = []

    @property 
    def senha(self):
        return self._senha


    @property 
    def carteira(self):
        return self._carteira
    
    @carteira.setter
    def carteira(self, novo_valor: int):
        self._carteira = novo_valor

    def exibir_status(self):
        print("="*25)
        print(f"{self.nome} | R${self.carteira} | R$ {self._estado.nome} \n\nProdutos :")
        self.listar_produtos()
        print("="*25)
    
    def mudar_estado(self, novo_estado):
        self._estado = novo_estado
        print(f"Estado {novo_estado.nome} ativado")

    def listar_produtos(self):
        if not self.produtos:
            print("Vazio!")
        else:
            for produto in self.produtos:
                contador = 1
                print(f"{contador}- {produto.nome} | {produto.descricao} | {produto.tipo}")
                contador+=1
                

class EstadoDoUser:
        nome = ""

class EstadoComprador(EstadoDoUser):
    nome = "Comprador"

    def cadastrar_produto(self, user, produto):
        user.produtos.append(produto)

    def fazer_anuncio(self, user, produto):
        raise ValueError("Você não pode fazer um anúncio no estado de Comprador. Mude para o modo Vendedor.")

    def comentar_anuncio(self, anuncio, comentario):
        anuncio.comentarios.append(comentario)



class EstadoVendedor(EstadoDoUser):
    nome = "Vendedor"

    def cadastrar_produto(self, user, produto):
        user.produtos.append(produto)

    def fazer_anuncio(self, user, anuncio):
        user.anuncios.append(anuncio)

    def comentar_anuncio(self, anuncio, comentario):
        raise ValueError("Você não pode comentar um anúncio no estado de Vededor. Mude para o modo Comprador")

