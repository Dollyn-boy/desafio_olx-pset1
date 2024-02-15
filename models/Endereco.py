import requests

class Endereco:
    def __init__(self, cep):
        cep = cep.replace("-", "").replace(".", "")
        if len(cep) == 8:
            link = f"https://viacep.com.br/ws/{cep}/json/"
            requisicao = requests.get(link) 

            dict_requisicao = requisicao.json()

            self.cidade = dict_requisicao['localidade']
            self.uf = dict_requisicao['uf']
        else:
            raise ValueError
            
