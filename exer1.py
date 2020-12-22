import time

while True:

    try:
        print('-' * 40)
        print(f'\033[1;32m{"Inciando o programa...":^40}\033[m')
        print('-' * 40)
        time.sleep(1)
        salario_bruto = float(input('Digite o salário bruto: R$ '))

    except:
        print('\033[31mERRO!\033[m Tente novamente com atenção')

    else:
        print('-' * 40)
        print(f'\033[1;31m{"Calculando os descontos":^40}\033[m')
        print('-' * 40)

        time.sleep(1)

        imposto_de_renda = (salario_bruto/100) * 11
        print(f'\033[33m- Imposto de renda (11%):\033[m \033[31mR$ {imposto_de_renda:.2f}\033[m')
        time.sleep(1)

        inss = (salario_bruto/100) * 8
        print(f'\033[33m- INSS (8%):\033[m \033[31mR$ {inss:.2f}\033[m')
        time.sleep(1)

        sindicato = (salario_bruto/100) * 5
        print(f'\033[33m- Sindicato (5%):\033[m \033[31mR$ {sindicato:.2f}\033[m')
        time.sleep(1)

        total_descontos = imposto_de_renda + inss + sindicato
        print(f'O total de descontos calculado em cima \ndo seu salário é de \033[31mR$ {total_descontos:.2f}\033[m')

        print('-' * 40)
        print(f'\033[1;34m{"Resultado Final":^40}\033[m')
        print('-' * 40)

        salario_liquido = salario_bruto - total_descontos
        time.sleep(1)
        print(f'\033[32mR$ {salario_bruto:.2f}\033[m - \033[31mR$ {total_descontos:.2f}\033[m')
        time.sleep(1)

        print(f'\033[32mSalário Líquido: R$ {salario_liquido:.2f}\033[m')

        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()

        if opcao == 'N':
            print('-' * 40)
            print(f'\033[1;37m{"Programa sendo fechado... Até Logo! :)":^40}\033[m')
            print('-' * 40)
            time.sleep(2)
            break

        elif opcao == 'S':
            print('-' * 40)
            print(f'\033[1;36m{"Ajustando para iniciar novamente...":^40}\033[m')
            print('-' * 40)
            time.sleep(2)

        elif opcao != 'SN':
            print('\033[1;31mERRO! Opção inválida. Reinicie o Programa!\033[m')
            break

