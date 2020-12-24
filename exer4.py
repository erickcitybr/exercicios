'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''
from time import sleep
porcentagem_vinte = 20
porcentagem_quinze = 15
porcentagem_dez = 10
porcentagem_cinco = 5
aumento = 0
print(f'\033[1;32m{"-="}\033[m' * 40)
print(f'{"PROGRAMA ABERTO!":^80}')
print(f'\033[1;32m{"-="}\033[m' * 40)
sleep(1)

while True:
    try:
        salario = float(input('Digite o valor do salário: R$'))
        print(f'\033[1;34m{"~"}\033[m' * 80)

    except:
        print(f'\033[1;31m{"-~"}\033[m' * 40)
        print(f'{"ERRO! Tente Novamente.":^80}')
        print(f'\033[1;31m{"-~"}\033[m' * 40)
        sleep(2)
    else:
        if salario < 280:
            aumento = (salario / 100) * porcentagem_vinte
            print(f'O salário antes do reajuste era de R${salario}')
            print(f'O porcentual de aumento aplicado é de {porcentagem_vinte}')
            print(f'O valor do aumento é de R${aumento}')
            print(f'O novo salário, após o aumento é de R${salario + aumento}')

        elif 700 > salario >= 280:
            aumento = (salario / 100) * porcentagem_quinze
            print(f'O salário antes do reajuste era de R${salario}')
            print(f'O porcentual de aumento aplicado é de {porcentagem_quinze}')
            print(f'O valor do aumento é de R${aumento}')
            print(f'O novo salário, após o aumento é de R${salario + aumento}')

        elif 1500 > salario >= 700:
            aumento = (salario / 100) * porcentagem_dez
            print(f'O salário antes do reajuste era de R${salario}')
            print(f'O porcentual de aumento aplicado é de {porcentagem_dez}')
            print(f'O valor do aumento é de R${aumento}')
            print(f'O novo salário, após o aumento é de R${salario + aumento}')

        elif salario >= 1500:
            aumento = (salario / 100) * porcentagem_vinte
            print(f'O salário antes do reajuste era de R${salario}')
            print(f'O porcentual de aumento aplicado é de {porcentagem_cinco}')
            print(f'O valor do aumento é de R${aumento}')
            print(f'O novo salário, após o aumento é de R${salario + aumento}')
        print(f'\033[1;34m{"~"}\033[m' * 80)
        sleep(2)

        opcao = str(input('\033[1;33mQuer continuar? [S/N] \033[m')).strip().upper()
        sleep(1)

        if opcao == 'S':
            print(f'\033[1;37m{"=-"}\033[m' * 40)
            print(f'{"Aguarde um instante...":^80}')
            print(f'\033[1;37m{"=-"}\033[m' * 40)
            sleep(2)

        elif opcao == 'N':
            print(f'\033[1;31m{"=-"}\033[m' * 40)
            print(f'{"Programa sendo encerrado! Até mais.":^80}')
            print(f'\033[1;31m{"=-"}\033[m' * 40)
            sleep(2)
            break

        else:
            print('\033[1;31m-\033[m' * 80)
            print(f'{"HOUVE UM ERRO! Reiniciei o programa.":^80}')
            print('\033[1;31m-\033[m' * 80)
            sleep(1)
