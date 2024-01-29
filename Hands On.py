menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float (input("Informe o valor do depósito:"))

        if  valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor :.2F}\n"

        else:
            print("Oeração falhou! o valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        execedeu_saldo = valor >saldo
        execedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif execedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saque excedido.")
        elif valor > 0: 
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "e":
        print("\n==========EXTRATO==========")
        print("Não foi realizado movimentaçães."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")
    elif opcao == "q":S
        break 
 
    else:
        print(" Operação Inválida, por favor selecione novamente a operação desejada.") 

