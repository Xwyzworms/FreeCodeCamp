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
def create_spend_chart(categories):
    result = 'Percentage spent by category\n'

    total = sum(x.spent for x in categories)
    percentages = [(x.spent/total)//0.01 for x in categories]
    for x in range(100, -10, -10):
        result = result + str(x).rjust(3, " ") + '|'
        for y in percentages:
            if y >= x:
                result = result + ' o '
            else:
                result = result + '   '
        result = result + ' \n'
    result = result + '    ' + '-'*len(percentages)*3 + '-\n'
    maxLength = max(len(x.name) for x in categories)
    for x in range(maxLength):
        result = result + '    '
        for y in categories:
            if x < len(y.name):
                result = result + ' ' + y.name[x] + ' '
            else:
                result = result + '   '
        result = result + ' \n'
    return result.rstrip() +'  '
