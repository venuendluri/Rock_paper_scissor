import random
items=["Rock","Paper","Scissor"]
com=random.choice(items)
c=True
win=0
loose=0
tie=0
while c:
    user = input("Enter your choice: ").capitalize()
    print("Computer Choose: " + com)
    if(user=="Rock" and com=="Scissor"):
        print("You Win")
        win+=1
    elif(user=="Rock" and com=="Paper"):
        print("You lose")
        loose+=1
    elif(user=="Paper" and com=="Scissor"):
        print("You Win")
        win += 1
    elif(user=="Paper" and com=="Rock"):
        print("You lose")
        loose += 1
    elif(user=="Scissor" and com=="Rock"):
        print("You lose")
        loose += 1
    elif(user=="Scissor" and com=="Paper"):
        print("You Won")
        win += 1
    elif((user=="Rock" and com=="Rock")or (user=="Paper" and com=="Paper") or (user=="Scissor" and com=="Scissor")):
        print("It's a tie")
        tie+=1
    else:
        print("Invalid")
    print("wins : ",win)
    print("Lose : ", loose)
    print("tie : ", tie)

    check=input("If you what another game Yes/No: ").capitalize()
    if(check=="Yes"):
        c=True
    else:
        c=False
        print("wins : ", win)
        print("Lose : ", loose)
        print("tie : ", tie)


