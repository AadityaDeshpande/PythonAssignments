class BankAccount:
    def __init__(self):
        self.amount = 50000

    def ShowBalance(self):
        return self.amount

    def Deposit(self,dep):
        self.amount = self.amount + dep
        return self.amount

    def WithDrawl(self,wd):
        if self.amount > wd :
            self.amount -= wd
            return self.amount
        else:
            return "In Sufficient amount"


if __name__ == '__main__':
    BankObj = BankAccount()
    print( BankObj.ShowBalance())
    print( BankObj.Deposit(50000))
    print( BankObj.ShowBalance())
    print( BankObj.WithDrawl(99999))
    print( BankObj.ShowBalance())
    print( BankObj.WithDrawl(100000))
    print( BankObj.ShowBalance())
    
            
