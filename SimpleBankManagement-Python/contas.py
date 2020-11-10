#Classe
class Conta():
    #Funções "Primárias" da Conta
    def __init__(self, limite, saldo):
        self.limite = limite
        self.saldo = saldo + limite

    #Depositar
    def depositar(self, valor_dep):
        if valor_dep > 0:
            self.saldo += valor_dep #Adiciona valor à conta
            return self.saldo

        else:
            print("O valor depositado precisa ser maior que R$00,00.") #Mensagem de erro

    #Sacar
    def sacar(self, valor_saq):
        if valor_saq < self.saldo:
            self.saldo -= valor_saq #Retira valor da conta
            return self.saldo

        else:
            print("Saldo insuficiente.") #Mensagem de erro

    #Visualizar Extrato
    def __str__(self):
        if self.saldo <= 100:
            return "Saldo (Limite): " + str(self.saldo) #Compara saldo e retorna "negativo"

        elif self.saldo > 100:
            return "Saldo (+ Limite): " + str(self.saldo) #Compara saldo e retorna "positivo"

        else:
            return "Ocorreu algum erro..." #Mensagem de erro
