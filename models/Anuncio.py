import datetime

class Anuncio:
    id = 1
    def __init__(self, produto, legenda, cidade, uf, vendedor):
        self.produto = produto
        self.legenda = legenda
        self.cidade = cidade
        self.uf = uf
        self.vendedor = vendedor
        self.data = datetime.now()
        self.comentarios = []
        self.id = Anuncio.id
        Anuncio.id += 1
