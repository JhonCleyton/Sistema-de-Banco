from datetime import datetime
now = datetime.now()
# tem que formatar a hora para não mostrar vairos centesimos.
formatted_datetime = now.strftime("%d/%m/%y %H:%M:%S")
##comecei criando uma conta, não faz sentido adcionar ou sacar valores de uma conta inexistente
def menu():
    menu = """\n
    ----------------- MENU ----------------
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Novo usuário
    [5]Nova conta
    [6]Listar contas
    [0]Sair
    -----------------------------------------
    """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n Digito inválido, verifique e tente novamente.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nSaque não realizado! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação inválida! Valor inserido maior que o permitido.")

    elif excedeu_saques:
        print("\nSaque não concluido! Você exedeu seu limite diario.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t-R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("\n digito inválido, verifique e tente novamente.")

    return saldo, extrato



def criar_usuario(clientes):
    cpf = input("Digite seu CPF: ")
    while not cpf.isdigit():
     cpf = input("Entrada inválida. Digite apenas números por favor: ")
    usuario = buscar_cliente(cpf, clientes)

    if usuario:
        print("\nCPF já cadastrado!")
        return

    nome = input("Insira seu nome completo: ")
    data_nascimento = input("Qual a sua data de Nascimento? (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, Nº, Bairro,  Cidade/UF ): ")
    
                 
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def exibir_extrato(saldo, /, *, extrato):
        print(formatted_datetime)           
        print("\n********************** EXTRATO *************************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n_____________________ BANCO DIO __________________________")
        print("**Qualquer irregularidade constatada procure o seu gerente")


def buscar_cliente(cpf, clientes):
    Clientes_filtrados = [Clientes for Clientes in clientes if Clientes["cpf"] == cpf]
    return Clientes_filtrados[0] if Clientes_filtrados else None


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do usuário: ")
    usuario = buscar_cliente(cpf, clientes)

    if usuario:
        print("\n\033[1mConta Criada com Sucesso.\033[0m")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Essa conta não existe")
    



def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Ag:{conta['agencia']}
            C/C: {conta['numero_conta']}
            Cliente:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 1500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    

    print("\033[1mSeja Bem Vindo ao Nosso Banco.\033[0m")
    print("Vamos pedir seu CPF para verificação.")
    print("caso não seja nosso cliente, um novo cadastro será criado para você!\n")
    print("Em seguida crie uma nova conta.\n")

    criar_usuario(usuarios)
    numero_conta = len(contas) + 1
    conta = criar_conta(AGENCIA, numero_conta, usuarios)

    print("\nFaça um Depósito para Validar a sua Conta.\n")

    valor = float(input("Informe o valor do depósito: "))

    saldo, extrato = depositar(saldo, valor, extrato)
        

  
    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 2
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
             print("Obrigado por usar nosso sistema bancário.Tenha um Exelente dia!")
             break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
