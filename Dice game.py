import random 
print("-----Roll The Dice-----")
while True:     
     print("1. roll the dice \n2. exit " )    
     user = int(input("what you want to do\n"))     
     if user==1:         
        number = random.randint(1,6)         
        print("Great! you got :",number)     
     else:         
        break