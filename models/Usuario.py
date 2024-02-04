from Enderecos import Endereco
from Produto import Produto
from abc import ABC, abstractmethod


class ComportamentoDoUsuario(ABC):

    def __init__(self, usuario):
        self.usuario = usuario

    #Interface diferenciada pela quantidade de métodos passados(cortesia do chat gpt)
    @abstractmethod
    def executar(self, *args, **kwargs):
        pass


class ComportamentoVendedor(ComportamentoDoUsuario):
    def __init__(self, usuario):
        super().__init__(usuario)

    def executar(self, nome, descricao, preco, tipo, index_endereco):
        index_endereco-=1
        endereco = self.usuario.escolher_endereco(index_endereco)
        produto = Produto(nome, descricao, preco, self.usuario.user, tipo, endereco)
        self.usuario.produtos_cadastrados.append(produto)
        print("Deu Bom")
class ComportamentoComprador(ComportamentoDoUsuario):
    #Implementa interface para "comentar_produto"
    def __init__(self, usuario):
        super().__init__(usuario)

    def executar(self ,produto):
        comentario = input("Comentar: ")
        produto.comentarios.append(comentario)
        
        
class Usuario:
    def __init__(self, nome, email, user, telefone, senha):
        self.nome = nome
        self.user = user
        self.telefone = telefone
        self.email = email
        self.__senha = senha
        self.enderecos = []
        self.produtos_cadastrados = []  
        self.comportamento = None
    
    @property 
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
    
    #Método que instancia um ou + endereços pro usuário 
    def inserir_endereco(self, cep):
        self.enderecos.append(Endereco(cep))
    
    def lista_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(f"{endereco.cidade}, {endereco.uf}")
    
    def escolher_endereco(self, index):
        return self.enderecos[index]

    def modo_vendedor(self):
            self.comportamento = ComportamentoVendedor(self)

    def executar_comportamento(self, *args, **kwargs):
        self.comportamento.executar(*args, **kwargs)
