import random as rd
ls=[[1,2,3],[4,5,6],[7,8,9]]
ls2=[1,2,3,4,5,6,7,8,9]
print("\n",ls[0],"\n",ls[1],"\n",ls[2])
def plant_bomb():
        place_1=rd.choice(ls2)
        place_2=rd.choice(ls2)
        game(place_1,place_2)
        """if place_1==1 or place_2==1:
            ls[0][0]="bomb"
            
        elif place_1 == 2 or place_2 == 2:
            ls[0][1]="bomb"

        elif place_1 == 3 or place_2==3:
            ls[0][2]="bomb"
            
        elif place_1 == 4 or place_2==4:
            ls[1][0]="bomb"
            
        elif place_1== 5 or place_2==5:
            ls[1][1]="bomb"
            
        elif place_1 == 6 or place_2==6:
            ls[1][2]="bomb"
            
        elif place_1 == 7 or place_2==7:
            ls[1][3]="bomb"
            
        elif place_1 == 8 or place_2==8:
            ls[2][0]="bomb"
            
        elif place_1 == 9 or place_2==9:
            ls[2][1]="bomb"
            
        else:
            print("you choose wrong option\n")"""

    
def game(b1,b2):
    level=input(print("Enter the difficulty level:"))
    if level=='noob':
        i=1
        
        while(i<=3):
            ind=int(input(print("Enter the number where you want to choose")))
            if ind==1 :
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 2:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 3:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 4:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 5:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 6:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 6:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][3]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 7:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 8:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 9:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            else:
                print("you choose wrong option\n")
            i=i+1
        else:
            print("-----------> YOU WON THE MATCH <-----------")
    elif level=='pro':
        i=1
    
        while(i<5):
            ind=int(input(print("Enter the number where you want to choose")))
            if ind==1 :
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 2:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 3:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 4:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 5:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 6:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 6:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][3]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 7:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 8:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 9:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            else:
                print("you choose wrong option\n")
                i=i+1
        else:
                print("-----------> YOU WON THE MATCH <-----------")
    elif level=='god':
        i=0
    
        while(i<2):
            ind=int(input(print("Enter the number where you want to choose")))
            if ind==1 :
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 2:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 3:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[0][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 4:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 5:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 6:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 6:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[1][3]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 7:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][0]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 8:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][1]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            elif ind == 9:
                if ind==b1 or ind==b2:
                    print("---------------> YOU Lose the game <------------")
                    exit(0)
                ls[2][2]="X"
                print("\n",ls[0],"\n",ls[1],"\n",ls[2])
            else:
                print("you choose wrong option\n")
            i=i+1
        else:
            print()
            print("<======//CONGRAGULATION//=======>")
            print("-----------> YOU WON THE MATCH <-----------")
plant_bomb()

print("\n",ls[0],"\n",ls[1],"\n",ls[2])


    