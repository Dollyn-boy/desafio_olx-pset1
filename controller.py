from models.Anuncio import Anuncio
from models.Usuario import Usuario, EstadoComprador, EstadoVendedor
from models.Produto import Produto
from models.Endereco import Endereco
from models.Estoque import Estoque
from models.Transacao import Transacao
from models.GerenciadorDeUsuario import GerenciadoDeUsuario
from models.GerenciadoDeAnuncio import GerenciadoDeAnuncio, BuscarPorNome, BuscarPorTipo, BuscarTodos

#Cria usuário com estado comprador pré-definido
def criar_usuario(nome, email, user, telefone, senha):
    user = Usuario(nome, email, user, telefone, senha, EstadoComprador())
    if not user:
        return "Usuário já existe."
    else:
        GerenciadoDeUsuario.get_instance().add_usuario(user)
        return user


def atualizar_estoque(produto, operacao):
    estoque = Estoque()
    estoque.atualizar_estoque(produto, operacao)


def criar_produto(usuario: Usuario, nome, descricao, tipo):
    produto = Produto(nome.lower(), descricao.lower(), tipo.lower())
    usuario._estado.cadastrar_produto(usuario, produto)


def criar_anuncio(vendedor:Usuario, cep: str, num_produto: int):
        endereco = Endereco(cep)
        gerenciador_anuncio = GerenciadoDeAnuncio.get_instance()

        while True:
            try:
                preco = float(input("Definir Preço: "))
                break
            except ValueError:
                print("Valor Inválido")

        try:
            anuncio = Anuncio(vendedor.produtos[num_produto - 1], preco, endereco.cidade, endereco.uf, vendedor)
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
                gerenciador_anuncio.adicionar_anuncio(anuncio)


def pesquisar_anuncios(estrategia, termo_buscado):
    estrategias = {
        'todo': BuscarTodos(),
        'nome': BuscarPorNome(),
        'tipo': BuscarPorTipo(),
    }

    estrategia_lower = estrategia.lower()
    
    if estrategia_lower in estrategias:
        estrategia_selecionada = estrategias[estrategia_lower]
    else:
        estrategia_selecionada = estrategias['nome']

    gerenciador_anuncio = GerenciadoDeAnuncio.get_instance()
    resultados = gerenciador_anuncio.pesquisar_anuncios(estrategia_selecionada, termo_buscado)
    gerenciador_anuncio.mostrar_resultado(resultados)

    return resultados

def selecionar_anuncio(resultados):
    while True:
        try:
            index = int(input("Selecione o anúncio: "))
            return resultados[index - 1]
        except (ValueError, IndexError, EOFError):
            print("Valor Inválido")

def fazer_comentario(usuario: Usuario, anuncio: Anuncio):
    comentario = input("Digite Aqui: ")
    try:
        usuario._estado.comentar_anuncio(anuncio, comentario)
    except ValueError:
        print("Você não pode comentar um anúncio no estado de Vededor. Mude para o modo Comprador")

def realizar_transacao(usuario: Usuario, anuncio:Anuncio):
    transador = Transacao()
    transador.realizar_transacao(usuario, anuncio)
    atualizar_estoque(anuncio.produto, "transacao")

    
def main():
    gerenciador_anuncio = GerenciadoDeAnuncio.get_instance()
    gerenciador_usuario = GerenciadoDeUsuario.get_instance()
    estoque = Estoque.get_instance()

    user1 = criar_usuario("Vitor", "eu@gmail.com", "vithu", 1233123, "vulto")
    user2 = criar_usuario("Jao", "ele@gmail.com", "johnga", 7458997, "joghsu231")

    user1.mudar_estado(EstadoVendedor())
    user2.mudar_estado(EstadoComprador())

    user2.carteira = 100000000

    criar_produto(user1, "Espada de Grama", "Item Almadiçoado", "Arma")
    criar_produto(user1, "Buraco Negro em minuatura", "-NÃO SE APROXIME-", "Corpo Celeste")
    criar_produto(user1, "Espada Grande do Luar", "Espada mágica", "Arma")
    criar_anuncio(user1, "44640000", 1)
    criar_anuncio(user1, "44640000", 2)
    criar_anuncio(user1, "44640000", 3)

    resultados = pesquisar_anuncios("todo", "arma")
    if resultados:
        anuncio_selecionado = selecionar_anuncio(resultados)
        escolha = input(" {1 -Comentar}      {2 -Comprar} \n>>")
        if escolha == "1":
            print()
            fazer_comentario(user2 ,anuncio_selecionado)
        else:
            print()
            realizar_transacao(user2, anuncio_selecionado)
    
    resultados = pesquisar_anuncios("todo", "arma")
 

if __name__ =="__main__":
    main()    