

from os import system

student_list = [
    ["100", "reza", "rajab", "male", 32],
    ["101", "tohid", "rajab", "male", 22],
    ["102", "majid", "rajab", "male", 52],
]

flag = True

while flag :
    system("cls")


    # region menu...

    print("\t\t\twelcom")
    print("------------------------------------------------------")
    print("\n\n1/  add student")
    print("2/  show student ")
    print("3/  exit")
    

    user_inp = int(input("\nmenu : "))
    system("cls")

    # endregion
    
    # region menu = 1 add student

    if user_inp == 1 :

        print("add student")
        print("-------------------")
        # region ncode check
        temp = True
        while temp :  

            ncode = (input("ncode : "))
            system("cls")

            if ncode == "":
                print("ncode is empty")
                input()

            else:

                check_exist = False

                for student in student_list :
                    if student[0] == ncode:
                        check_exist = True

                if check_exist :
                    print(ncode, "exist")

                else:    
                    temp = False

        # endregion

        # region name check

        temp = True
        while temp :  

            name = (input("name : "))
            system("cls")

            if name == "":
                print("name is empty")
                input()

            else:
                temp = False

        # endregion

        # region family check

        temp = True
        while temp :  

            family = (input("family : "))
            system("cls")

            if family == "":
                print("family is empty")
                input()

            else:
                temp = False

        # endregion

        # region gender check

        temp = True
        while temp :  

            gender = (input("gender : "))
            system("cls")

            if gender == "" :
                print("gender is empty")

            elif gender not in ["male", "female", "other"]:
                print("error")
                input()

            else:
                temp = False

        # endregion

        # region age check

        temp = True
        while temp :  

            age = int(input("age : "))
            system("cls")

            if age not in range(1, 151) :
                print("error")
                input()

            else:
                temp = False


        # endregion

        student = [ncode, name, family, gender, age]
        student_list.append(student)
        system("cls")

    # endregion

    # region menu = 2 show student
    elif user_inp == 2 :
                
        print("show student")
        print("--------------------")
        print("\n\nncode\t\tname\t\tfamily\t\tgender\t\tage")
        print("-------------------------------------------------------------------")
        print("\n")

        for student in student_list:
            for item in student:
                print(item, end = "\t\t")
            
            print()
        input()

    # endregion

    # region menu = 3 exit

    elif user_inp == 3 :
        flag = False 

    else:
        print("error")

    # endregion

print("good bye")
input()


 




