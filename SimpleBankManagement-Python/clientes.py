#Classe
class Cliente():
    #Funções "Primárias" do Cliente
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    #Visualizar Dados Pessoais
    def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + self.idade
        