#Gustavo Sobreira e Raphaella Ranieri

import pygame
from time import sleep
from random import randint
#Desenhar o tabuleiro
tabuleiro_player = []
tabuleiro_pc = []
repetir = 1
esconderijo_pc = []
esconderijo_player = []
barcos_play = 0
dimensao = int(input('\n\n\033[1;94mQUANTAS CASAS TERÁ NOSSA PARTIDA?\n'
                     'LEMBRE - SE QUE O JOGO É UM TABULEIRO QUADRDO\n'
                     '(Obs* Mínimo 4x4, escolha apenas a medida de um lado pois\n'
                     'as embarcações seram a divisão exata com dividendo 4)\n'
                     'LADO =  \033[m'))
def avisar_som():
    print('\033[31m                         -- > ATIVE O SOM < -- \033[m')
    sleep(2)

def apresentacao():
    print(' ')
    print(' ')
    print('                         ☠️ TORNEM SE LENDAS ☠️\n\n'
          '__________☠️ MARUJOS...AS TROPAS DA RAINHA VITÓRIA SE APROXIMAM ☠️__________\n'
          '__________☠️ HOJE SERÁ O NOSSO GRANDE DIA! AFUNDAREMOS TODOS!   ☠️__________\n'
          '__________☠️ HOJE NÃO EXISTE FRAQUEZA, HOJE NÃO EXISTE RECUAR   ☠️__________\n'
          '__________☠️ MOSTRAREMOS A TODOS O VALOR DE UM PIRATA           ☠️__________\n'
          '__________☠️   - - - - - - - - - - - - - - - - - - - - - - - -  ☠️__________\n'
          '__________☠️ PREPAREM OS CANHÕES E AS CANECAS DE RUN !!!        ☠️__________')
    print('''                              \033[1;33m💦\033[m\033[1;97m☁☁☁☁\033[m                         
                              \033[1;37m🍺\033[1;33m🍺🍺🍺 \033[1;37m🍻                                      
                              \033[1;37m🍺\033[1;33m🍺🍺🍺\033[1;37m🍺   🍻                                  
                              \033[1;37m🍺\033[1;33m🍺🍺🍺\033[1;37m🍺    🍻                                 
                              \033[1;37m🍺\033[1;33m🍺🍺🍺\033[1;37m🍺   🍻                                  
                              \033[1;37m🍺\033[1;33m🍺🍺🍺\033[1;37m🍺🍻                                    
                              \033[1;37m🍺\033[1;33m🍺🍺🍺\033[1;37m🍺                                      
                              \033[1;37m🍺🍺🍺🍺🍺\033[m''')

def musica_tema():

    pygame.mixer.init()

    pygame.init()  # essa inicialização nos meus testes, não foi necessária

    pygame.mixer.music.load('musica.mp3')

    pygame.mixer.music.play()

    pygame.mixer.music.set_volume(0.20)

    x = input('__________☠️ SE NESTIVER PRONTO DIGITE QUALQUER COISA IWOW      ☠️__________\n'
              '__________☠️            ASSINADO REI DOS PIRATAS                ☠️__________\n'
              '  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

def montar_player():
    if repetir == 1:
        avisar_som()
        apresentacao()
        musica_tema()

    for coluna_player in range(dimensao):
        if repetir == 1:
            tabuleiro_player.append(['| \033[31m⚓\033[m | '] * dimensao)

    #Usar esse repetir foi o modo que achei para as listas não dobrarem de tamanho
    #print(repetir)

    contador = 0

    for linha in tabuleiro_player:
        print(f'L -{contador:3}', end=' ➡ ')
        contador += 1
        print(''.join(linha))

def montar_pc():
    montar_player()
    print('         ', '☠️‍☠️☠‍' * len(tabuleiro_player))
    for coluna_pc in range(len(tabuleiro_player)):
        if repetir == 1:
            tabuleiro_pc.append(['| \033[32m⚓\033[m | '] * len(tabuleiro_player))

    contador = 0
    cont_coluna = -1
    for linha_pc in tabuleiro_pc:
        print(f'L -{contador:3}', end=' ➡ ')
        contador += 1
        print(''.join(linha_pc))

    for c in range(len(tabuleiro_player)):
        cont_coluna += 1
        if cont_coluna == 0:
            print(f'           C-{cont_coluna}',end='   ')
        else:
            if cont_coluna % 3 == 0:
                print(f'C-{cont_coluna}', end='    ')
            else:
                print(f'C-{cont_coluna}', end='   ')
    print('\n')

montar_pc()
if repetir == 1:
    repetir += 1

def jogada_esconde_pc():
    num_jogadas_pc = len(tabuleiro_player) // 4
    while num_jogadas_pc != 0:
        posicione_linha_pc = randint(0, len(tabuleiro_player) - 1)
        posicione_coluna_pc = randint(0, len(tabuleiro_player) - 1)
        if tabuleiro_pc[posicione_linha_pc][posicione_coluna_pc] == '| \033[32m⚓\033[m | ':
            num_jogadas_pc -= 1
            esconderijo_pc.append(posicione_linha_pc)
            esconderijo_pc.append(posicione_coluna_pc)


        else:
            while tabuleiro_pc[posicione_linha_pc][posicione_coluna_pc] != '| \033[32m⚓\033[m | ':
                posicione_linha_pc = randint(0, len(tabuleiro_player) - 1)
                posicione_coluna_pc = randint(0, len(tabuleiro_player) - 1)


def jogada_esconde_player():
    jogada_esconde_pc()
    num_jogadas_player = len(tabuleiro_player) // 4
    while num_jogadas_player != 0:
        posicione_linha_player = int(input('\033[1;94mNOSSAS TROPAS FICAM NO LADO \033[1;31mVERMELHO\033[1;94m, POSICIONE-AS\n L -  \033[m'))
        posicione_coluna_player = int(input(' \033[1;94mC -  \033[m'))
        if tabuleiro_player[posicione_linha_player][posicione_coluna_player] == '| \033[31m⚓\033[m | ':
            num_jogadas_player -= 1
            tabuleiro_player[posicione_linha_player][posicione_coluna_player] = '  \033[1;37m⛵\033[m   '
            esconderijo_player.append(posicione_linha_player)
            esconderijo_player.append(posicione_coluna_player)

        else:
            while tabuleiro_player[posicione_linha_player][posicione_coluna_player] != '| \033[31m⚓\033[m | ':
                posicione_linha_player = int(input('NOSSAS TROPAS FICAM NO LADO VERMELHO, POSICIONE-AS\n L -  '))
                posicione_coluna_player = int(input(' C -  '))
    montar_pc()

def tiroteio():

    jogada_esconde_player()

    barcos_pc = len(tabuleiro_pc) // 4
    barcos_player = len(tabuleiro_player) // 4

    while barcos_player != 0 and barcos_pc != 0:
        #print(esconderijo_pc)
        atire_linha_pc = int(input('\033[1;94mATIRE EM UMA LINHA DO NOSSO INIMIGO\n L -  '))
        atire_coluna_pc = int(input('ATIRE EM UMA CULUNA DO INIMIGO\n C -  \033[m'))

        for c in range(len(esconderijo_pc)):
            if esconderijo_pc[c - 1] == atire_linha_pc and esconderijo_pc[c] == atire_coluna_pc:
                tabuleiro_pc[atire_linha_pc][atire_coluna_pc] = '  X   '
                barcos_pc -= 1
                break

            else:
                if atire_linha_pc > len(tabuleiro_pc) or atire_coluna_pc > len(tabuleiro_pc):
                    print('\033[1;94mO tiro foi muito forte\033[m')

                else:
                    tabuleiro_pc[atire_linha_pc][atire_coluna_pc] = ' 🟧   '


        atire_linha_player = randint(0, len(tabuleiro_player) - 1)
        atire_coluna_player = randint(0, len(tabuleiro_player) - 1)

        for c in range(0, len(esconderijo_player)):
            if esconderijo_player[c - 1] == atire_linha_pc and esconderijo_player[c] == atire_coluna_pc:
                tabuleiro_player[atire_linha_player][atire_coluna_player] = '  X  '
                barcos_player -= 1
                break

            else:
                tabuleiro_player[atire_linha_player][atire_coluna_player] = ' 🟧   '
                montar_pc()

    if barcos_player == 0:
        print('GAME OVER')
        pygame.mixer.init()

        pygame.init()

        pygame.mixer.music.load('lose.mp3')

        pygame.mixer.music.play()

        pygame.mixer.music.set_volume(1)

        x = input('DIGITE QUALQUER COISA RÁPIDO, NÃO QUERO QUE ME VEJAM COM VOCÊ')

    else:
        print('YOU WIN')
        pygame.mixer.init()

        pygame.init()  # essa inicialização nos meus testes, não foi necessária

        pygame.mixer.music.load('quen.mp3')

        pygame.mixer.music.play()

        pygame.mixer.music.set_volume(1)

        x = input('MEU CAMPEÃO DIGITE QUALQUER COISA PARE ESTÁ MÚSICA INSPIRADA EM VOCÊ!')


tiroteio()
