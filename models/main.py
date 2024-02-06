from Estoque import Estoque
from Usuario import Usuario



user2 = Usuario("Cassio do Corhinthias", "cassio@yahoo.com", "cassiochan", 90000023, "1234567890")
user2.inserir_endereco("22430000")
user2.lista_enderecos()
user2.modo_vendedor()
user2.executar_comportamento("Bola", "bola de futeball", 29.99, "Esportes", 1)
user2.executar_comportamento("Sabre de Luz", "sabre de luz azul", 159.99, "Nerd", 1)
estoque = Estoque()
estoque.listar_estoque()

