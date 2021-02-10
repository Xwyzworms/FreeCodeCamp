import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers ')
  else:  
    listNp = np.array(list).reshape(3,3)
    
    finAns = {}
    props = ["mean","variance","standard deviation", "max","min","sum"]
    for prop in props:
      ansList = []
      if(prop == "mean"):
        ansList.append(np.mean(listNp,axis=0).tolist())
        ansList.append(np.mean(listNp,axis=1).tolist())
        ansList.append(np.mean(list).tolist())
        finAns[prop]= ansList
      elif(prop=="variance"):
        ansList.append(np.var(listNp,axis=0).tolist())
        ansList.append(np.var(listNp,axis=1).tolist())
        ansList.append(np.var(list).tolist())
        finAns[prop]= ansList
      elif(prop=="standard deviation"):
        ansList.append(np.std(listNp,axis=0).tolist())
        ansList.append(np.std(listNp,axis=1).tolist())
        ansList.append(np.std(list).tolist())
        finAns[prop]= ansList
      elif(prop == "max"):
        ansList.append(np.max(listNp,axis=0).tolist())
        ansList.append(np.max(listNp,axis=1).tolist())
        ansList.append(np.max(list).tolist())
        finAns[prop]= ansList
      elif(prop == "min"):
        ansList.append(np.min(listNp,axis=0).tolist())
        ansList.append(np.min(listNp,axis=1).tolist())
        ansList.append(np.min(list).tolist())
        finAns[prop]= ansList
      elif(prop=="sum"):
        ansList.append(np.sum(listNp,axis=0).tolist())
        ansList.append(np.sum(listNp,axis=1).tolist())
        ansList.append(np.sum(list).tolist())
        finAns[prop]= ansList               
    
    
    return finAns