# NUMBER GUESS:-

import random

x=random.randint(1,9)

turn=0

while turn<4:
    
    num =int(input("Enter your number"))
    if num==x:
        print("Congrats! You have guessed the right number.",x)
        break
        
    elif num>x:
        if num-x>6:
            print("Hint: You are very far ")
        elif num-x>4:
            print("Hint: You are a little far")
        elif num-x>2:
            print("Hint: You are close")
        else:
            print("Hint: You are very close")
            
    else:
        if x-num>6:
            print("Hint: You are very far ")
        elif x-num>4:
            print("Hint: You are a little far")
        elif x-num>2:
            print("Hint: You are close")
        else:
            print("Hint: You are very close")
            
    turn += 1

if turn>=4:
    print("Sorry, you lost!")
    
        
            

 