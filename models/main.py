from Estoque import Estoque
from Usuario import Usuario, ComportamentoComprador, ComportamentoDoUsuario, ComportamentoVendedor



user2 = Usuario("Cassio do Corhinthias", "cassio@yahoo.com", "cassiochan", 90000023, "1234567890")
user2.inserir_endereco("22430000")
user2.modo_vendedor()
user2.executar_comportamento("Bola", "bola de futeball", 29.99, "Esportes", 1)
user2.executar_comportamento("Bola", "bola de futeball", 29.99, "Esportes", 1)
user2.executar_comportamento("Bola", "bola de futeball", 29.99, "Esportes", 1)
estoque = Estoque()
estoque.listar_estoque()

