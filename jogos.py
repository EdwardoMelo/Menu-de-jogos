import forca
import advinhacao

jogando = True
while (jogando == True):
    print('*********************************')
    print('********MENU DE JOGOS********')
    print('*********************************')

    print("[1]  -   Advinhe o número secreto")
    print("[2]  -   Jogo da Forca")
    print("[3]  -   Encerrar")
    escolha = int(input("Digite um número para escolher: "))
    if (escolha ==1):
        advinhacao.jogar()
    elif(escolha ==2):
        forca.jogar()
    elif(escolha ==3):
        exit()