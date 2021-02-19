class Category:

    def __init__(self,name:str):
        self.name = name
        self.ledger = list()

    def deposit(self,amount:float=0.0,description:str = ""):
        theDict = {}
        theDict["amount"] = amount
        theDict['description'] = description
        self.ledger.append(theDict)

    def get_balance(self):
        totalBalance = []
        for i in self.ledger:
            totalBalance.append(i['amount'])
        
        return sum(totalBalance)

    def check_funds(self,amount:float=0.0):

        curBalance = self.get_balance()
        if(curBalance < amount):
            return false
        return True

    def withdraw(self,amount:float=0.0,description:str=""):
        
        if( self.check_funds(amount) == False) :
            return False
        else:
            theDict = {}
            theDict["amount"] = -amount
            theDict["description"] = description
            self.ledger.append(theDict)
            return True

        return False
    def transfer(self,amount:float=0.0,dest:str=""):
        if(self.check_funds(amount)):
            self.withdraw(amount,description="Transfer to "+ dest.name)
            dest.deposit(amount,description="Transfer from" + self.name)
            return True
        return False
    def __str__(self):
        table = self.name.center(30,"*")+"\n"
        for i in self.ledger:
            print(i)
            table +=  f"{i['description'][0:23].ljust(23)}{str(round(i['amount'],2)).rjust(7)}\n"

        table += f"Total: {round(self.get_balance(),2)}"
        return table
ans = Category("baju")
ans.deposit(10000,"Hoyong Deposit")
ans.withdraw(1600,"ngambil duid")

print(ans)

#def create_spend_chart(categories):

