import sys
import threading
import Pyro4


class Client(object):
    def __init__(self):
        self.chat = Pyro4.core.Proxy('PYRONAME:')
        self.abort = 0
        self.chat_history = ""

    @Pyro4.expose
    @Pyro4.oneway
    def message(self, nick, msg):
        if nick != self.nick and nick != "Servidor":
            self.chat_history += '<font  color=#FF0000>' + nick + ":" + " " + msg + '<br>' + '</font>'
            #print(self.chat_history)
            #print(self.chat_history)
        elif nick == "Servidor":
            self.chat_history += '<font  color=#437C17>' + '<b>' + nick + ":" + " " + msg + '</b>' +'<br>' + '<br>' + '</font>'



    def jogada(self,mapeamento_peca):
        return mapeamento_peca

    def getTurno(self):
        return self.chat.getTurno()

    def setTurno(self,turno):
        self.chat.setTurno(turno,self.conexao)

    def getMapeamento(self):
        return self.chat.getMapeamento_peca()

    def setMapeamentopeca(self,mapeamento_peca):
        self.chat.setMapeamento_peca(mapeamento_peca,self.conexao)

    def server_backup(self,mapeamento_peca):
        self.chat.backup_peca(mapeamento_peca,self.conexao)

    def reiniciar_partida(self):
        self.chat.reiniciar_partida(self.conexao)

    def checkWin(self,mapeamento_peca):
        return self.chat.checkWin(mapeamento_peca,self.conexao)

    def desistir(self,player):
        self.chat.desistir(self.conexao, player)

    def dispatch_broadcast(self,msg):
        self.chat.Broadcast_msg(self.conexao,"Servidor",msg)


    def restart_request(self,msg):
        request = msg.split("!")
        print(len(request))
        if len(request) == 3:
            text = self.nick + " " + request[1]
            print(text)
            self.chat.Send_msg(self.conexao,'Servidor',text)

    def send(self, msg):
        if msg:
            if self.nick == 'Player 1':
                self.chat.Send_msg(self.conexao, 'Player 2', msg)
            elif self.nick == 'Player 2':
                self.chat.Send_msg(self.conexao, 'Player 1', msg)

    def start_conexao(self):
        nicks = self.chat.getPlayers()
        if nicks:
            self.nick = 'Player 2'
            self.conexao = "jogo"
        else:
            self.nick = 'Player 1'
            self.conexao = "jogo"
        self.chat.Connect(self.conexao, self.nick, self)


class DaemonThread(threading.Thread):
    def __init__(self, chat):
        threading.Thread.__init__(self)
        self.chatter = chat
        self.setDaemon(True)

    def run(self):
        with Pyro4.core.Daemon() as daemon:
            daemon.register(self.chatter)
            daemon.requestLoop(lambda: not self.chatter.abort)

# chat = Client()
# daemonThread = DaemonThread(chat)
# daemonThread.start()
# chat.start_conexao()
