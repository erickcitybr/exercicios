'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''
from time import sleep

contador_minutos = 0
contador_segundos = 1
resto_arquivo = 0
divisao = 0
contador = 0

print('~' * 80)

while True:

    try:

        tamanho_arquivo = int(input('\033[1;32mQual o tamanho do arquivo (em MB)? \033[m'))
        sleep(1)
        print('~' * 80)
        velocidade_link = int(input('\033[1;32mQual a velocidade do link (em Mbps)? \033[m'))
        print('~' * 80)
        sleep(1)

    except:
        print('\033[1;31mHOUVE UM ERRO! Tente Novamente.\033[m')
        sleep(1)

    else:
        while tamanho_arquivo > velocidade_link:
            tamanho_arquivo = tamanho_arquivo - velocidade_link
            contador_segundos += 1

        if tamanho_arquivo < velocidade_link:
            divisao = tamanho_arquivo / velocidade_link
            resto_arquivo = tamanho_arquivo

        segundos = resto_arquivo + divisao

        if contador_segundos >= 60:
            while contador_segundos >= 60:
                contador_segundos -= 60
                contador_minutos += 1

        if divisao == 0.00:
            print(f'O tempo aproximado de dowload do arquivo usando esse link é {contador_minutos} minuto(s) e\n'
                  f'{contador_segundos} segundo(s) para terminar.')
            sleep(1)

        elif divisao >= 0.01:
            print(f'O tempo aproximado de dowload do arquivo usando esse link é {contador_minutos} minuto(s), \n'
                  f'{contador_segundos} segundo(s) e {divisao:.2f} milissegundo(s) para terminar.')
            sleep(1)
        print('-' * 80)
        opcao = str(input('\033[1;33mQuer continuar? [S/N] \033[m')).strip().upper()
        sleep(1)
        if opcao == 'S':
            print('=-' * 40)
            print(f'\033[1;37m{"Aguarde um instante...":^80}\033[m')
            print('=-' * 40)
            sleep(2)

        elif opcao == 'N':
            print('=-' * 40)
            print(f'\033[1;31m{"Programa sendo encerrado! Até mais.":^80}\033[m')
            print('=-' * 40)
            sleep(2)
            break

        else:
            print('-' * 80)
            print('\033[1;31mHOUVE UM ERRO! Reiniciei o programa.\033[m')
            print('-' * 80)
            sleep(1)
