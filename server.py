import Pyro4
import time


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Chat(object):
    def __init__(self):
        self.conexao = {}
        self.players = []
        self.turno = 0
        self.mapeamento_peca = []
        self.backup_mapeamento_peca = []



    def getPlayers(self):
        return self.players

    def getTurno(self):
        return self.turno

    def getMapeamento_peca(self):
        return self.mapeamento_peca

    def setMapeamento_peca(self, mapeamento_peca, conexao):
        self.mapeamento_peca = mapeamento_peca

    def backup_peca(self,mapeameto_peca,conexao):
        self.backup_mapeamento_peca = mapeameto_peca

    def reiniciar_partida(self,conexao):
        self.mapeamento_peca = self.backup_mapeamento_peca
        self.Broadcast_msg(conexao,'Servidor','Partida Reiniciada')

    def checkWin(self,mapeamento_peca,conexao):
        self.player1Pieces = 0;
        self.player2Pieces = 0;
        for i,j in enumerate(mapeamento_peca):
            for k,l in enumerate(j):
                if mapeamento_peca[i][k] == 1:
                    self.player1Pieces += 1
                elif mapeamento_peca[i][k] == 2:
                    self.player2Pieces += 1
        if self.player1Pieces == 2:
            #self.Broadcast_msg(conexao,'Servidor',"Vitoria do Player 2")
            return 0
        elif self.player2Pieces == 2:
            #self.Broadcast_msg(conexao, 'Servidor', "Vitoria do Player 1")
            return 1


    def setTurno(self, turno, conexao):
        self.turno = turno


    def Connect(self, conexao, player, callback):
        if conexao not in self.conexao:
            self.conexao[conexao] = []
        self.conexao[conexao].append((player, callback))
        self.players.append(player)
        self.Send_server_msg(conexao, player, "Conexao com " + player + " iniciada")
        time.sleep(0.2)
        # self.publish(conexao, "Servidor", "Conexao com " + player + " iniciada")

    def Send_server_msg(self, conexao, player, mensagem):
        if len(self.players) == 1:
            p, c = self.conexao[conexao][0]
            c.message('Servidor', mensagem)
        else:
            p, c = self.conexao[conexao][1]
            c.message('Servidor', mensagem)

    #### função em que um cliente envia mensagem para o servidor que a envia para o outro cliente
    def Send_msg(self, conexao, player, mensagem):
        for (p, c) in self.conexao[conexao]:
            if p == player:
                if player == self.players[0]:
                    c.message(self.players[1], mensagem)
                elif player == self.players[1]:
                    c.message(self.players[0], mensagem)

    ##### função em que o servidor envia mensagem para os dois clientes
    def Broadcast_msg(self, channel, player, msg):
        for (p, c) in self.conexao[channel]:
            try:
                c.message(player, msg)
            except Pyro4.errors.ConnectionClosedError:
                # connection dropped, remove the listener if it's still there
                # check for existence because other thread may have killed it already
                if (p, c) in self.conexao[channel]:
                    self.conexao[channel].remove((p, c))
                    print('Removed dead listener %s %s' % (p, c))

    def desistir(self,channel,player):
        for (p,c) in self.conexao[channel]:
            if p == player:
                self.conexao[channel].remove((p,c))
                self.players.remove(p)
                print('aqui')
                break
        if len(self.conexao[channel]) > 0:
            self.Broadcast_msg(channel, 'Servidor', player + " Desistiu do jogo")
        else:
            del self.conexao[channel]


    def publish(self, channel, player, msg):
        for (p, c) in self.conexao[channel]:
            try:
                c.message(player, msg)
            except Pyro4.errors.ConnectionClosedError:
                # connection dropped, remove the listener if it's still there
                # check for existence because other thread may have killed it already
                if (p, c) in self.conexao[channel]:
                    self.conexao[channel].remove((p, c))
                    print('Removed dead listener %s %s' % (p, c))


Pyro4.Daemon.serveSimple({
    Chat: "example.chat.server"
})
