import random
def jogar():
     #aqui
     print('*****JOGO DA ADVINHAÇÃO*****\n')
     print('NUMEROS ALEATÓRIOS DE 1 - 12')
     print ('-----------------------------------------')
     n_tentativas = 4
     points = 0
     escolha = True
     while (escolha==True):
        cont_tentativas = 1
        n_secreto = random.randrange(1,12)
        while (cont_tentativas <= n_tentativas):
            print('Tentativa {} de {}!'.format (cont_tentativas, n_tentativas))
            chute = int ( input ('Chute um numero: '))
            acertou = chute == n_secreto
            menor = chute < n_secreto
            maior = chute > n_secreto #enquanto o contador de tentativas for menor que 3 
            if (acertou):
                print('------ Você acertou, ganhou 10 pontos! ------')
                points = points + 10
                break; 
            elif (menor):
                print('Você errou! o número é maior, tente novamente')
                cont_tentativas = cont_tentativas +1
            elif (maior):
                print('Você errou! o número é menor, tente novamente')
                cont_tentativas = cont_tentativas +1
        print ('-----------------------------------------')
        print ('-----------FIM DA RODADA-----------\n')
        print ('-----------NUMERO SECRETO: {}'. format (n_secreto))
        print (' [1]    -   CONTINUAR   -   Pontuação Atual: {} '. format(points))
        print (' [2]    -    ENCERRAR')
        escolha = int (input ('qual sua escolha?  '))
        if (escolha == 2):
            escolha = False
        elif(escolha ==1):
            escolha = True
