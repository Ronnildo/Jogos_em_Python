# -*- coding: utf-8 -*-
print('*****************************')
print('*    Joga da Adivinhação    *')
print('*****************************')

numero_secreto = 42

chute = int(input('Digite seu número: '))
print('Você digitou:', chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print('Você acertou!')
elif maior:
    print('Você errou! O chute foi maior que o número secreto')
elif menor:
    print('Você errou! O chute foi menor que o número secreto')