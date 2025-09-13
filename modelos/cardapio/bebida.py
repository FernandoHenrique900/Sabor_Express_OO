from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio): #filho do ItemCardapio - herda metodos e atributos
    def __init__(self,nome,preco,tamanho):
        super().__init__(nome,preco) #comando super faz o acesso ao itens da classe ItemCardapio
        self.tamanho = tamanho

    def __str__(self): #mostrar o nome no app.py
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)