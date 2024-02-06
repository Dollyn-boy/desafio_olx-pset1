class Estoque:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Estoque, cls).__new__(cls)
            # Inicialize quaisquer outros atributos necessários aqui
            cls._instancia.produtos_disponiveis = []
            cls._instancia.produtos_vendidos = []
        return cls._instancia
    
    
