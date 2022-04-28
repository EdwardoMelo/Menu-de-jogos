import random
def jogar():
     imprime_mensagem_abertura()
     palavra_secreta = carrega_palavra_secreta()
     letras_acertadas = incializa_letras_acertadas(palavra_secreta)
     acertou = False
     enforcou = False
     erros = 0 

     while(not acertou and not enforcou): 
         print(letras_acertadas)
         letra_chutada = pede_chute()

         if (letra_chutada in palavra_secreta):
             marca_posicao_correta(letra_chutada, letras_acertadas, palavra_secreta)
         else:
             erros = erros +1
        
         print(letras_acertadas) #imprimir as letras acertadas, que vão aparecer apenas nas posições que receberam o chute=letra
         acertou = '_' not in letras_acertadas
         enforcou = erros == 3

         if (acertou):
             imprime_mensagem_vencedor()
         if (enforcou):
             imprime_mensagem_perdedor()

def imprime_mensagem_abertura():
     print('***BEM VINDO AO JOGO DA FORCA***\n')
     print('VOCE TEM 6 TENTATIVAS\n')
     print('********************************\n')
def carrega_palavra_secreta():
     arquivo = open ('palavras.txt', 'r')
     palavras = [] #abrindo variavel de lista para receber as palavras do arquivo 

     for linha in arquivo:
         linha = linha.strip() #linha é igual a linha menos o \n
         palavras.append(linha) #adicionando a linha (palavra) na variavel palavras
     arquivo.close()

     numero = random.randrange (0, len(palavras) )
     palavra_secreta = palavras[numero].upper()
     return palavra_secreta
def incializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]
def pede_chute():
     letra_chutada = input('Qual a letra? ') 
     letra_chutada = letra_chutada.upper().strip()      
     return letra_chutada
def marca_posicao_correta(letra_chutada, letras_acertadas, palavra_secreta):
     posicao = 0 
     for letra in palavra_secreta: 
         if (letra_chutada.upper() == letra.upper()): 
             letras_acertadas[posicao]=letra 
         posicao = posicao +1    
def imprime_mensagem_vencedor():
     print('***** VOCE COMPLETOU A PALAVRA ******!')
def imprime_mensagem_perdedor():
     print ('Voce perdeu! FIm do Jogo!')
