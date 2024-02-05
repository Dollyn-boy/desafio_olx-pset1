import requests

class Endereco:
    def __init__(self, cep):
        #Armazena o valor do cep em um link e faz a requisição dele retornando uma resposta
        cep = cep.replace("-", "").replace(".", "")
        if len(cep) == 8:
            link = f"https://viacep.com.br/ws/{cep}/json/"
            requisicao = requests.get(link) 

            #requisicao retorna um dicionario com as informações do CEP
            dict_requisicao = requisicao.json()

            self.cidade = dict_requisicao['localidade']
            self.uf = dict_requisicao['uf']
        else:
            print("Cep Inválido")