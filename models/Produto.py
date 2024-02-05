from Estoque import Estoque
class Produto:
    def __init__(self, nome, descricao ,preco, id_vendedor, tipo, cidade_estado):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.id_vendedor = id_vendedor
        self.tipo = tipo
        self.cidade_estado = cidade_estado
        self.comentarios = []
        self.quantidade = 1
    
    def atualizar_estoque(self):
        estoque = Estoque()
        estoque.adicionar_produto(self)