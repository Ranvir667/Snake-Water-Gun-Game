import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = int(input("Enter your choice:"))
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr]

print(f"You chose {youDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer ==you):
    print("Its a draw")
'''
else:
    if(computer ==-1 and you ==1):
        print("you win!")

    elif(computer ==-1 and you ==0):
        print("You lose!")

    elif(computer ==1 and you ==-1):
        print("You lose!")

    elif(computer ==1 and you ==0):
        print("You win!")

    elif(computer ==1 and you ==-1):
        print("you win!")

    elif(computer ==1 and you ==0):
        print("You lose!" )

    else:
        print("something went wrong")
'''

if((computer - you) ==-1 or (computer-you) ==2 ):
    print("You lose!")
          
else:
     print("You win!")
          
