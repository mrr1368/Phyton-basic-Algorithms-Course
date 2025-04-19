

from os import system

num = int(input(" num :"))
system("cls")

row = 1

while row <= num :
    column = 1

    while column <= num :
        print("*", end = "")
        column += 1
    
    print()
    row += 1
