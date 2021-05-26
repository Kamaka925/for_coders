import promptlib
prompter = promptlib.Files()
filep = prompter.file()



class OPERACAO:

    def __init__(self, loja, dono, tipo, cartao, cpf, valor, data, hora, total):
        self.loja = loja
        self.dono = dono
        self.tipo = tipo
        self.cartao = cartao
        self.cpf = cpf
        self.valor = valor
        self.data = data
        self.hora = hora
        self.total = total


class CARGAR:

    def carregar():
        file = open(filep, encoding='utf-8', mode='r')
        dic = {
            "descricao": ["Debito", "Boleto", "Financiamento", "Credito", "Recebimento Emprestimo", "Vendas",
                          "Recebimento TED", "Recebimento DOC", "Aluguel"],
            "natureza": ["Entrada", "Saida", "Saida", "Entrada", "Entrada", "Entrada", "Entrada", "Entrada", "Saida"]
        }
        total = 0
        operacoes = []
        for x in file:
            tipo = dic["descricao"][int(x[0]) - 1]
            data = x[1:9]
            valor = int(x[9:19]) / 100
            if dic["natureza"][int(x[0]) - 1] == "Entrada":
                total += int(int(x[9:19]) / 100)
            else:
                total -= int(int(x[9:19]) / 100)
            cpf = x[19:30]
            cartao = x[30:42]
            hora = x[42:48]
            dono = x[48:61]
            loja = x[61:81]
            operacoes.append(OPERACAO(loja, dono, tipo, cartao, cpf, valor, data, hora, total))
        file.close()
        return operacoes

