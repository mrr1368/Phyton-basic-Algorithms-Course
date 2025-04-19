

from datetime import datetime
from os import system
from random import randint

flag = True

while flag :
    system("cls")
    start_time = datetime.now()
    counter = 0
    rnd_num = randint(1, 7)

    #region word
    if rnd_num == 1 :
        pc_word = "hi"

    elif rnd_num == 2 :
        pc_word = "by"

    elif rnd_num == 3 :
        pc_word = "hello"

    elif rnd_num == 4 :
        pc_word = "goodby"

    elif rnd_num == 5 :
        pc_word = "my"

    elif rnd_num == 6 :
        pc_word = "frind"

    #endregion

    temp = True

    while temp :
        user_inp = input("\n\nguess what ?   (hi , by , hello , goodby , my , frind)   :   ")
        system("cls")

        if  user_inp == pc_word :
            temp = False
        
        else :
            print("wrong !!!")
            counter += 1

    print(" you win !!!!")
    print("time :", datetime.now() - start_time)
    print("round : ", counter)




    if input("continue?    yes / no ") == "no" :
        flag = False

