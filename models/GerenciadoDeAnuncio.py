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
    

    def mostrar_comentarios(self, anuncio):
        for comentario in anuncio.comentarios:
            print(comentario)
        

    def mostrar_resultado(self, resultados):
        if not resultados:
            print("Nenhum resultado foi encontrado.")
        else:
            for resultado in resultados:
                print(f"> {resultado.produto.nome.title()} | R${resultado.preco} | {resultado.produto.tipo} | {resultado.vendedor.nome} | {resultado.cidade} - {resultado.uf} | {resultado.data} ")
                self.mostrar_comentarios(resultado)
    

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

class BuscarTodos(EstrategiaBuscar):
    def buscar(self, anuncios, termo):
        return [anuncio for anuncio in anuncios]

