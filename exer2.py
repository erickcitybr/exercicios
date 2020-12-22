''' Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e
o preço total. '''
import time

litro = 0
contador_de_litros = 0
contador_de_latas = 0
preco = 80

print('=-' * 40)
print(f'\033[1;35m{"Programa Iniciado":^80}\033[m')
print('=-' * 40)
time.sleep(1)

while True:
    try:
        area_pintar = float(input('Digite quantos m² serão a área a ser pintada: '))

    except:
        print('\033[1;31mDigite Apenas números\033[m')

    else:
        print('-' * 80)
        print(f'\033[1;36m{"Fazendo os Cálculos...":^80}\033[m')
        print('-' * 80)
        time.sleep(1)

        while True:
            if litro <= area_pintar:
                litro += 3
                contador_de_litros += 1
            else:
                break

        contador_de_latas = contador_de_litros / 18
        time.sleep(1)

        print(f'Quantidade de lata(s) de tinta a serem usada(s) são ', end='')
        if contador_de_latas < 1:
            print('aproximadamente 1.')
        else:
            print(f'{int(contador_de_latas)}.')
        print(f'O preço total delas são ', end='')
        if contador_de_latas < 1:
            print('R$ 80.00.')
        else:
            print(f'R$ {preco * int(contador_de_latas):.2f}.')
        print('-' * 80)
        time.sleep(1)
        if 1 < contador_de_latas > int(contador_de_latas):
            print('~' * 80)
            print(f'\033[1;41m{"OBSERVAÇÃO":^80}\033[m')
            print('-' * 80)
            print('\033[1;33mMas recomendamos que compre mais uma lata de tinta para garantir que não falte,\033[m\n'
                  f'\033[1;33mpois a {contador_de_latas:.2f} não é um número inteiro.\033[m')
            print(f'\033[1;33mCaso siga a recomendação, a quantidade de lata(s) de tinta a serem usada é\033[m'
                  f'\033[1;33m {int(contador_de_latas+ 1)}.\033[m')
            print(f'\033[1;33mE o preço será R${preco * int(contador_de_latas+1)}\033[m')
            print('~' * 80)

        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
        print(litro, contador_de_litros, contador_de_latas, preco)
        if opcao == 'S':
            print('=-' * 40)
            print(f'\033[1;37m{"Aguarde um instante...":^80}\033[m')
            print('=-' * 40)
            litro = 0
            contador_de_litros = 0
            contador_de_latas = 0
            preco = 80
            time.sleep(2)
        elif opcao == 'N':
            print('=-' * 40)
            print(f'\033[1;31m{"Programa sendo encerrado! Até mais.":^80}\033[m')
            print('=-' * 40)
            time.sleep(3)
            break
        else:
            print('-' * 80)
            print('\033[1;31mHOUVE UM ERRO! Reiniciei o programa.\033[m')
            print('-' * 80)
