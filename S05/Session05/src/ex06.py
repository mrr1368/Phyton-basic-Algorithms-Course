

from os import system

num = int(input("num :"))
system("cls")
row = 1

while row <= num:
    column = 1

    while column <= num:

        if (num - (num//2) + 1) <= row + column <= (num + (num//2) + 1) and \
                - (num//2) <= row - column <= (num//2) :
            print("*", end="")

        else:
            print(" ", end="")

        column += 1
    print()
    row += 1
