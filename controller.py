from models.Anuncio import Anuncio
from models.Usuario import Usuario
from models.Produto import Produto
from models.Endereco import Endereco
from models.Estoque import Estoque
from models.Transacao import Transacao
from models.Persistencia import Persistencia
from models.GerenciadoDeAnuncio import GerenciadoDeAnuncio, BuscarPorNome, BuscarPorTipo

def criar_usuario(nome, email, user, telefone, senha):
    user = Usuario(nome, email, user, telefone, senha)
    if not user:
        return "Usuário já existe."

def atualizar_estoque(produto, operacao):
    estoque = Estoque()
    estoque.atualizar_estoque(produto, operacao)

def criar_produto(usuario: Usuario, nome, descricao, tipo):
    produto = Produto(nome.lower(), descricao.lower(), tipo.lower())
    usuario.cadastrar_produto(produto)


def criar_anuncio(vendedor:Usuario, cep: str, num_produto: int):
    endereco = Endereco(cep)
    gerenciador = GerenciadoDeAnuncio.get_instance()

    legenda = input("Inseir legenda do Anúncio: ")
    try:
        preco = int(input("Definir Preço: "))
    except ValueError:
        print("Valor Inválido")
    
    anuncio = Anuncio(vendedor.produtos[num_produto + 1], preco, legenda, endereco.cidade, endereco.uf, vendedor)

    vendedor.fazer_anuncio(anuncio)
    atualizar_estoque(vendedor.produtos[num_produto], "adicionar")
    gerenciador.adicionar_anuncio(anuncio)

def pesquisar_anuncios(estrategia, termo_buscado):
    estrategias = {
        'nome': BuscarPorNome(),
        'tipo': BuscarPorTipo(),
    }

    estrategia_lower = estrategia.lower()
    
    if estrategia_lower in estrategias:
        estrategia_selecionada = estrategias[estrategia_lower]
    else:
        # Se a estratégia fornecida não estiver no mapeamento, você pode definir uma estratégia padrão ou lançar uma exceção.
        estrategia_selecionada = estrategias['nome']

    gerenciador = GerenciadoDeAnuncio.get_instance()
    resultado_pesquisa = gerenciador.pesquisar_anuncios(estrategia_selecionada, termo_buscado)

    return resultado_pesquisa


def realizar_transacao(usuario: Usuario, anuncio:Anuncio):
    transador = Transacao()
    transador.realizar_transacao(usuario, anuncio)
    atualizar_estoque(anuncio.produto, "transacao")
    
def main():
    print("aoba")
    criar_usuario("Vitor", "eu@gmail.com", "vithu", 1233123, "vulto")
    print(Persistencia.get_instance().get_usuarios())

    pass

if __name__ =="__main__":
    main()    