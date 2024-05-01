def Menu():
    menu = """
    [u] criar usuario
    [c] criar conta conrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    """

    return menu

def Criar_usuario(usuarios):

    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: [dd-mm-aaa]")
    cpf = input("cpf: ")
    endereço = input("endereço: [logradouro, nro - bairro - cidade/sigla estado]")

    n_usuario = Filtrar_usuario(cpf, usuarios)
    if n_usuario:
        print("Usuario existente!")
    
    else:
        usuarios.append({"nome" : nome, "data_nascimento" : data_nascimento, "cpf": cpf, "endereço" : endereço})
    

def Filtrar_usuario(cpf, usuarios):
    for n_usuario in usuarios:
        if n_usuario["cpf"] == cpf:
            return n_usuario
        else:
            return None


def Criar_conta_corrente(agencia, nro_conta, usuarios):
    cpf = input("Informe o cpf: ")
    usuario = Filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = {"agencia": agencia, "nro_conta": nro_conta , "usuario": usuario}
        return conta
    else:
        print("Usuario não existe!")

def Deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    return saldo, extrato

def Saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        

    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques

def Extrato(saldo,/, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():

    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        print(Menu())

        opcao = input("Selecione opção: ")

        match opcao:

            case "u":  
                Criar_usuario(usuarios)
        
            case "c":
                nro_conta = len(contas) + 1
                conta =Criar_conta_corrente(AGENCIA, nro_conta, usuarios )

                if conta:
                    contas.append(conta)
                
            case "d":
                    valor = float(input("Informe o valor do depósito: "))
                    if valor < 0:
                        print("Operação falhou! O valor informado é inválido.")
                    
                    else:
                        saldo, extrato = Deposito(saldo, valor, extrato)
                        print("Deposito realizado com sucesso!")
                        

            case "s":
                    valor = float(input("Informe o valor do saque: "))

                    if valor < 0:
                        print("Operação falhou! O valor informado é inválido.")
                    
                    else:
                        try:
                            saldo, extrato, numero_saques = Saque(saldo = saldo, valor= valor, extrato= extrato, limite= limite, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES)
                            print("Saque realizado com sucesso!")

                        except:
                            pass
            case "e": 
                    Extrato(saldo, extrato= extrato)

            case "q":
                    break

            case _:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")
main()