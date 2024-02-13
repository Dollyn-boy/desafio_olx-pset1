class Persistencia:

    _instancia = None

    @classmethod
    def get_instance(Persistencia):
        if not Persistencia._instancia:
            Persistencia._instancia = Persistencia()
        return Persistencia._instancia
    
    def __init__(self):
        self.usuarios = []

    def get_usuarios(self):
        return self.usuarios