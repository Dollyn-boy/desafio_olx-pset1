from models.Anuncio import Anuncio
from models.Usuario import Usuario
from models.Produto import Produto
from models.Endereco import Endereco
from models.Estoque import Estoque

def criar_usuario(nome, email, user, telefone, senha):
    user = Usuario(nome, email, user, telefone, senha)
    if not user:
        return "Usuário já existe."

def atualizar_estoque(produto):
    estoque = Estoque()
    estoque.produtos_disponiveis.append(produto)

def criar_produto(usuario: Usuario, nome, descricao, preco, tipo):
    produto = Produto(nome, descricao, preco, tipo)
    usuario.cadastrar_produto(produto)


def criar_anuncio(vendedor:Usuario, cep: str, num_produto: int):
    endereco = Endereco(cep)
    legenda = input("Inseir legenda do Anúncio: ")
    anuncio = Anuncio(vendedor.produtos[num_produto], legenda, endereco.cidade, endereco.uf, vendedor)
    vendedor.fazer_anuncio(anuncio)
    atualizar_estoque(vendedor.produtos[num_produto])

def realizar_transacao(Usuario: Usuario, anuncio:Anuncio):
    ...