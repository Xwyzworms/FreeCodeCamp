from itertools import zip_longest 
class Category:

    def __init__(self,name:str):
        self.name = name
        self.ledger = list()

    def deposit(self,amount,description:str = ""):
        theDict = {}
        theDict["amount"] = amount
        theDict['description'] = description
        self.ledger.append(theDict)

    def get_balance(self):
        totalBalance = []
        for i in self.ledger:
            totalBalance.append(i['amount'])
        
        return sum(totalBalance)

    def check_funds(self,amount):

        curBalance = self.get_balance()
        if(curBalance < amount):
            return False
        return True

    def withdraw(self,amount,description:str=""):
        
        if( self.check_funds(amount) == False) :
            return False
        else:
            theDict = {}
            theDict["amount"] = -amount
            theDict["description"] = description
            self.ledger.append(theDict)
            return True

        return False
    def transfer(self,amount,dest:str=""):
        if(self.check_funds(amount)):
            self.withdraw(amount,description="Transfer to "+ dest.name)
            dest.deposit(amount,description="Transfer from " + self.name)
            return True
        return False
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output
def create_spend_chart(categories):

    names = []
    spend = []
    totals = []

    def is_column_one(row):
        return row * 10 <= percents[0] <= row * 10 + 10

    def is_column_two(row):
        return row * 10 <= percents[1] <= row * 10 + 10

    def is_column_three(row):
        return row * 10 <= percents[2] <= row * 10 + 10

    for category in categories:
        names.append(list(category.name))
        spend.append(
            list((filter(lambda t: t["amount"] < 0, category.ledger))))

    for withdrawal in spend:

        totals.append(sum(t["amount"] for t in withdrawal))
    percents = list(map(lambda x: int((x / sum(totals)) * 100), totals))
    bar_chart = "Percentage spent by category\n"
    x_axis = " " * 4 + ("-" * 10) + "\n"
    coloumn1 = " "
    coloumn2 = " "
    coloumn3 = " "


    for i in range(10, -1, -1):
        if i == 0:
            bar_chart += "  0| o  o  o  " + "\n"
        elif i == 10:
            bar_chart += f"{i}0| {' '}  {' '}  {' '}  " + "\n"
        else:
            if is_column_one(i):
              coloumn1 = "o"
            elif is_column_two(i):
              coloumn2 = "o"
            elif is_column_three(i):
              coloumn3 = "o"
            bar_chart += f" {i}0| {coloumn1}  {coloumn2}  {coloumn3}  " + "\n"

    label = ""

    for row in list(zip_longest(names[0],names[1],names[2])):
      temp = ""
      for ans in row:
        if ans == None:
          temp += "   "
        else:
          temp += "  " + ans

      label += f"   {temp}  " + "\n"

    return bar_chart + x_axis + label[0:len(label)-1]
