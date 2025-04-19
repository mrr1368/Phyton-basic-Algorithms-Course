

from random import randint
from os import system
from datetime import datetime

user_score = 0
pc_score = 0
counter = 0
start_time = datetime.now()

# while counter == 10 :
while user_score != 3 and pc_score != 3 :
    user_inp = int(input("\n\n1/rock  2/paper 3/scissirs :"))
    pc_inp = randint(1, 3)
    counter += 1
    system ("cls")

    #region CHECKSCORE

    if (user_inp == 1 and pc_inp == 3) or \
            (user_inp == 2 and pc_inp == 1) or \
            (user_inp == 3 and pc_inp == 2) :
        
         user_score += 1
        
    elif (pc_inp == 1 and user_inp == 3) or \
            (pc_inp == 2 and user_inp == 1) or \
            (pc_inp == 3 and user_inp == 2) :
        
         pc_score += 1
    
    #endregion
    
    #region showinfo
    if user_inp == 1 :
        print("user : rock ", end = " - ")
    
    elif user_inp == 2 :
        print("user : paper ", end = " - ")
    
    else :
        print("user : scissore ", end = " - ")

    
    if pc_inp == 1 :
        print("pc : rock ")
    
    elif pc_inp == 2 :
        print("pc : paper ")
    
    else :
        print("pc : scissore ")

    print("user score:", user_score, ", pc score :", pc_score )

    #endregion

if user_score == 3 :             #if user_score > pc_score :
    print("user win")            #   print("user win")
                                 #if user_score > pc_score :
else:                            #   print("pc win") 
    print("pc win")              #else ("  :(   ")

print("counter :", counter)      
print("time", datetime.now()-start_time)

input()



# -----------------------------------------------------------------

from os import system
from random import randint
from datetime import datetime



flag = True

while flag :
    system("cls")
    user_score = 0
    pc_score = 0
    counter = 0
    start_time = datetime.now()


    while user_score != 3 and pc_score != 3 :
        system("cls")
        
        user_inp = int(input("\n\n1\ rock    2\ paper   3\ sissores  :   "))
        pc_inp = randint(1, 3)
        
        # region score

        if (user_inp ==1 and pc_inp == 3) or \
                (user_inp ==2 and pc_inp == 1) or \
                (user_inp ==3 and pc_inp == 2) :
            user_score += 1

        elif (pc_inp ==1 and user_inp == 3) or \
                (pc_inp ==2 and user_inp == 1) or \
                (pc_inp ==3 and user_inp == 2) :
            pc_score += 1

        # endregion

        # region show info

        if user_inp == 1 :
            print("user : rock", end = "  ---  ")

        elif user_inp == 2 :
            print("user : paper",  end = "  ---  ")
 
        elif user_inp == 3 :
            print("user : sissores",  end = "  ---  ")


        if pc_inp == 1 :
            print("pc : rock", )

        elif pc_inp == 2 :
            print("pc : paper", )
 
        elif pc_inp == 3 :
            print("pc : sissores", )

        print("user score : " , user_score, end = "   ---   ")
        print("pc score : " , pc_score,)
        counter += 1
        input()

        # endregion
        




        
    if user_score == 3 :
        print("user win ")
    else :
        print("pc win")




    print("count :", counter)
    print("time :", datetime.now() - start_time)
    if input("\n\ncontinue ?  yes/no ") == "no" :
        flag = False

input()



