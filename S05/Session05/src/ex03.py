

from os import system

num = int(input("num :"))
system("cls")
row = 1

while row <= num:
    column = 1

    while column <= num:

        if column == 1 or row == 1 or column == num or row == num:
            print("*", end="")

        else:
            print(" ", end="")

        column += 1
    print()
    row += 1
