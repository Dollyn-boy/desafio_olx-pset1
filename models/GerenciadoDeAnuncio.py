from abc import ABC, abstractmethod

class GerenciadoDeAnuncio:
    _instancia = None

    @classmethod
    def get_instance(GerenciadorDeAnuncio):
        if not GerenciadorDeAnuncio._instancia:
            GerenciadorDeAnuncio._instancia = GerenciadorDeAnuncio()
        return GerenciadorDeAnuncio._instancia
    
    def __init__(self):
        self.anuncios = []

    def adicionar_anuncio(self, anuncio):
        self.anuncios.append(anuncio)
    
    def pesquisar_anuncios(self, estrategia ,termo):
        return estrategia.buscar(self.anuncios, termo)
    
    def listar_anuncios(self):
        for anuncio in self.anuncios:
            if anuncio.is_disponivel():
                print(f"{anuncio.produto.nome} | R${anuncio.preco} | {anuncio.produto.tipo} | {anuncio.cidade} - {anuncio.uf} | {anuncio.data} ")
    


class EstrategiaBuscar(ABC):
    @abstractmethod
    def buscar(self, anuncios, termo):
        pass

class BuscarPorNome(EstrategiaBuscar):
    def buscar(self, anuncios, termo):
        return [anuncio for anuncio in anuncios if termo.lower() in anuncio.produto.nome.lower()]

class BuscarPorTipo(EstrategiaBuscar):
    def buscar(self, anuncios, termo):
        return [anuncio for anuncio in anuncios if termo.lower() in anuncio.produto.tipo.lower()]


