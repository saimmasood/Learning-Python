
def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
         print("Divded by zero ! Never divide by zero again!")
         return None

    return c

    
def modulus(a,b):
    try:
        c=a%b
    except ZeroDivisionError:
         print("Divded by zero ! Never divide by zero again!")
         return None

    return c

def power(a,b):
    return a**b




while True:

    print("---Calculator---\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\n6.Power")
    print("0.Exit!")

    try:
        choice=int(input("Enter the choice between(0-6): "))
    except ValueError:
         print("Enter the valid value for choice!")
         continue    

    if(choice<0 or choice>6):
            print("Choice not in range try agian(0-6)!")
            continue

    if(choice==0):
         print("Exiting the program!")
         break


    try:
        a=float(input("Enter the number 1 : "))
    except ValueError:
        print("Enter the valid input")
        continue

    try:    
        b=float(input("Enter the number 2 : "))
    except ValueError:
        print("Enter the valid input")
        continue    


    if(choice==1):
         print("Ans : ",addition(a,b))
    elif(choice==2):
         print("Ans : ",subtraction(a,b))
    elif(choice==3):
         print("Ans : ",multiplication(a,b))
    elif(choice==4):
         print("Ans : ",division(a,b))
    elif(choice==5):
         print("Ans : ",modulus(a,b))
    elif(choice==6):
         print("Ans : ",power(a,b))                        


