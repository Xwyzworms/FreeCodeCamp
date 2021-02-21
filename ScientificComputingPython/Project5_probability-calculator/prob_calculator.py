import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        temp = ""
        for color,total in kwargs.items():
            temp += (color + " ")*total
        
        self.contents = temp.strip().split(" ")

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        randomChoice = list()
        for i in range(num_balls):
            deleteTheBall = random.choice(self.contents)
            self.contents.remove(deleteTheBall)
            randomChoice.append(deleteTheBall)
        
        return randomChoice
            
      

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    solve = 0
    for i in range(num_experiments):
        cp_hat = copy.deepcopy(hat)
        ans  = []
        luck = cp_hat.draw(num_balls_drawn)

        for color,tot in expected_balls.items():
            if(luck.count(color) >= tot):
                ans.append(True)
            else:
                ans.append(False)

        if False not in ans:
            solve +=1

    return solve / num_experiments

    