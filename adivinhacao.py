# -*- coding: utf-8 -*-
''
print('*****************************')
print('*    Joga da Adivinhação    *')
print('*****************************')

nivel1 = 20
nivel2 = 10
nivel3 = 5

numero_secreto = 42
pontos = 1000
print('Nivel 1 digite 1\nNivel 2 digite 2\nNivel 3 digite 3')
total_tentativas = int(input('Escolha o nivel de dificuldade: '))
rodada = 1

if total_tentativas == 1:
    for rodada in range(1, nivel1 + 1):
        print('Você tem {0} pontos'.format(pontos))
        print('Tentativas {0} de {1}'.format(rodada, nivel1))
        chute = int(input('Digite seu número: '))
        print('Você digitou:', chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou!')
            break
        elif maior:
            print('Você errou! O chute foi maior que o número secreto')
        elif menor:
            print('Você errou! O chute foi menor que o número secreto')

        rodada = rodada + 1
        if chute < pontos:
            pontos = pontos - chute

elif total_tentativas == 2:
    for rodada in range(1, nivel2 + 1):
        print('Você tem {0} pontos'.format(pontos))
        print('Tentativas {0} de {1}'.format(rodada, nivel2))
        chute = int(input('Digite seu número: '))
        print('Você digitou:', chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou!')
            break
        elif maior:
            print('Você errou! O chute foi maior que o número secreto')
        elif menor:
            print('Você errou! O chute foi menor que o número secreto')

        rodada = rodada + 1
        if chute < pontos:
            pontos = pontos - chute

elif total_tentativas == 3:
    for rodada in range(1, nivel3 + 1):
        print('Você tem {0} pontos'.format(pontos))
        print('Tentativas {0} de {1}'.format(rodada, nivel3))
        chute = int(input('Digite seu número: '))
        print('Você digitou:', chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou!')
            break
        elif maior:
            print('Você errou! O chute foi maior que o número secreto')
        elif menor:
            print('Você errou! O chute foi menor que o número secreto')

        rodada = rodada + 1
        if chute < pontos:
            pontos = pontos - chute

print('Pontos: {0}'.format(pontos))
print('Fim de Jogo')
print('Jogou bem!')
