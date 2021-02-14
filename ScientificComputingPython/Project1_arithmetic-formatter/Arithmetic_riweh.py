def arithmetic_arranger(problems, Show=False):
    maxOperand =0 
    operand1Line=""
    operand2Line=""
    answerLine=""
    dashedLine=""
    #assert(len(problems) <= 6), "Error: Too many problems."
    notLastProblems = len(problems) -1
    if(len(problems) <= 5):
      for operation in problems:
          operation = operation.split()
          try:
              operand1 = (operation[0])
              operator = operation[1]
              operand2 = (operation[2])
              if(len(str(operand1)) > 4 or len(str(operand2)) > 4):
                return "Error: Numbers cannot be more than four digits."              
              if(  (operator == '+' ) or (operator == '-')) :
                operand1 = int(operation[0])
                operator = operation[1]
                operand2 = int(operation[2])
              else:
                return "Error: Operator must be '+' or '-'."

              
          except:
              return "Error: Numbers must only contain digits."
          
          #assert(operator == "+" or operator == "-"),"Error: Operator must be '+' or '-'."
          #assert(len(str(operand1)) <= 4 or len(str(operand2)) <= 4 ),"Error: Numbers cannot be more than four digits."
        
          if(operator == '+'):
              ans = operand1 + operand2
          else:
              ans = operand1 - operand2
      
          maxOperand = max( len(str(operand1)), len(str(operand2))) + 2
          operand1Line += str(operand1).rjust(maxOperand) 
          operand2Line += str(operator + ' '+ str(operand2).rjust(maxOperand - 2))
          dashedLine += str("-" * maxOperand)        
          answerLine += str(ans).rjust(maxOperand)
          if notLastProblems > 0:
            fourSpaces = "    "
            operand1Line+= fourSpaces
            operand2Line+= fourSpaces
            dashedLine+=fourSpaces
            answerLine+=fourSpaces
            notLastProblems-=1

          if Show == True:
              arranged_problems = (operand1Line + "\n" + operand2Line + "\n" +dashedLine + "\n" + answerLine )
              print(len(arranged_problems))
          else:
              arranged_problems = (operand1Line + "\n" + operand2Line + "\n" + dashedLine)
    else:
      return "Error: Too many problems."
    return arranged_problems
