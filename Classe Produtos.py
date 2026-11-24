class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, qtd):
        if qtd > 0:
            if qtd <= self.estoque:
                self.estoque -= qtd  
                print(f"Vendido: {qtd} unidades de {self.nome}")
            else:
                print("Quantidade inválida! Entre em contato conosco para fazer uma encomenda ou tirar dúvidas.")

    def get_produto(self):
        return self.estoque

produto = Produto("Caderno", 15.50, 100)

print(f"Quantidade de produtos inicial: {produto.get_produto()}")

produto.vender(45)

print(f"Quantidade de produtos final: {produto.get_produto()}")

        