import random
counter = 0
print('_' * 30, end=' ')
print('DIVINATION', end=' ')
print('_' * 30)
print('_' * 31, end=' ')
print('the game', end=' ')
print('_' * 31)
print('')
print('Vamos jogar? Eu vou pensar em um número e você vai ter que advinhar!\n')
print('Escolha uma dificuldade:   1.Fácil   2.Média   3.Difícil   4.Hardcore\n')
dificuldade = int(input('Qual a dificuldade que deseja? (digite o número correspondente)\n'))
if dificuldade == 1:
    tentativas = 1
    n = random.randint(1, 5)
    print('O número está entre 1 e 5 e voce tem 1 tentativa!\n')
    while counter < tentativas:
        counter += 1
        number_choice = int(input('Qual foi o número em que pensei?\n'))
        if number_choice == n:
            print('Parabéns, você acertou, mas não vai ser tão fácil na próxima!\n')
        else:
            print('Você errou seu limitado, se esforce mais e um dia poderá ganhar de mim!\n')
elif dificuldade == 2:
    tentativas = 3
    print(f'O número está entre 1 e 20 e voce tem {tentativas} tentativas!')
    n = random.randint(1, 20)
    while counter < tentativas:
        counter += 1
        number_choice = int(input('Qual foi o número em que pensei?\n'))
        if number_choice == n:
            print('Parabéns, você acertou, mas não vai ser tão fácil na próxima!\n')
            break
        elif number_choice != n and counter != tentativas:
            if counter == 1:
                print('Você errou, vou te dar uma dica!\n')
                if n % 2 == 0:
                    print('O número é par\n')
                else:
                    print('O número é ímpar\n')
            elif counter == 2:
                print('Vou te dar a segunda dica!\n')
                if n >= 10:
                    print('O número é maior ou igual a 10\n')
                else:
                    print('O número é menor que 10\n')
        else:
            print('Você errou seu limitado, se esforce mais e um dia poderá ganhar de mim!\n')
elif dificuldade == 3:
    tentativas = 5
    print(f'O número está entre 1 e 100 e voce tem {tentativas} tentativas!')
    n = random.randint(1, 100)
    while counter < tentativas:
        counter += 1
        number_choice = int(input('Qual foi o número em que pensei?\n'))
        if number_choice == n:
            print('Parabéns, você acertou, mas não vai ser tão fácil na próxima!\n')
            break
        elif number_choice != n and counter != tentativas:
            if counter == 1:
                print('Você errou, vou te dar uma dica!\n')
                if n >= 50:
                    print('O numero é maior ou igual a 50!\n')
                else:
                    print('O numéro é menor que 50!\n')
            elif counter == 2:
                print('Vou te dar a segunda dica!\n')
                if n % 2 == 0:
                    print('O número é par!\n')
                else:
                    print('O número é ímpar!\n')
            elif counter == 3:
                print('Vou te dar a terceira dica!\n')
                if n % 5 == 0:
                    print('O número é um multiplo de 5!\n')
                else:
                    print('O número não é um múltiplo de 5\n')
            elif counter == 4:
                print('Vou te dar a quarta dica!\n')
                print(f'O número está entre {n-5} e {n+5}\n')
        else:
            print('Você errou seu limitado, se esforce mais e um dia poderá ganhar de mim!\n')
elif dificuldade == 4:
    print('Tu é brabo mesmo hein, até o diabo teme medo de você\n')
    tentativas = 10
    print(f'O número está entre 1 e 1000 e voce tem {tentativas} tentativas!\n')
    n = random.randint(1, 1000)
    while counter < tentativas:
        counter += 1
        number_choice = int(input('Qual foi o número em que pensei?\n'))
        if number_choice == n:
            print('Parabéns, você acertou, mas não vai ser tão fácil na próxima!\n')
            break
        elif number_choice != n and counter != tentativas and counter <= 5:
            if counter == 1:
                print('Você errou, vou te dar uma dica!\n')
                if n >= 500:
                    print('O numero é maior ou igual a 500!\n')
                else:
                    print('O numéro é menor que 500!\n')
            elif counter == 2:
                print('Vou te dar a segunda dica!\n')
                if n % 2 == 0:
                    print('O número é par!\n')
                else:
                    print('O número é ímpar!\n')
            elif counter == 3:
                print('Vou te dar a terceira dica!\n')
                if n % 5 == 0:
                    print('O número é um multiplo de 5!\n')
                else:
                    print('O número não é um múltiplo de 5\n')
            elif counter == 4:
                print('Vou te dar a quarta dica!\n')
                print(f'O número está entre {n-100} e {n+100}!\n')
            elif counter == 5:
                print('Vou te dar a quinta e última dica!\n')
                print(f'O número está entre {n-50} e {n+50}, e essa foi a última dica!\n')
        elif number_choice != n and counter != tentativas and counter > 5:
            print('O número nao é esse, digite outro\n')
        else:
            print('Você errou seu limitado, se esforce mais e um dia poderá ganhar de mim!\n')
print('_' * 30, end=' ')
print('Fim do jogo', end=' ')
print('_' * 30)