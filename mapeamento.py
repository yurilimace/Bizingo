class Mapeamento(object):

    def __init__(self):
        self.linha = 11
        self.coluna = 21
        self.mapeamento_casa = []
        self.posicao_casa = []
        self.mapeamento_rect = []
        self.mapeamento_peca = []

    def Mapeamento_casa(self):
        min = 8
        max = 12
        for i in range(0, self.linha):
            linha = []
            for j in range(0, self.coluna):
                if i < 9 and j >= min and j <= max:
                    if i % 2 == 0 and j % 2 == 0:
                        linha.append(1)
                    elif i % 2 != 0 and j % 2 != 0:
                        linha.append(1)
                    else:
                        linha.append(2)
                elif i >= 9 and j > min and j < max:
                    if i % 2 == 0 and j % 2 == 0:
                        linha.append(1)
                    elif i % 2 != 0 and j % 2 != 0:
                        linha.append(1)
                    else:
                        linha.append(2)
                else:
                    linha.append(0)

            if min > -1:
                min = min - 1
                max = max + 1
            else:
                if i == 9:
                    # aux = np.array([diagonal[0], diagonal[1]])
                    # ponto_b = ponto_b - [-diagonal[0],diagonal[1]]
                    #  ponto_c = ponto_c - [-diagonal[0],diagonal[1]]
                    #  ponto_a = ponto_a + aux
                    #  cont_loop = 0
                    min = 0
                    max = 20
            self.mapeamento_casa.append(linha)
            #self.peca.append(linha)

        return self.mapeamento_casa

