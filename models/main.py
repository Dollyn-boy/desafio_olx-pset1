from Usuario import Usuario

user1 = Usuario("Vitor", "vitordoreahdx11@gmail.com", "DomVital", 89028922, "japodaomossar123")
#User pode ter mais de 1 endereço
user1.inserir_endereco("44640000")
user1.inserir_endereco("22430000")
user1.lista_enderecos()