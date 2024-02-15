from controller import *
from pyfiglet import Figlet
  

# Exemplo de uso

def printar_sessao_cadastro():
    print()
    print("Sessão de Cadastro")
    print("-"*40)
    user = input("Digite seu nome de usuário: ").strip()
    email = input("Digite seu email: ").strip()
    senha = input("Digite sua senha: ").strip()
    nome = input("Digite seu Nome: ").strip()
    telefone = input("Digite seu Telefone: ").strip()
    print("Cadastro bem sucedido")
    return criar_usuario(nome, email, user, telefone, senha)

def printar_sessao_login():  
    print()
    print("Sessão de Login")
    print("-"*40)
    email = input("Digite seu email: ").strip()
    senha = input("Digite sua senha: ").strip()
    user_logado =  verificar_usuario(email,senha)
    if not user_logado:
         printar_sessao_login()
    return user_logado

def acessar_homepage(user):
     fig = Figlet(font="slant")
     logo = fig.renderText(" Olx 2 Home ")
     print()
     print(logo)
     print("Seja Bem Vindo!!!")
     print()
     print("{1 - Pesquisar}        {2 - Perfil}         {3 - Produtos}")
     escolha = input(">>")
     if escolha == "1":
          pesquisar(user)
     elif escolha == "2":
          mostrar_perfil(user)
     else:
          manipular_produtos(user)

def pesquisar(user):
    print("\n Filtros:  {Nome}  {Tipo}  {Todos}")
    estrategia = input(">>").strip().lower()
    if estrategia not in ["nome", "tipo", "todos"]:
        print("Filtro Inválido")
        acessar_homepage(user)
    termo = "Pesquisar: "
    resultados = pesquisar_anuncios(estrategia, termo)
    if resultados:
        anuncio_selecionado = selecionar_anuncio(resultados)
        escolher_acao(anuncio_selecionado, user)

def mostrar_perfil(user):
    user.exibir_status()
    print("Deseja mudar de estado? [y/n] ")
    resposta = input(">>").strip().lower()
    if resposta == "y":
        if user._estado == ESTADO_COMPRADOR:
            user.mudar_estado(ESTADO_VENDEDOR)
        else:
            user.mudar_estado(ESTADO_COMPRADOR)

def manipular_produtos(user):
    print("Produtos: ")
    user.listar_produtos()
    print("     {1 - Adicionar Produtos}   {2 - Criar Anuncio}")
    escolha = input(">>").strip().lower()
    if escolha == "1":
        nome = input("Nome do Produto: ")
        descricao = input("Descricao do Produto: ")
        tipo = input("Tipo do Produto: ")
        criar_produto(user, nome, descricao, tipo)
        print("Produto criado com sucesso!!")
    elif escolha == "2":
        while True:
            try:
                num_produto = int(input("Selecione o número correspondete ao produto desejado: "))
                cep = input("Inserir CEP: ")
                break
            except ValueError:
                print("Valores Inválidos")
        criar_anuncio(user, cep ,num_produto)
 
def main():
    
    criar_usuario("Vitor", "vitor@gmail.com", "vithu", "9999999", "aipim")
    criar_usuario("Pedro", "pedro@gmail.com", "rujinho", "9234565", "arveis")
    criar_usuario("John", "johzi@gmail.com", "jaum", "8124590", "imas")


    fig = Figlet(font="slant")
    logo = fig.renderText("   Olx 2   ")

    print(logo)
    print("[1 - Cadastrar]          [2 - Fazer Login] \n")
    resposta = input(">>").strip()
    if resposta == "1":
        novo_user = printar_sessao_cadastro()
        while True:
            acessar_homepage(novo_user)
    else:
        user_logado = printar_sessao_login()
        while True:
            acessar_homepage(user_logado)

        


if __name__ == "__main__":
    main()