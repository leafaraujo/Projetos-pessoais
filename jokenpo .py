from random import choice
from time import sleep
print('=' * 36)
print('JO-KEN-PO')
print('=' * 36)
jogar = input('Olá vamos brincar de Jokenpo? Digite "S" para sim e "N" para não :D')
if jogar.lower() == 's':
    print('Coloque a sua escolha após o "PO!"\n' 'Pedra, papel ou tesoura!')
    contador = int(input('Quantas vezes você quer jogar?'))
    empates = []
    vitorias = []
    derrotas = []
    for i in range(contador):
        print('JO!')
        sleep(1)
        print('KEN!')
        sleep(1)
        print('PO!')
        escolha = input('')
        escolha_pc = choice(['pedra', 'papel', 'tesoura'])
        print(escolha_pc)
        if escolha.lower() == escolha_pc:
            print('Deu empate')
            empates.append('1')
        elif escolha.lower() == 'pedra' and escolha_pc == 'papel':
            print('Eu ganhei essa! XD')
            derrotas.append('1')
        elif escolha.lower() == 'tesoura' and escolha_pc == 'pedra':
            print('Eu ganhei essa! XD')
            derrotas.append('1')
        elif escolha.lower() == 'papel' and escolha_pc == 'tesoura':
            print('Eu ganhei essa! XD')
            derrotas.append('1')
        else:
            print('Você ganhou essa!')
            vitorias.append('1')
    print(f'Terminamos por aqui! com um total de {contador} partidas, com você tendo ganho {len(vitorias)}, eu tendo'
          f' ganho {len(derrotas)}, e termos empatado {len(empates)} vezes!\n')
    print('Até a próxima, camarada!')
elif jogar.lower() == 'n':
    print('Que pena, espero que se prepare pra quando eu roubar seu emprego!')
