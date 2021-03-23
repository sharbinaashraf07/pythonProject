class Bank:
    accno=""
    name=""
    acctype=""
    bal=""

    def __int__(self,accno,name,acctype,bal):
        self.accno=accno
        self.name=name
        self.acctype=acctype
        self.bal=bal

    def deposit(self,amount):
        self.bal=self.bal+amount
    def withdraw(self,amount):
        self.bal=self.bal-amount

acc1=Bank("ACCNO1","parvathy","savings",10000)
acc2=Bank("ACCNO2","Amritha","current",50000)

acc1.withdraw(5000)
acc2.deposit(5000)
print(acc1.bal)
print(acc2.bal)
