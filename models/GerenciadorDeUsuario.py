class GerenciadoDeUsuario:

    _instancia = None

    @classmethod
    def get_instance(GerenciadoDeUsuario):
        if not GerenciadoDeUsuario._instancia:
            GerenciadoDeUsuario._instancia = GerenciadoDeUsuario()
        return GerenciadoDeUsuario._instancia
    
    def __init__(self):
        self.usuarios = []

    def get_usuarios(self):
        return self.usuarios
    
    def add_usuario(self, user):
        self.usuarios.append(user)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"{usuario.nome} | {usuario.user}" )