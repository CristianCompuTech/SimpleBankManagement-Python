#Importação de Classes
from clientes import Cliente #Importa "Cliente" do arquivo "clientes.py"
from contas import Conta #Importa "Conta" do arquivo "contas.py"
import time #Importa biblioteca de controle de tempo

#Input: Adicionar Contas?
print("")
add_conta = input("Deseja adicionar uma conta? S/n: ")

#Input: Dados Cliente
print("")
dados_cliente = print("Digite seus dados (Nome, CPF, Idade): ")
nome = input("Nome: ")
cpf = input("CPF: ")
idade = input("Idade: ")

#Variável "Cliente"
cliente1 = Cliente(nome, cpf, idade)

#Input: Dados Conta
print("")
dados_conta = print("Digite os dados da sua conta (Saldo): ")
limite = 100 #Limite da conta
saldo = int(input("Saldo: ")) #Saldo da conta

#Variável "Conta"
conta1 = Conta(limite, saldo)

#Cria o Cliente e Conta (ou passa direto para o menu)
if add_conta == "S":
    cliente1 = Cliente(nome, cpf, idade) #Adiciona dados ao "Cliente"
    conta1 = Conta(limite, saldo) #Adiciona dados à "Conta"

    time.sleep(0.5)
    print("")
    print("Carregando Menu...") #Carrega o Menu

else:
    time.sleep(0.5)
    print("")
    print("Carregando Menu...") #Carrega o Menu

while True:
    #Menu de escolha de ação
    time.sleep(0.5)
    def menu():
        print("")
        print("1 - Saque", "\n2 - Depósito", "\n3 - Extrato", "\n4 - Sair") #Opções de escolha
        escolha_menu = input() #Escolha
        return(escolha_menu)

    escolha_menu = menu()

    #Sistema de Saque
    if escolha_menu == "1":
        try:
            time.sleep(0.5)
            print("")
            valor_saq = int(input("Quanto deseja sacar? ")) #Valor de saque desejado
            conta1.sacar(valor_saq) #Chama a função de sacar
            
        except Exception as error_saq:
            time.sleep(0.5)
            print("")
            print("Aconteceu algum erro...", error_saq) #Aponta o erro e passa

    #Sistema de Depósito
    elif escolha_menu == "2":
        try:
            time.sleep(0.5)
            print("")
            valor_dep = int(input("Quanto deseja depositar? ")) #Valor de depósito desejado
            conta1.depositar(valor_dep) #Chama a função de depositar

        except Exception as error_dep:
            time.sleep(0.5)
            print("")
            print("Aconteceu algum erro...", error_dep) #Aponta o erro e passa

    #Sistema de Extrato
    elif escolha_menu == "3":
        try:
            time.sleep(0.5)
            print("")
            print(cliente1) #Mostra os dados do cliente
            print("")
            print(conta1) #Mostra os dados da conta

        except Exception as error_ext:
            time.sleep(0.5)
            print("")
            print("Aconteceu algum erro...", error_ext) #Aponta o erro e passa

    #Sistema de Sair do Programa
    elif escolha_menu == "4":
        time.sleep(0.5)
        print("")
        print("Saindo do Programa...")
        break #Para o loop e fecha o programa

    #Resposta inválida
    else:
        time.sleep(0.5)
        print("")
        print("Resposta inválida...") #Aponta resposta inválida e reinicia o Menu
    
