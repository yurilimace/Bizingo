import numpy as np
import pygame
class Tabuleiro(object):
    #construtor
    def __init__(self,screen):
        self.linha = 11
        self.coluna = 21
        self.ponto_a = np.array([280,80])
        self.ponto_b = np.array([252,130])
        self.ponto_c = np.array([308,130])
        self.screen = screen

    def getOrigem(self):
        return [self.ponto_a,self.ponto_b,self.ponto_c]



    def desenha_tabuleiro(self,mapa):
        desloc_lat = np.array([27, 50])
        diagonal = np.array([-27, 50])
        for i in range(0, 11):
            aux_a = self.ponto_a
            aux_b = self.ponto_b
            aux_c = self.ponto_c
            linha = []
            linha_rect =[]
            # print(i)
            if (i < 9):
                #aux_a = self.ponto_a
                #aux_b = self.ponto_b
                #aux_c = self.ponto_c
                # print(i)
                for j in range(0, 21):
                    if mapa.mapeamento_casa[i][j] == 0:
                        linha.append(0)
                        linha_rect.append(0)
                    elif mapa.mapeamento_casa[i][j] == 1:
                        # print(ponto_a,ponto_b,ponto_c)
                        rect = pygame.rect.Rect(self.ponto_a[0]-11,self.ponto_a[1]+26,20,20)
                        pygame.draw.polygon(self.screen, (60, 170, 104), [self.ponto_a,self.ponto_b,self.ponto_c])
                       # pygame.draw.rect(self.screen,(0,0,139),rect)
                        linha.append([self.ponto_a,self.ponto_b,self.ponto_c])
                        linha_rect.append(rect)
                       #self.matriz_tabuleiro[i][j] = [1,[self.ponto_a,self.ponto_b,self.ponto_c]]
                        aux = np.array([desloc_lat[0], -desloc_lat[1]])
                        self.ponto_a = self.ponto_a + desloc_lat
                        self.ponto_b = self.ponto_b + aux
                        self.ponto_c = self.ponto_c + aux
                    else:
                        rect = pygame.rect.Rect(self.ponto_b[0] + 18, self.ponto_a[1] - 43, 20, 20)
                        pygame.draw.polygon(self.screen, (255, 255, 255), [self.ponto_a,self.ponto_b,self.ponto_c])
                        #pygame.draw.rect(self.screen, (0, 0, 139), rect)
                        linha_rect.append(rect)
                        linha.append([self.ponto_a, self.ponto_b, self.ponto_c])
                        aux = np.array([desloc_lat[0], -desloc_lat[1]])
                        self.ponto_a = self.ponto_a + aux
                        self.ponto_b = self.ponto_b + desloc_lat
                        self.ponto_c = self.ponto_c + desloc_lat
                    # print('peça escura')
                    # print(ponto_a, ponto_b, ponto_c)
                self.ponto_a = aux_a + diagonal
                self.ponto_b = aux_b + diagonal
                self.ponto_c = aux_c + diagonal
            # print(ponto_a,ponto_b,ponto_c)

            else:
                if i == 9:
                    aux = np.array([desloc_lat[0], desloc_lat[1]])
                    self.ponto_a = aux_a + aux
                    self.ponto_b = aux_b - diagonal
                    self.ponto_c = aux_c - diagonal
                if i == 10:
                    aux2 = np.array([0, desloc_lat[1] * 2])
                    self.ponto_a = aux_a + aux2

                for j in range(0, 21):
                    if mapa.mapeamento_casa[i][j] == 0:
                        linha.append(0)
                        linha_rect.append(0)
                    elif mapa.mapeamento_casa[i][j] == 2:
                        # print(ponto_a)
                        pygame.draw.polygon(self.screen, (255, 255, 255), [self.ponto_a,self.ponto_b,self.ponto_c])
                        rect = pygame.rect.Rect(self.ponto_b[0] + 18, self.ponto_a[1] - 43, 20, 20)
                        #pygame.draw.rect(self.screen, (0, 0, 139), rect)
                        linha.append([self.ponto_a, self.ponto_b, self.ponto_c])
                        linha_rect.append(rect)
                        if j == 0:
                            aux2 = np.array([desloc_lat[0], -desloc_lat[1]])
                            self.ponto_a = self.ponto_a + aux2
                            self.ponto_b = self.ponto_b + aux
                            self.ponto_c = self.ponto_c + aux
                            aux_a = self.ponto_a
                            aux_b = self.ponto_b
                            aux_c = self.ponto_c
                        else:
                            aux = np.array([desloc_lat[0], -desloc_lat[1]])
                            self.ponto_a = self.ponto_a + aux
                            self.ponto_b = self.ponto_b + desloc_lat
                            self.ponto_c = self.ponto_c + desloc_lat
                           # print(aux_a, aux_b, aux_c,j)

                    else:
                        pygame.draw.polygon(self.screen, (60, 170, 104), [self.ponto_a,self.ponto_b,self.ponto_c])
                        rect = pygame.rect.Rect(self.ponto_a[0] - 11, self.ponto_a[1] + 26, 20, 20)
                        #pygame.draw.rect(self.screen, (0, 0, 139), rect)
                        linha_rect.append(rect)
                        linha.append([self.ponto_a, self.ponto_b, self.ponto_c])
                        aux = np.array([desloc_lat[0], -desloc_lat[1]])
                        self.ponto_a = self.ponto_a + desloc_lat
                        self.ponto_b = self.ponto_b + aux
                        self.ponto_c = self.ponto_c + aux
                self.ponto_a = aux_a
                self.ponto_b = aux_b
                self.ponto_c = aux_c
            mapa.posicao_casa.append(linha)
            mapa.mapeamento_rect.append(linha_rect)


    def redesenha_tabuleiro(self,mapa):
        for i in range(0,self.linha):
            for j in range(0,self.coluna):
                if mapa.mapeamento_casa[i][j] == 0:
                    pass
                elif mapa.mapeamento_casa[i][j] == 1:
                    pygame.draw.polygon(self.screen,(60, 170, 104),mapa.posicao_casa[i][j])
                else:
                    pygame.draw.polygon(self.screen, (255, 255, 255),mapa.posicao_casa[i][j])



    def redesenha_rect(self,gameMatriz):
       for i in gameMatriz.mapeamento_rect:
           for j in i:
               if j != 0:
                   pygame.draw.rect(self.screen,(0,0,130),j)
               else:
                   pass

    def redesenha_peca(self,mapa):
        for i,j in enumerate(mapa.mapeamento_peca):
            for k,l in enumerate(j):
                if l!=0 and l==1:
                    x = mapa.mapeamento_rect[i][k][0] + 10
                    y = mapa.mapeamento_rect[i][k][1] + 10
                    pygame.draw.circle(self.screen, [200, 120, 50], (x,y), 8)
                elif l!=0 and l==2:
                    x = mapa.mapeamento_rect[i][k][0] + 10
                    y = mapa.mapeamento_rect[i][k][1] + 10
                    pygame.draw.circle(self.screen,[250, 10, 26], (x, y), 8)




    def distribuir_pecas(self,mapa):
        min = 8
        max = 12
        min2 = 2
        max2 = 17
        for i,j in enumerate( mapa.mapeamento_casa):
            linha = []
            for l,k in enumerate(j):
                if i > 1 and i < 6 and k == 1 and l > min and l < max:
                   # print(min, max)
                    #print(min)
                    #print(l)
                    x = mapa.mapeamento_rect[i][l][0] + 10
                    y = mapa.mapeamento_rect[i][l][1] + 10
                    linha.append(1)
                    pygame.draw.circle(self.screen,[200,120,50],(x,y),8)
                elif i>6 and  i<10 and k == 2 and l > min2 and l< max2:
                    x = mapa.mapeamento_rect[i][l][0] + 10
                    y = mapa.mapeamento_rect[i][l][1] + 10
                    linha.append(2)
                    pygame.draw.circle(self.screen, [250, 10, 26], (x, y),8)
                else:
                    linha.append(0)
            if( i>6 and i<9):
                min2 = min2+1
                max2 = max2-1
            min = min - 1
            max = max + 1
            mapa.mapeamento_peca.append(linha)

    ## fazer a movimentação da peca

    #### implementar o suicidio nas pontas
    def move_peca(self,x,y,mapeamento,teste,turno):
        for i, j in enumerate(mapeamento.mapeamento_rect):
            for k,l in enumerate(j):
                if l !=0 and l.collidepoint(x,y):
                    if(mapeamento.mapeamento_peca[i][k] == 0 and mapeamento.mapeamento_casa[i][k] == 1 and turno == 0):
                        mapeamento.mapeamento_peca[teste[0]][teste[1]] = 0
                        mapeamento.mapeamento_peca[i][k] = 1
                        if k < 20 and mapeamento.mapeamento_peca[i][k - 1] == 2 and mapeamento.mapeamento_peca[i][k + 1] == 2 and mapeamento.mapeamento_peca[i + 1][k] == 2:
                                print('SUICIDIO')
                                mapeamento.mapeamento_peca[i][k] = 0
                        elif k < 20 and mapeamento.mapeamento_peca[i][k-1] == 0 and mapeamento.mapeamento_peca[i][k+1] == 2 and mapeamento.mapeamento_peca[i+1][k] == 2:
                            print('SUICIDIO')
                            mapeamento.mapeamento_peca[i][k] = 0
                        elif k == 0 and i == 8 and mapeamento.mapeamento_peca[i][k+1] == 2 and mapeamento.mapeamento_peca[i+1][k] == 2:
                            print('SUICIDIO')
                            mapeamento.mapeamento_peca[i][k] = 0
                        elif k == 20 and i == 8 and mapeamento.mapeamento_peca[i][k-1] == 2 and mapeamento.mapeamento_peca[i+1][k] == 2:
                            print('SUICIDIO')
                            mapeamento.mapeamento_peca[i][k] = 0


                        break
                    elif(mapeamento.mapeamento_peca[i][k] == 0 and mapeamento.mapeamento_casa[i][k] == 2 and turno ==1):
                        mapeamento.mapeamento_peca[teste[0]][teste[1]] = 0
                        mapeamento.mapeamento_peca[i][k] = 2
                        if k < 20 and mapeamento.mapeamento_peca[i][k-1] == 1 and mapeamento.mapeamento_peca[i][k+1] == 1 and mapeamento.mapeamento_peca[i-1][k] == 1:
                            print('SUICIDIO')
                            mapeamento.mapeamento_peca[i][k] = 0
                        elif i == 10 and mapeamento.mapeamento_peca[i-1][k] == 1 and mapeamento.mapeamento_peca[i][k+1] == 1:
                            print('SUICIDIO')
                            mapeamento.mapeamento_peca[i][k] = 0
                        elif i == 10 and mapeamento.mapeamento_peca[i-1][k] == 1 and mapeamento.mapeamento_peca[i][k-1] == 1:
                            print('SUICIDIO')
                            mapeamento.mapeamento_peca[i][k] = 0
                        break



    def checa_vitoria(self,mapeamento,turno,nclient,v):
        cont = 0
        for i,j in enumerate(mapeamento.mapeamento_peca):
            for k,l in enumerate(j):
                if mapeamento.mapeamento_peca[i][k] == 2 and turno == 0:
                    cont+=1
                elif mapeamento.mapeamento_peca[i][k] == 1 and turno == 1:
                    cont+=1
        if cont == 2 and turno == 0:
            print("Jogador 1 Venceu")
            return  1
        elif cont == 2 and turno ==1:
            print("Jogador 2 Venceu")


    def captura_peca(self,x,y,mapeamento,teste,turno):
        min = 8
        max = 12
        for i,j in enumerate(mapeamento.mapeamento_peca):
            for k,l in enumerate(j):
                if turno ==0:
                    if k < 19 and i < 10 and mapeamento.mapeamento_peca[i][k] == 1 and mapeamento.mapeamento_peca[i][k+1] ==2 and (mapeamento.mapeamento_peca[i-1][k+1] ==1 and mapeamento.mapeamento_peca[i][k++2] ==1):
                        print('captura')
                        mapeamento.mapeamento_peca[i][k + 1] = 0
                    elif k < 21 and i == 9 and mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_peca[i][k - 1] == 1 and mapeamento.mapeamento_peca[i - 1][k] == 1:
                        mapeamento.mapeamento_peca[i][k] = 0
                    elif k == 0 and i == 9 and mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_peca[i][k + 1] == 1 and mapeamento.mapeamento_peca[i - 1][k] == 1:
                        mapeamento.mapeamento_peca[i][k] = 0
                    elif k == 20 and mapeamento.mapeamento_peca[i][k] == 1 and mapeamento.mapeamento_peca[i][k - 1] == 2 and mapeamento.mapeamento_peca[i - 1][k - 1] == 1 and mapeamento.mapeamento_peca[i][k - 2]:
                        mapeamento.mapeamento_peca[i][k - 1] == 0
                    elif i == 0 and mapeamento.mapeamento_peca[i][k] == 1 and mapeamento.mapeamento_peca[i][k+1] == 2 and mapeamento.mapeamento_peca[i][k+2] == 1:
                        mapeamento.mapeamento_peca[i][k + 1] = 0
                    elif i == 10 and mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_peca[i][k+1] ==1 and (mapeamento.mapeamento_peca[i-1][k] ==1):
                        mapeamento.mapeamento_peca[i][k] = 0
                    elif i == 10 and mapeamento.mapeamento_peca[i][k] == 1 and mapeamento.mapeamento_peca[i][k+1] == 2 and mapeamento.mapeamento_peca[i-1][k+1]==1:
                        mapeamento.mapeamento_peca[i][k+1] = 0
                elif turno == 1:
                    if k < 19 and i < 10 and mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_peca[i][k+1] == 1 and (mapeamento.mapeamento_peca[i+1][k+1] ==2 and mapeamento.mapeamento_peca[i][k++2] ==2):
                        mapeamento.mapeamento_peca[i][k+1] = 0
                    elif k == max-1 and i < 8 and mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_peca[i][k + 1] == 1 and mapeamento.mapeamento_peca[i][k + 2] == 0 and mapeamento.mapeamento_peca[i + 1][k + 1] == 2:
                        print('aqui1')
                        mapeamento.mapeamento_peca[i][k + 1] = 0
                    elif k == min+1 and i < 8 and mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_peca[i][k - 1] == 1 and mapeamento.mapeamento_peca[i][k - 2] == 0 and mapeamento.mapeamento_peca[i + 1][k - 1] == 2:
                        print('aqui2')
                        mapeamento.mapeamento_peca[i][k - 1] = 0
                    elif k == 19 and i == 8 and mapeamento.mapeamento_peca[i][k] == 2 and  mapeamento.mapeamento_peca[i][k+1] == 1 and mapeamento.mapeamento_peca[i-1][k+1] == 0 and mapeamento.mapeamento_peca[i+1][k+1] == 2:
                        mapeamento.mapeamento_peca[i][k+1] = 0
                    elif k == 1 and i == 8 and mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_peca[i][k - 1] == 1 and mapeamento.mapeamento_peca[i - 1][k - 1] == 0 and mapeamento.mapeamento_peca[i + 1][k - 1] == 2:
                        mapeamento.mapeamento_peca[i][k - 1] = 0
                    elif i == 10 and mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_peca[i][k+1] == 1 and mapeamento.mapeamento_peca[i][k+2] ==2:
                        mapeamento.mapeamento_peca[i][k + 1] = 0
            if min > -1 and i<9:
                min = min - 1
                max = max + 1











    def check_peca(self,x,y,mapeamento,turno):
        for i, j in enumerate(mapeamento.mapeamento_rect):
            for k, l in enumerate(j):
                aux = 50
                if l != 0 and l.collidepoint(x, y):
                    if(mapeamento.mapeamento_peca[i][k] == 1 and mapeamento.mapeamento_casa[i][k] == 1 and turno == 0):
                        print('casa tem peca turno 1')
                    elif(mapeamento.mapeamento_peca[i][k] == 2 and mapeamento.mapeamento_casa[i][k] == 2 and turno == 1):
                        print('casa tem peca turno 2')
                    #elif(mapeamento.mapeamento_peca[i][k] == 0 and mapeamento.mapeamento_casa[i][k] == 1):
                        #print(i, 'aqui')
                        #print('casa nao tem peca')
                    else:
                        print('não é peca')
                        return 0
                    return (i, k)
                    break

        return 0