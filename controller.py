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
    else:
        Persistencia.get_instance().add_usuario(user)
        return user

def atualizar_estoque(produto, operacao):
    estoque = Estoque()
    estoque.atualizar_estoque(produto, operacao)

def criar_produto(usuario: Usuario, nome, descricao, tipo):
    produto = Produto(nome.lower(), descricao.lower(), tipo.lower())
    usuario._estado.cadastrar_produto(usuario, produto)


def criar_anuncio(vendedor:Usuario, cep: str, num_produto: int):
        endereco = Endereco(cep)
        gerenciador = GerenciadoDeAnuncio.get_instance()

        legenda = input("Inseir legenda do Anúncio: ")
        while True:
            try:
                preco = float(input("Definir Preço: "))
                break
            except ValueError:
                print("Valor Inválido")
        try:
            anuncio = Anuncio(vendedor.produtos[num_produto - 1], preco, legenda, endereco.cidade, endereco.uf, vendedor)
        except IndexError:
            print("Espaço de produto Vazio.")
        else:
            try:
                vendedor._estado.fazer_anuncio(vendedor, anuncio)
            except ValueError:
                print("Você não pode fazer um anúncio no estado de Comprador. Mude para o modo Vendedor.")
                pass
            else:       
                atualizar_estoque(vendedor.produtos[num_produto - 1], "adicionar")
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
    resultados = gerenciador.pesquisar_anuncios(estrategia_selecionada, termo_buscado)

    if not resultados:
        print("Nenhum resultado foi encontrado.")
    else:
        for resultado in resultados:
            print(f"{resultado.produto.nome} | R${resultado.preco} | {resultado.produto.tipo} | {resultado.cidade} - {resultado.uf} | {resultado.data} ")


def realizar_transacao(usuario: Usuario, anuncio:Anuncio):
    transador = Transacao()
    transador.realizar_transacao(usuario, anuncio)
    atualizar_estoque(anuncio.produto, "transacao")
    
def main():
    gerenciador = GerenciadoDeAnuncio.get_instance()
    estoque = Estoque.get_instance()
    user1 = criar_usuario("Vitor", "eu@gmail.com", "vithu", 1233123, "vulto")
    user2 = criar_usuario("Jao", "ele@gmail.com", "johnga", 7458997, "joghsu231")
    Persistencia.get_instance().list_usuarios()


    user1.mudar_estado()
    user2.mudar_estado()
    criar_produto(user2, "Night`s edge", "Lâmina da noite", "Arma")
    criar_anuncio(user1, "95555000", 1)
    criar_anuncio(user2, "95555000", 1)
    user1.carteira = 100000
    realizar_transacao(user1, user2.anuncios[0])
    user2.exibir_status()
    estoque.listar_estoque()
 

if __name__ =="__main__":
    main()    