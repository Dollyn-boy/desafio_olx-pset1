class Estoque:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Estoque, cls).__new__(cls)
            # Inicialize quaisquer outros atributos necessários aqui
            cls._instancia.produtos_disponiveis = []
            cls._instancia.produtos_vendidos = []
        return cls._instancia
    
    def adicionar_produto(self, produto):
        if produto in self.produtos_disponiveis:
            produto.quantidade+=1
        else:
            self.produtos_disponiveis.append(produto)
            produto.quantidade+=1
    
    def remover_produto(self, produto):
        if produto in self.produtos_disponiveis:
            produto.quantidade-=1
        else:
            self.produtos_vendidos.append(produto)
            self.produtos_disponiveis.remove(produto)

    def listar_estoque(self):
        print("Disponíveis")
        for produto in self.produtos_disponiveis:
            print(produto.nome + " - " + str(produto.quantidade))
        print("-------------")
        print("Vendidos")
        for produto in self.produtos_vendidos:
            print(produto.nome + " - " + str(produto.quantidade))