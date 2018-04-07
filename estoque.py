import sys

idProduto = sys.argv[1]
operacao = sys.argv[2]
qtd = sys.argv[3]

class Estoque:

    def verificaQtd_minima(self, idProduto):
        # Consulta no banco
        if(int(idProduto) == 1):
            return 10
        elif(int(idProduto) == 2):
            return 3


    def consulta_estoque(self, idProduto):
        # Consulta no banco
        if(int(idProduto) == 1):
            return 20
        elif(int(idProduto) == 2):
            return 5


    def calcula_estoque(self, operacao, qtd):
        estoque_atual = self.consulta_estoque(idProduto)

        if(operacao == "saida"):
            qtd_atual = int(estoque_atual) - int(qtd)
            estoque_minimo = self.verificaQtd_minima(idProduto)

            if(qtd_atual <= 0):
                print("Idiota, não tem")
            elif(qtd_atual <= estoque_minimo):
                print("Porra você precisa adicionar produtos no estoque carai")

        else:
            qtd_atual = int(estoque_atual) + int(qtd)

        return qtd_atual




estoque = Estoque()
print(estoque.calcula_estoque(operacao, qtd))
