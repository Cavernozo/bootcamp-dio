from abc import ABC, ABCMeta, abstractmethod

class cliente:

    def __init__(self, endereco):
        self.endereco = pessoaFisica
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        pass


    #adiciona a conta na lista contas    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
    def __str__(self) -> str:
        return f"{self.endereco}, {self.contas}"
    
class pessoaFisica(cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

#cria uma conta
class conta:

    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico()
        self.numero_saques = 0

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):

        excedeu_saldo = valor > self._saldo

        excedeu_limite = valor > self._limite

        excedeu_saques = self.numero_saques >= self._limite_saque

        if excedeu_saldo or excedeu_limite or excedeu_saques:
            return False 
        
        else:
            self.numero_saques += 1
            self._saldo -= valor
            return True

    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            return False
        
class contacorrente(conta):

    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self._limite = 500
        self._limite_saque = 3


class historico:
    
    def __init__(self):
        self._historico = []

    def adicionar_transacao(self, transacao):
        self._historico.append(transacao)

    def __iter__(self):
        return iter(self._historico)

class transacao(ABC):

    @property
    @abstractmethod
    def registrar(conta):
        pass

class deposito(transacao):

    def deposito(valor, conta):
        transacao = conta.depositar(valor)
        if transacao == True:
            print("Deposito feito com sucesso!")
            deposito.registrar(conta)
        else:
            print("Falha no deposito!")
        
        
    def registrar(conta):
        conta._historico.adicionar_transacao(f"Deposito: R$ {valor:.2f}")


class saque(transacao):
    
    def sacar(valor, conta):
        transacao = conta.sacar(valor)
        if transacao == True:
            print("Saque feito com sucesso!")
            saque.registrar(conta)
        else:
            print("Falha no Saque!")
        
        
    def registrar(conta):
        conta._historico.adicionar_transacao(f"Saque: R$ {valor:.2f}")
        
class verificador_usuarios:
    
    def verificacao_cliente(cpf, lista_clientes):
        for usuario in lista_clientes:
            if cpf == usuario._cpf:
                return usuario
            else:
                return None

    def verificacao_conta(cpf, lista_clientes):
        for usuario in lista_clientes:
            if usuario.contas == None:
                return None
            else:
                for conta in usuario.contas:
                    return conta


lista_clientes = []
while True:
    opcao = input("""
    =====Menu=====
    [C] Novo Cliente
    [N] Nova Conta
    [D] Depositar
    [S] Sacar
    [H] Historico da conta
    [L] Listar Contas
    [Q] Sair
    >>>""").upper()
    match opcao:

        case "C":
            endereco = input("Endereço: ")
            cpf = input("Cpf: ")
            nome = input("Nome: ")
            data = input("Data de nascimento: ")
            usuario = pessoaFisica(endereco, cpf, nome, data)
            n_usuario = verificador_usuarios.verificacao_cliente(usuario._cpf, lista_clientes)
            if n_usuario == None:
                lista_clientes.append(usuario)
            else:
                print("Usuario já existe!")
            
        case "N":
            cpf = input("cpf: ")
            usuario = verificador_usuarios.verificacao_cliente(cpf, lista_clientes)
            if usuario == None:
                print("Usuario não existe!")

            else:
                usuario_conta = contacorrente.nova_conta(usuario._cpf, len(usuario.contas) + 1)
                usuario.adicionar_conta(usuario_conta)

        case "D":
            cpf = input("cpf: ")
            usuario = verificador_usuarios.verificacao_cliente(cpf, lista_clientes)
            if usuario == None:
                print("Usuario não existe!")
            else:
                usuario_conta = verificador_usuarios.verificacao_conta(usuario, lista_clientes)
                if usuario_conta == []:
                    print("Conta não existe!")
                else:
                    valor = float(input("Valor deposito: R$ "))
                    deposito.deposito(valor, usuario_conta) 

        case "S":
            cpf = input("cpf: ")
            usuario = verificador_usuarios.verificacao_cliente(cpf, lista_clientes)
            if usuario == None:
                print("Usuario não existe!")
            else:
                usuario_conta = verificador_usuarios.verificacao_conta(usuario, lista_clientes)
                if usuario_conta == []:
                    print("Conta não existe!")
                else:
                    valor = float(input("Valor saque: R$ "))
                    saque.sacar(valor, usuario_conta) 

        case "H":
            cpf = input("cpf: ")
            usuario = verificador_usuarios.verificacao_cliente(cpf, lista_clientes)
            if usuario == None:
                print("Usuario não existe!")
            else:
                usuario_conta = verificador_usuarios.verificacao_conta(usuario, lista_clientes)
                if usuario_conta == []:
                    print("Conta não existe!")
                else:
                        print("====== Historico ======")
                        for item in usuario_conta._historico:
                            print(f"\n {item}")

        case "L":
            for usuario in lista_clientes:
                for item in usuario.contas:
                    print("=-" * 20)
                    print("Nome: ", usuario._nome)
                    print("Data de nascimento: ", usuario._data_nascimento)
                    print("Agencia: ", item._agencia)
                    print()


        case "Q":
            break

        case _:
            print("Opção não existe!")
