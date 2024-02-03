import requests

class Usuario:
    def __init__(self, nome, email, user, telefone, senha):
        self.nome = nome
        self.user = user
        self.telefone = telefone
        self.email = email
        self.__senha = senha
        self.enderecos = []
    
    @property 
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
    
    def inserir_enderoco(self, cep):
        self.enderecos.append(Endereco(cep))
    
    def lista_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(f"{endereco.cidade}, {endereco.uf}")
class Endereco:
    def __init__(self, cep):
        #Armazena o valor do cep em um link e faz a requisição dele retornando uma resposta
        cep = cep.replace("-", "").replace(".", "")
        if len(cep) == 8:
            link = f"https://viacep.com.br/ws/{cep}/json/"
            requisicao = requests.get(link) 

            dict_requisicao = requisicao.json()

            self.cidade = dict_requisicao['localidade']
            self.uf = dict_requisicao['uf']
        else:
            print("Cep Inválido")