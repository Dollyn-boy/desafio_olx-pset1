from datetime import datetime

class Anuncio:
    id = 1
    def __init__(self, produto, preco , cidade, uf, vendedor):
        self.produto = produto
        self.preco = preco
        self.cidade = cidade
        self.uf = uf
        self.vendedor = vendedor
        self.disponivel = True
        self.data = datetime.now()
        self.comentarios = []
        self.id = Anuncio.id
        Anuncio.id += 1

    def is_disponivel(self):
        return self.disponivel
    
    def vender(self):
        self.disponivel = False