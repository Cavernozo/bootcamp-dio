menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 

'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DIARIO = 3

while True:
    opçao = input(menu)

    if opçao == "d":
        deposito = int(input("Valor de deposito: "))
        if deposito < 0:
            print("Erro")
        else:
            saldo += deposito
            extrato += f"deposito: R${deposito:.2f}\n"
        
    
    elif opçao == "s":
        saque = int(input("Valor de saque: "))
        if numero_saques == LIMITE_DIARIO:
            print("Limite de saques diario atingido.")

        elif saque > limite:
            print("Valor maior do que o limite permitido.")

        elif saque > saldo:
            print("Valor indisponivel.")

        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"saque: R${saque:.2f}\n"

    elif opçao == "e":
        print("=====Extrato=====")
        print("Não foram ralizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: {saldo:.2f}")
        print("=======================")
        

    elif opçao == "q":
        break

    else:
        print("Opreçâo invalida, por favor selecione novamente a operaçâo desejada.")

print(menu)