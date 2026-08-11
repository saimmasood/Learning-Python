import random


numbers="0123456789"
upperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase="abcdefghijklmnopqrstuvwxyz"
symbols="!@#$%^&*()_"


while True:
    try:
        length=int(input("Enter the length of Password(>=8)"))
    except ValueError:
        print("Enter valid value (numbers only)")
        continue

    if(length<8):
        print("Length too short.Enter length >=8")
        continue
    break

while True:
    print("Do you want to Include:")

    upper =input("Upper Case Letters (y/n):")
    lower =input("Lower Case Letters (y/n):")
    sym =input("Symbols (y/n):")
    num =input("Numbers (y/n):")    

    if upper not in ["y", "n"] or lower not in ["y", "n"] or sym not in ["y", "n"] or num not in ["y", "n"]:
        print("Enter n/y for the choices!")
        continue  

    if(upper=="n" and lower=="n" and sym=="n" and num=="n"):
        print("Select at least one!")
        continue

    break

all_characters = ""

if upper == "y":
    all_characters += upperCase
if lower == "y":
    all_characters += lowerCase
if sym == "y":
    all_characters += symbols
if num == "y":
    all_characters += numbers


password=""

for i in range(0,length):
    password +=random.choice(all_characters)

print("This is Your final Password: ",password)
