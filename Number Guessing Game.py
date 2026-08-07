import random

def GameFunction(startingValue,endingValue):

    attempts = 0

    key=random.randint(startingValue,endingValue)

    while True:
        try:    
            n=int(input("Enter the guess (press -1 for Main Menu): "))
        except ValueError:
            print("Enter the valid input, Returning!")
            return None

        if(n<startingValue or n>endingValue):
            print("Choice not in range try agian! (",startingValue,"-",endingValue,")")
            continue

        attempts+=1

        if(n==-1):
            return None
        
        if(n==key):
            print("Congratulations, You guess the Number!")
            print("Attempts: ",attempts)

            if endingValue==100:
                f=open("highScore.txt","r")
                f.readline()
                f.readline()
                d=int(f.readline())
                f.close()

                if(d<attempts):
                    print("High Score: ",d)
                elif(d>=attempts):
                    print("You Broke the HighScore. New HighScore: ",attempts) 

                    f=open("highScore.txt","r+")
                    f.readline()
                    f.readline()
                    f.write(str(attempts))
                    f.close()
                    

            elif endingValue==50:
                f=open("highScore.txt","r")
                f.readline()
                d=int(f.readline())
                f.close()
                
                if(d<attempts):
                    print("High Score: ",d)
                elif(d>=attempts):
                    print("You Broke the HighScore. New HighScore: ",attempts) 
                
                    f=open("highScore.txt","r+")
                    f.readline()
                    f.write(str(attempts))
                    f.close()  
                    

            elif endingValue==20:
                f=open("highScore.txt","r")
                d=int(f.readline())
                f.close()
                
                if(d<attempts):
                    print("High Score: ",d)
                elif(d>=attempts):
                    print("You Broke the HighScore. New HighScore: ",attempts) 
                
                    f=open("highScore.txt","r+")
                    f.write(str(attempts))
                    f.close()
            return None       

        elif n>key:
            print("Too High")

        elif n<key and n>=startingValue:
            print("Too Low")

           
print("\n------------------")
print("Number Guessing Game")
print("------------------\n")

while True:

    print("Select the Mode\n1.Easy\n2.Medium\n3.Hard\n0.Exit!")

    try:
        choice=int(input("Enter the choice between(0-3): "))
    except ValueError:
        print("Enter the valid value for choice!")
        continue    
    
    if(choice<0 or choice>3):
        print("Choice not in range try agian(0-3)!")
        continue
    
    if(choice==0):
        print("Exiting the program!")
        break


    if(choice==1):
         print("\nGuess Between 0-20\n")
         GameFunction(0,20)
    elif(choice==2):
        print("\nGuess Between 0-50\n")
        GameFunction(0,50)
    elif(choice==3):
        print("\nGuess Between 0-100\n")
        GameFunction(0,100)
    