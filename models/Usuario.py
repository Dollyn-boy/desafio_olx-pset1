from Enderecos import Endereco
from Produto import Produto
from abc import ABC, abstractmethod

class ComportamentoDoUsuario:
    @abstractmethod
    def executar(self, usuario):
        pass

class ComportamenVendedor(ComportamentoDoUsuario):
    def executar(self, usuario):
        usuario.produtos_cadastrados = [] 

class Comp
        
class Usuario:
    def __init__(self, nome, email, user, telefone, senha, comportamento):
        self.nome = nome
        self.user = user
        self.telefone = telefone
        self.email = email
        self.__senha = senha
        self.enderecos = []
        self.comportamento = comportamento
    
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
            print(f"{endereco.cidade}, {endereco.uf}")
    
    def escolher_endereco(self, index):
        return self.enderecos[index]

    def executar_comportamento(self):
        self.comportamento.executar(self)
        
class Vendedor(Usuario):
    def __init__(self, nome, email, user, telefone, senha):
        super().__init__(nome, email, user, telefone, senha)
        self.produtos_cadastrados = []
    
    def cadastrar_produtos(self, nome, descricao, preco, tipo, index_endereco):
        usuario = super().user
        enderecos = super().enderecos
        self.produtos_cadastrados.append(Produto(nome, descricao, preco, usuario, tipo, enderecos(index_endereco)))        