

from os import system
password = "mrr"

flag = True

while flag :
    user_inp = input("password:")
    system("cls")

    if user_inp != password :
        print("error!!!")

    else:
        flag = False

print("hi mohammad")
input()



