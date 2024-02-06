import datetime

class Anuncio:
    id = 1
    def __init__(self, produto, legenda, local, user):
        self.produto = produto
        self.legenda = legenda
        self.local = local
        self.user = user
        self.data = datetime.now()
        self.id = Anuncio.id
        Anuncio.id += 1