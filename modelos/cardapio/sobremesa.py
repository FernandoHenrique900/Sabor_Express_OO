from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):#filho do ItemCardapio - herda metodos e atributos
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome,preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self): #mostrar o nome no app.py
        return self._nome
    
    def aplicar_desconto(self):
            self._preco -= (self._preco*0.15)