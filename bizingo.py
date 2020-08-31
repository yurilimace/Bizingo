import pygame
import pygame_gui

from client import Client
from client import DaemonThread
from mapeamento import Mapeamento
from tabuleiro import Tabuleiro

mapa = Mapeamento()
mapa.Mapeamento_casa()

client = Client()
daemonThread = DaemonThread(client)
daemonThread.start()
client.start_conexao()

pygame.init()
html = """"""
html = html + client.chat_history
screen = pygame.display.set_mode([960, 680])
manager = pygame_gui.UIManager((400, 400), "style.JSON")
manager2 = pygame_gui.UIManager((400, 400), "style2.JSON")
chat_entryText = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((680, 600), (270, 200)),
                                            manager=manager)

chat_textBox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((680, 80), (270, 520)),
                                             html_text=html,
                                             manager=manager)

server_log = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((205, 20), (270, 39)),
                                           html_text='',
                                           manager=manager2)

button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((730, 25), (180, 30)),
                                            text='Reiniciar Partida',
                                            manager=manager)

id = client.nick
turno = client.getTurno()
screen.fill([203, 237, 216])
clock = pygame.time.Clock()
table = Tabuleiro(screen)
table.desenha_tabuleiro(mapa)
table.distribuir_pecas(mapa)
client.setMapeamentopeca(mapa.mapeamento_peca)
client.server_backup(mapa.mapeamento_peca)
manager.draw_ui(screen)
manager2.draw_ui(screen)
pygame.display.flip()

running = True
ganhador = False

recieve = len(client.chat_history)
click_cont = 0
while running:
    if turno == 0:
        info = '<font  size=5>' + '<b>' + id + '</b>' + '<br>' + '<b>' + "Player 1 Turno" + '</b>' + '</font>'
        server_log = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((205, 20), (270, 100)),
                                                   html_text=info,
                                                   manager=manager2)

    elif turno == 1:
        info = '<font  size=5>' + '<b>' + id + '</b>' + '<br>' + '<b>' + "Player 2 Turno" + '</b>' + '</font>'
        server_log = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((205, 20), (270, 100)),
                                                   html_text=info,
                                                   manager=manager2)

    if client.checkWin(mapa.mapeamento_peca) == 1 and not ganhador:
        ganhador = True
        client.chat_history = client.chat_history + '<font  color=#437C17>' + '<b>' + "Servidor" + ":" + " " + "Player 1 Ganhou" + '</b>' + '<br>' + '<br>' + '</font>'
        print("Player 1 Ganhou")
        client.setTurno(3)

    elif client.checkWin(mapa.mapeamento_peca) == 0 and not ganhador:
        ganhador = True
        client.chat_history = client.chat_history +'<font  color=#437C17>' + '<b>' + "Servidor" + ":" + " " + "Player 2 Ganhou" + '</b>' + '<br>' + '<br>' + '</font>'
        print("Player 2 Ganhou")
        client.setTurno(3)

    elif turno == 1 and ganhador:
        ganhador = False

    elif turno == 0 and ganhador:
        ganhador = False



    time_delta = clock.tick(60) / 1000.0
    if recieve < len(client.chat_history):
        chat_textBox.kill()
        print(client.chat_history)
        html = client.chat_history
        chat_textBox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((680, 80), (270, 520)),
                                                     html_text=html,
                                                     manager=manager)
        recieve = len(client.chat_history)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            client.desistir(id)
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                texto = chat_entryText.get_text()
                client.chat_history = client.chat_history + str('<font  color=#0000FF>' + id + ":" + " " + texto + '<br>' + '</font>')
                print(client.chat_history)
                chat_entryText.set_text('')
                client.send(texto)
        manager.process_events(event)
        manager2.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == button:
                    client.reiniciar_partida()
                    client.setTurno(0)
                    ganhador = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and turno == 0 and id == "Player 1" and not ganhador:
                if click_cont == 0:
                    x, y = pygame.mouse.get_pos()
                    isPeca = table.check_peca(x, y, mapa, turno)
                    if isPeca != 0:
                        screen.fill([203, 237, 216])
                        click_cont += 2
                        pygame.event.wait()
                    else:
                        click_cont = 0
                elif click_cont == 2:
                    x1, x2 = pygame.mouse.get_pos()
                    empty = table.check_peca(x1, x2, mapa, turno)
                    table.move_peca(x1, x2, mapa, isPeca, turno)
                    table.captura_peca(x1, x2, mapa, empty, turno)
                    screen.fill([203, 237, 216])
                    click_cont = 0
                    client.setMapeamentopeca(mapa.mapeamento_peca)
                    client.setTurno(1)
            elif pygame.mouse.get_pressed()[0] and id == "Player 1" and turno == 1:
                print('não é seu turno')
                # client.chat_history = client.chat_history + str("Servidor" + ":" + " " + "nao é seu turno" + '<br>')

            elif pygame.mouse.get_pressed()[0] and turno == 1 and id == "Player 2" and not ganhador:
                if click_cont == 0:
                    x, y = pygame.mouse.get_pos()
                    isPeca = table.check_peca(x, y, mapa, turno)
                    if isPeca != 0:
                        screen.fill([203, 237, 216])
                        click_cont += 2
                        pygame.event.wait()
                    else:
                        click_cont = 0
                elif click_cont == 2:
                    x1, x2 = pygame.mouse.get_pos()
                    empty = table.check_peca(x1, x2, mapa, turno)
                    table.move_peca(x1, x2, mapa, isPeca, turno)
                    table.captura_peca(x1, x2, mapa, empty, turno)
                    screen.fill([203, 237, 216])
                    click_cont = 0
                    client.setMapeamentopeca(mapa.mapeamento_peca)
                    client.setTurno(0)
            elif pygame.mouse.get_pressed()[0] and id == "Player 2" and turno == 0:
                print("não é seu turno")

    manager.update(time_delta)
    manager.draw_ui(screen)
    manager2.draw_ui(screen)
    mapa.mapeamento_peca = client.getMapeamento()
    table.redesenha_tabuleiro(mapa)
    table.redesenha_peca(mapa)
    turno = client.getTurno()
    pygame.display.flip()
    pygame.event.pump()

