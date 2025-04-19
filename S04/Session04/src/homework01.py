

from os import system
from random import randint
from datetime import datetime

flag = True

while flag :
    user_inp_lvl = int(input(" pick a level from  (4 , 5 , 6 , 7 , 8)   :   "))
    system("cls")
    start_time = datetime.now()


    if user_inp_lvl == 4 :
        pc_rnd = randint(1000, 9999)

    elif user_inp_lvl == 5 :
        pc_rnd = randint(10000, 99999)

    elif user_inp_lvl == 6 :
        pc_rnd = randint(100000, 999999)

    elif user_inp_lvl == 7 :
        pc_rnd = randint(1000000, 9999999)

    elif user_inp_lvl == 8 :
        pc_rnd = randint(10000000, 99999999)

    temp = True

    while temp :
        guess_inp = int(input("guess number :   "))

        if guess_inp < pc_rnd :
            print("its higher")
        
        elif guess_inp > pc_rnd :
            print("its lower")

        elif guess_inp == pc_rnd :
            temp = False
        
    if input("again ?   yes / no    ") == "no" :
        flag = False

print (" ...that was a good game... ")
input()
