class Banco():
    def __init__(self, nome, numero, tipo):
        self.nome=nome
        self.numero=numero
        self.tipo=tipo
        self.status=False
        self.saldo=0.0

    def contaAtivar(self):
        if self.status == False:
            print("Conta ativada com sucesso!")
            self.status=True
        else:
            print("Conta já foi Ativada!")

    def contaDesativar(self):
        if self.status == True:
            if self.saldo==0:
                print("Conta desativada com sucesso")
                self.status=False
            else:
                print("Existe saldo na conta, retire os valores!")
        else:
            print("Conta já foi desativada!")
    def depositar(self,valordeposito):
        if self.status == True:
            self.saldo+=valordeposito
            print(f"Deposito efetuado, seu novo saldo {self.saldo}!")
        else:
            print("Conta inativa!")

    def sacar(self, valorsaque):
        if self.status == True:
            if self.saldo >= valorsaque:
                self.saldo-=valorsaque
                print(f"Saque efetuado, seu novo saldo {self.saldo}")
            else:
                print("Saldo insuficinte!")
        else:
            print("Conta inativa!")

    def saldoverificar(self):
        if self.status ==True:
            print(f"Seu saldo atual {self.saldo}")
        else:
            print("Conta inativa!")

c1 = Banco("joão",1234,"Conta Corrente")

c1.contaAtivar()
c1.contaAtivar()
c1.saldoverificar()
c1.depositar(11)
c1.saldoverificar()
c1.sacar(10)
c1.contaDesativar()
c1.sacar(1)
c1.contaDesativar()
c1.contaDesativar()
