#TASK-4 ROCK,SCISSOR,PAPER GAME
#TYPE: 0 for ROCK, 1 for PAPER, 2 for SCISSOR



def con():
    import random
    while True:
        CHOICE=int(input("enter your choice: type 0 for Rock , 1 for Paper, 2 for Scissor: "))
        if(CHOICE>=3 or CHOICE<0):
            print("Enter an Valid Value")
        else:
            c_choice=random.randint(0,2)
            print("computer choice")
            print(c_choice)
            if(c_choice == CHOICE):
                    print("DRAW")
            elif(CHOICE==0 and c_choice==2):
                print("YOU WIN")
            elif(CHOICE==2 and c_choice==0):
                print("YOU LOSE")
            elif(c_choice > CHOICE):
                print("YOU LOSE")
            elif(CHOICE > c_choice):
                print("YOU WIN")


            u=input("Do you want to stop: ")
            if u.casefold()=="yes":
                print("THANK YOU")
                break
            else:
                continue
con()    


    


