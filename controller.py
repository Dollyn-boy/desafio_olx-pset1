from models.Anuncio import Anuncio
from models.Usuario import Usuario, EstadoComprador, EstadoVendedor
from models.Produto import Produto
from models.Endereco import Endereco
from models.Estoque import Estoque
from models.Transacao import Transacao
from models.GerenciadorDeUsuario import GerenciadoDeUsuario
from models.GerenciadoDeAnuncio import GerenciadoDeAnuncio, BuscarPorNome, BuscarPorTipo, BuscarTodos


ESTADO_COMPRADOR = EstadoComprador()
ESTADO_VENDEDOR = EstadoVendedor()

#Cria usuário com estado comprador pré-definido
def criar_usuario(nome, email, user, telefone, senha):
    user = Usuario(nome, email, user, telefone, senha, ESTADO_COMPRADOR)
    if not user:
        return "Usuário já existe."
    else:
        GerenciadoDeUsuario.get_instance().add_usuario(user)
        return user

def verificar_usuario(email, senha):
    usuarios = GerenciadoDeUsuario.get_instance().get_usuarios()
    if usuarios:
        for usuario in usuarios:
            if usuario.email == email or usuario.senha == senha:
                print("Login bem sucedido!")
                return usuario
    print("ERRO: Email e/ou senha inválidos")

def pegar_usuario():
    return GerenciadoDeUsuario.get_instance().get_usuarios()    

def atualizar_estoque(produto, operacao):
    estoque = Estoque()
    estoque.atualizar_estoque(produto, operacao)


def criar_produto(usuario: Usuario, nome, descricao, tipo):
    produto = Produto(nome.lower(), descricao.lower(), tipo.lower())
    usuario._estado.cadastrar_produto(usuario, produto)


def criar_anuncio(vendedor:Usuario, cep: str, num_produto: int, preco:float):
        gerenciador_anuncio = GerenciadoDeAnuncio.get_instance()

        try:    
            endereco = Endereco(cep)

        except ValueError:
            print("Cep Inválido")
            return

        try:

            anuncio = Anuncio(vendedor.produtos[num_produto - 1], preco, endereco.cidade, endereco.uf, vendedor)
        except IndexError:
            print("Espaço de produto Vazio.")
            return
        
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
    

def escolher_acao(usuario, anuncio_selecionado):
    escolha = input(" {1 -Comentar}      {2 -Comprar}       {sair}\n>>")
    if escolha == "1":
            print()
            fazer_comentario(usuario ,anuncio_selecionado)
    elif escolha == "2":
            print()
            realizar_transacao(usuario, anuncio_selecionado)
    else:
        print()
        print("Saindo...")
    


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
    pass

if __name__ =="__main__":
    main()    