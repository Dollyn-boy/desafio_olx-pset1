class Transacao:
    def realizar_transacao(self, usuario, anuncio):
        # Verificar se o produto está disponível na lista do vendedor
        if anuncio.produto in anuncio.vendedor.produtos and anuncio.is_disponivel():
            # Verificar se o comprador tem dinheiro suficiente
            if usuario.carteira >= anuncio.preco:
                # Remover produto da lista do vendedor e adicionar à lista do comprador
                anuncio.vendedor.produtos.remove(anuncio.produto)
                usuario.produtos.append(anuncio.produto)
                # Atualizar carteiras
                usuario.carteira -= anuncio.preco
                anuncio.vendedor.carteira += anuncio.preco
                print("Transação Concluída")
                usuario.exibir_status()
                #atualiza estado do anuncio
                anuncio.vender()
            else:
                print("Dinheiro Insuficiente")
        else:
            print("Produto Indisponível")

        