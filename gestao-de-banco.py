from time import sleep #Importa função "Sleep" da biblioteca de tempo

cliente = {} #Dados pessoais do cliente
conta = {} #Dados bancários do cliente

print("-------- BankManagement --------")

add_conta = str(input("\nDeseja adicionar uma conta? S/n: ")).upper().strip()[0]
sleep(1)

#Adiciona os dados do cliente
if add_conta == "S":
    print("\nDigite seus dados pessoais: ")
    cliente["nome"] = str(input("Nome: ")).strip()
    cliente["cpf"] = int(input("CPF: "))
    cliente["idade"] = int(input("Idade: "))

    sleep(0.5)

    print("\nDigite o saldo da sua conta: ")
    conta["saldo"] = int(input("Saldo: ")) + 100

    sleep(1)

    print("\nConta adicionada com sucesso!")

    sleep(0.5)

    print("Carregando Menu...")

    sleep(1)

    #Menu principal de transações
    while True:
        print("\n=====================")
        print("1 = Sacar \n2 = Depositar \n3 = Extrato \n4 = Sair")
        print("=====================")

        opcao_menu = str(input("O que você deseja fazer? ")).upper()[0]

        sleep(1)

        #"Função" de sacar
        if opcao_menu == "1":
            quant_saq = float(input("\nQuanto vocẽ deseja sacar? R$"))

            sleep(0.5)

            if conta["saldo"] > quant_saq:
                conta["saldo"] -= quant_saq
                print(f"Você sacou R${quant_saq:.2f}")

                sleep(1)

            elif conta["saldo"] < quant_saq:
                print("Saldo insuficiente.")

                sleep(1)

        #"Função" de depositar
        elif opcao_menu == "2":
            quant_dep = float(input("\nQuanto vocẽ deseja depositar? R$"))

            sleep(0.5)

            if quant_dep > 0.00:
                conta["saldo"] += quant_dep
                print(f"Você depositou R${quant_dep:.2f}")

                sleep(1)

            elif quant_dep < 0.00:
                print("O valor de depósito precisa ser maior que R$0,00")

                sleep(1)

        #"Função" de extrato bancário
        elif opcao_menu == "3":
            print(f"\nNome: {cliente['nome']} \nIdade: {cliente['idade']} \nCPF: {str(cliente['cpf'])[0:3]}*******")

            sleep(0.5)

            if conta["saldo"] > 100:
                print(f"\nSaldo: {conta['saldo']:.2f}")
                
            elif conta["saldo"] <= 100:
                print(f"\nSaldo: -{100 - conta['saldo']:.2f}")

            sleep(1)

        #Sair do programa
        elif opcao_menu == "4":
            sleep(1)

            print("\nSaindo do programa...")
            break

        #Repete o menu caso o input do usuário seja inválido
        else:
            sleep(0.5)

            print("\nERRO! Digite apenas '1', '2', '3' ou '4'.")
            continue

#Não adiciona os dados do cliente
elif add_conta == "N":
    sleep(1)

    print("\nSaindo do programa...")
