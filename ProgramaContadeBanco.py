from datetime import datetime

class ContaBancaria:
    saldo = 0
    depositos = []
    saques = []
    saques_diarios = 3
    limite_saque_diario = 500.00

while True:
    print("\nEscolha uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            ContaBancaria.saldo += valor_deposito
            ContaBancaria.depositos.append((valor_deposito, datetime.now()))
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")

    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        if ContaBancaria.saques_diarios > 0 and valor_saque > 0 and ContaBancaria.saldo >= valor_saque and valor_saque <= ContaBancaria.limite_saque_diario:
            ContaBancaria.saldo -= valor_saque
            ContaBancaria.saques.append((valor_saque, datetime.now()))
            ContaBancaria.saques_diarios -= 1
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
        elif ContaBancaria.saques_diarios == 0:
            print("Limite de saques diários atingido.")
        elif valor_saque <= 0:
            print("Valor inválido. O saque deve ser maior que zero.")
        else:
            print("Saldo insuficiente para realizar o saque ou valor acima do limite diário.")

    elif opcao == "3":
        print("\nExtrato:")
        for deposito in ContaBancaria.depositos:
            valor, data_hora = deposito
            print(f"Depósito: R${valor:.2f} - {data_hora.strftime('%d/%m/%Y %H:%M:%S')}")
        for saque in ContaBancaria.saques:
            valor, data_hora = saque
            print(f"Saque: R${valor:.2f} - {data_hora.strftime('%d/%m/%Y %H:%M:%S')}")

        if not ContaBancaria.depositos and not ContaBancaria.saques:
            print("Não foram realizadas movimentações.")
        else:
            print(f"Saldo atual: R${ContaBancaria.saldo:.2f}")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Digite um número válido de 1 a 4.")