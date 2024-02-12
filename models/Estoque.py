class Estoque:
    _instancia = None

    @staticmethod
    def get_instance():
        if not Estoque._instancia:
            Estoque._instancia = Estoque()
        return Estoque._instancia

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Estoque, cls).__new__(cls)
            # Inicialize quaisquer outros atributos necessários aqui
            cls._instancia.produtos_disponiveis = []
            cls._instancia.produtos_vendidos = []
        return cls._instancia
    
    def atualizar_estoque(self, produto, operacao):
        if operacao == "adicionar":
            self.produtos_disponiveis.append(produto)
        else:
            try:
                self.produtos_disponiveis.remove(produto)
                self.produtos_vendidos.append(produto)
            except IndexError:
                print("Produto indisponível")
    
