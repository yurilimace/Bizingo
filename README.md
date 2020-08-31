# Jogo de Tabuleiro Bizingo
implementacão do jogo de tabuleiro Bizingo integrado com um chat para a interação entre os jogadores. usando como comunicação distribuida a tecnologia RPC(Remote Procedere Call) através da biblioteca Pyro4 e interface grafica contruida com pygame.

## Autor
José Yuri Lira Lira


### Executando o Projeto
1 - Instale o Pyro4 e o pygame utilizando os comandos rodando no prompt de comando o  pip, para o pygame insira o comando "pip install pygame" para o Pyro4 "pip install Pyro4" e para o pygame_gui "pip install pygame-gui"
2 - Para executar o jogo é necessário primeiro executar o servidor de nomes através do comando "python -m Pyro4.naming"
3 - Após a execução do servidor de nomes é necessário executar o servidor do jogo basta rodar o arquivo server.py
4 - após a execução desses dois arquivos execute o arquivo bizingo.py e o jogo será aberto


#### Tecnologias Utilizadas
* Python
* Pyro4
* Pygame
