

from os import system

student_list = [
    [" reza", "rajabali", 34, "male", "a", "00115", "88024", 95, 95, 95, 95],
    ["tohid", "rajabali", 22, "male", "b", "00215", "88025", 90, 100, 95, 95],
    ["javad", "shokri", 30, "male", "c", "00315", "88026", 90, 90, 90, 90]
]

flag = True

while flag:

    system("cls")

    # region Menu ...

    print("\t\tStudent Management")
    print("--------------------------------------------------")

    print("\n\n 1\ Add Student")
    print(" 2\ Show Student")
    print(" 3\ Search Student")
    print(" 4\ Remove Student")
    print(" 5\ Edit Student")
    print(" 6\ Best Student")
    print(" 7\ Best Score")
    print(" 8\ Exit")

    menu = input("\n\nMenu : ")
    system("cls")

    # endregion

    # region Menu 1 =  Add Student ...

    if menu == "1":

        # region Show Menu

        print("\t\tAdd Student")
        print("--------------------------------------------------")
        print("\n\nName :")
        print("Family :")
        print("Age :")
        print("Gender :")
        print("Class :")
        print("National Code :")
        print("Student id :")
        print("Csharp :")
        print("Java :")
        print("Python :")
        print("Php :")
        input()

        # endregion

        # region Check Name

        temp = True

        while temp:
            system("cls")

            name = input("\n\nName : ")

            if name == "":

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        # region Check Family

        temp = True

        while temp:
            system("cls")

            family = input("\n\nFamily : ")

            if family == "":

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        # region Check Age

        temp = True

        while temp:
            system("cls")

            age = int(input("\n\nAge : "))

            if age not in range(1, 121):

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        # region Check Gender

        temp = True

        while temp:
            system("cls")

            gender = input("\n\nGender (male, female, other) : ")

            if gender == "":

                print("Error!!!")
                input()

            elif gender not in ("male", "female", "other"):

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        # region Check Class

        temp = True

        while temp:
            system("cls")

            class_ = input("\n\nClass  (a,b,c) : ")

            if class_ == "":

                print("Error!!!")
                input()

            elif class_ not in ("a", "b", "c"):

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        # region Check National Code

        temp = True

        while temp:
            system("cls")

            national_code = input("\n\nNational Code : ")

            if national_code == "":

                print("Error!!!")
                input()

            else:

                check_exist = False
                for student in student_list:
                    if student[5] == national_code:

                        check_exist = True

                if check_exist:
                    print("This National Code Exist")
                    input()

                else:

                    temp = False

        # endregion

        # region Check Std_Id

        temp = True

        while temp:
            system("cls")

            student_id = input("\n\nStudent id : ")

            if student_id == "":

                print("Error!!!")
                input()

            else:

                check_exist = False
                for student in student_list:
                    if student[6] == student_id:

                        check_exist = True

                if check_exist:
                    print("This Student id Exist")
                    input()

                else:

                    temp = False

        # endregion

        # region Check Csharp

        temp = True

        while temp:
            system("cls")

            csharp_score = int(input("\n\nCsharp Score : "))

            if csharp_score not in range(1, 101):

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        # region Check Java

        temp = True

        while temp:
            system("cls")

            java_score = int(input("\n\nJava Score : "))

            if java_score not in range(1, 101):

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        # region Check Python

        temp = True

        while temp:
            system("cls")

            python_score = int(input("\n\nPython Score : "))

            if python_score not in range(1, 101):

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        # region Check Php

        temp = True

        while temp:
            system("cls")

            php_score = int(input("\n\nPhp Score : "))

            if php_score not in range(1, 101):

                print("Error!!!")
                input()

            else:

                temp = False

        # endregion

        student = [name, family, age, gender, class_, national_code,
                   student_id, csharp_score, java_score, python_score, php_score]
        student_list.append(student)

        print("Done")
        input()

    # endregion

    # region Menu 2 =  Show Student ...

    elif menu == "2":

        # region Show Menu

        print("\t\tShow Student")
        print("--------------------------------------------------")
        input()
        system("cls")

        # endregion

        # region Ask Information

        # region Ask Name

        disply_name = False

        ask_name = input("\n\nDo You Want To See ? ( Name ) :  ")

        if ask_name == "yes":

            disply_name = True

        system("cls")

        # endregion

        # region Ask Family

        disply_family = False

        ask_family = input("\n\nDo You Want To See ? ( Family ) :  ")

        if ask_family == "yes":

            disply_family = True

        system("cls")

        # endregion

        # region Ask Age

        disply_age = False

        ask_age = input("\n\nDo You Want To See ? ( Age ) :  ")

        if ask_age == "yes":

            disply_age = True

        system("cls")

        # endregion

        # region Ask Gender

        disply_gender = False

        ask_gender = input("\n\nDo You Want To See ? ( Gender ) :  ")

        if ask_gender == "yes":

            disply_gender = True

        system("cls")

        # endregion

        # region Ask Class

        disply_class = False

        ask_class = input("\n\nDo You Want To See ? ( Class ) :  ")

        if ask_class == "yes":

            disply_class = True

        system("cls")

        # endregion

        # region Ask National Code

        disply_natonal_code = False

        ask_natonal_code = input(
            "\n\nDo You Want To See ?  ( National Code ) :  ")

        if ask_natonal_code == "yes":

            disply_natonal_code = True

        system("cls")

        # endregion

        # region Ask Student id

        disply_student_id = False

        ask_student_id = input("\n\nDo You Want To See  ( Student id ) :  ")

        if ask_student_id == "yes":

            disply_student_id = True

        system("cls")

        # endregion

        # region Ask Csharp

        disply_csharp = False

        ask_csharp = input("\n\nDo You Want To See  ( Csharp ) :  ")

        if ask_csharp == "yes":

            disply_csharp = True

        system("cls")

        # endregion

        # region Ask Java

        disply_java = False

        ask_java = input("\n\nDo You Want To See  ( Java ) :  ")

        if ask_java == "yes":

            disply_java = True

        system("cls")

        # endregion

        # region Ask Python

        disply_python = False

        ask_python = input("\n\nDo You Want To See  ( Python ) :  ")

        if ask_python == "yes":

            disply_python = True

        system("cls")

        # endregion

        # region Ask Php

        disply_php = False

        ask_php = input("\n\nDo You Want To See  ( Php ) :  ")

        if ask_php == "yes":

            disply_php = True

        system("cls")

        # endregion

        # endregion

        # region Show Information

        print("\t\tShow Information")
        print("--------------------------------------------------")
        print("\n\n")

        for student in student_list:

            if disply_name:

                print(student[0], end=" ")

            if disply_family:

                print(student[1], end=", ")

            if disply_age:

                print(student[2], end=", ")

            if disply_gender:

                print(student[3], end=", ")

            if disply_class:

                print("Class:", student[4], sep="", end=", ")

            if disply_natonal_code:

                print("Nationalcode:", student[5], sep="", end=", ")

            if disply_student_id:

                print("Stdid:", student[6], sep="", end=", ")

            if disply_csharp:

                print("Csharp:", student[7], sep="", end=", ")

            if disply_java:

                print("Java:", student[8], sep="", end=", ")

            if disply_python:

                print("Python:", student[9], sep="", end=", ")

            if disply_php:

                print("Php:", student[10], sep="")

            print()

        input()

        # endregion

    # endregion

    # region Menu 3 =  Search Student ...

    elif menu == "3":

        # region Show Menu

        search_flag = True

        while search_flag:
            system("cls")

            print("\t\tSearch Student")
            print("--------------------------------------------------")
            print("\n\nSearch With :")
            print("\n1\ National Code  ")
            print("2\ Student id  ")
            print("3\ Exit  ")

            search_menu_input = input("\n\nMenu : ")
            system("cls")

        # endregion

        # region Search Menu 1 = National Code

            if search_menu_input == "1":

                temp = True

                while temp:
                    system("cls")

                    national_code = input("\n\nNational Code : ")

                    if national_code == "":

                        print("Error")
                        input()

                    else:

                        check_exist = False

                        for student in student_list:
                            if student[5] == national_code:

                                print("\n")
                                print(student[0], end=" ")
                                print(student[1], end=", ")
                                print(student[2], end=", ")
                                print(student[3], end=", ")
                                print("Class:", student[4], sep="", end=", ")
                                print("Nationalcode:",
                                      student[5], sep="", end=", ")
                                print("Stdid:", student[6], sep="", end=", ")
                                print("Csharp:", student[7], sep="", end=", ")
                                print("Java:", student[8], sep="", end=", ")
                                print("Python:", student[9], sep="", end=", ")
                                print("Php:", student[10], sep="")
                                input()

                                check_exist = True

                        if check_exist:

                            print("Done")
                            input()

                            temp = False

                        else:

                            print(national_code, " Does Not Exist")
                            input()

        # endregion

        # region Search Menu 2 = Student id

            elif search_menu_input == "2":

                temp = True

                while temp:
                    system("cls")

                    student_id = input("\n\nStudent id : ")

                    if student_id == "":

                        print("Error")
                        input()

                    else:

                        check_exist = False

                        for student in student_list:
                            if student[6] == student_id:

                                print("\n")
                                print(student[0], end=" ")
                                print(student[1], end=", ")
                                print(student[2], end=", ")
                                print(student[3], end=", ")
                                print("Class:", student[4], sep="", end=", ")
                                print("Nationalcode:",
                                      student[5], sep="", end=", ")
                                print("Stdid:", student[6], sep="", end=", ")
                                print("Csharp:", student[7], sep="", end=", ")
                                print("Java:", student[8], sep="", end=", ")
                                print("Python:", student[9], sep="", end=", ")
                                print("Php:", student[10], sep="")
                                input()

                                check_exist = True

                        if check_exist:

                            print("Done")
                            input()

                            temp = False

                        else:

                            print(student_id, " Does Not Exist")
                            input()

        # endregion

        # region Search Menu 3 = Exit

            elif search_menu_input == "3":

                search_flag = False

            else:

                print("Error")
                input()

        # endregion

    # endregion

    # region Menu 4 =  Remove Student ...

    elif menu == "4":

        # region Menu 4

        remove_flag = True

        while remove_flag:
            system("cls")

            print("\t\tRemove Student")
            print("--------------------------------------------------")
            print("\n\nRemove With :")
            print("\n1\ National Code  ")
            print("2\ Student id  ")
            print("3\ Exit  ")

            remove_menu_input = input("\n\nMenu : ")
            system("cls")

        # endregion

        # region Remove Menu 1 = National Code

            if remove_menu_input == "1":

                temp = True

                while temp:
                    system("cls")

                    national_code = input("\n\nNational Code : ")

                    if national_code == "":

                        print("Error")
                        input()

                    else:

                        check_exist = False

                        for student in student_list:
                            if student[5] == national_code:
                                student_list.remove(student)

                                check_exist = True

                        if check_exist:

                            print("\nRemoved. Done")
                            input()

                            temp = False

                        else:

                            print(national_code, " Does Not Exist")
                            input()

        # endregion

        # region Remove Menu 2 = Student id

            elif remove_menu_input == "2":

                temp = True

                while temp:
                    system("cls")

                    student_id = input("\n\nStudent id : ")

                    if student_id == "":

                        print("Error")
                        input()

                    else:

                        check_exist = False

                        for student in student_list:
                            if student[6] == student_id:
                                student_list.remove(student)

                                check_exist = True

                        if check_exist:

                            print("\nRemoved . Done")
                            input()

                            temp = False

                        else:

                            print(student_id, " Does Not Exist")
                            input()

        # endregion

        # region Remove Menu 3 = Exit

            elif remove_menu_input == "3":

                remove_flag = False

            else:

                print("Error")
                input()

        # endregion

    # endregion

    # region Menu 5 =  Edit Student ...

    elif menu == "5":

        # region Show Menu

        edit_flag = True

        while edit_flag:
            system("cls")

            print("\t\tEdit Student")
            print("--------------------------------------------------")
            print("\n\nEdit With :")
            print("\n1\ National Code  ")
            print("2\ Student id  ")
            print("3\ Exit  ")

            edit_menu_input = input("\n\nMenu : ")
            system("cls")

        # endregion

        # region Edit Menu 1 = National Code

            # region Check National Code

            if edit_menu_input == "1":

                temp = True

                while temp:
                    system("cls")

                    national_code = input("\n\nNational Code : ")

                    if national_code == "":
                        print("Error")
                        input()

                    else:

                        check_exist = False

                        for student in student_list:
                            if student[5] == national_code:

                                old_nationalcode = student[5]
                                old_studentid = student[6]
                                system("cls")

            # endregion

            # region Check Info

                                # region Check Name

                                ask_name = input(
                                    "\n\nDo You Want To Edit ? ( Name ) :  ")

                                if ask_name == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        name = input("\n\nName : ")

                                        if name == "":

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Family

                                ask_family = input(
                                    "\n\nDo You Want To Edit ? ( Family ) :  ")

                                if ask_family == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        family = input("\n\nFamily : ")

                                        if family == "":

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Age

                                ask_age = input(
                                    "\n\nDo You Want To Edit ? ( Age ) :  ")

                                if ask_age == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        age = int(input("\n\nAge : "))

                                        if age not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Gender

                                ask_gender = input(
                                    "\n\nDo You Want To Edit ? ( Gender ) :  ")

                                if ask_gender == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        gender = input("\n\nGender : ")

                                        if gender == "":

                                            print("Error!!!")
                                            input()

                                        elif gender not in ("male", "female", "other"):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Class

                                ask_class = input(
                                    "\n\nDo You Want To Edit ? ( Class ) :  ")

                                if ask_class == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        class_ = input("\n\nClass  (a,b,c) : ")

                                        if class_ == "":

                                            print("Error!!!")
                                            input()

                                        elif class_ not in ("a", "b", "c"):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check National Code

                                ask_national_code = input(
                                    "\n\nDo You Want To Edit ?  ( National Code ) :  ")

                                if ask_national_code == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        national_code = input(
                                            "\n\nNational Code : ")

                                        if old_nationalcode == national_code:

                                            ask_temp = False

                                        elif national_code == "":

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_check_exist = False

                                            for check_student in student_list:
                                                if check_student[5] == national_code:

                                                    ask_check_exist = True

                                            if ask_check_exist:

                                                print(
                                                    "This National Code Exist")
                                                input()

                                            else:

                                                ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Std_Id

                                ask_student_id = input(
                                    "\n\nDo You Want To Edit ?  ( Student id ) :  ")

                                if ask_student_id == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        student_id = input("\n\nStudent id : ")

                                        if old_studentid == student_id:

                                            ask_temp = False

                                        elif student_id == "":

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_check_exist = False

                                            for check_student in student_list:
                                                if check_student[6] == student_id:

                                                    ask_check_exist = True

                                            if ask_check_exist:

                                                print("This Student id Exist")
                                                input()

                                            else:

                                                ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Csharp

                                ask_csharp = input(
                                    "\n\nDo You Want To edit ? ( Csharp ) :  ")

                                if ask_csharp == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        csharp = int(input("\n\nCsharp : "))

                                        if csharp not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Java

                                ask_java = input(
                                    "\n\nDo You Want To edit ? ( Java ) :  ")

                                if ask_java == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        java = int(input("\n\nJava : "))

                                        if java not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Python

                                ask_python = input(
                                    "\n\nDo You Want To edit ? ( Python ) :  ")

                                if ask_python == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        python = int(input("\n\nPython : "))

                                        if python not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Php

                                ask_php = input(
                                    "\n\nDo You Want To edit ? ( Php ) :  ")

                                if ask_php == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        php = int(input("\n\nPhp : "))

                                        if php not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

            # endregion

            # region Edit Info

                                if ask_name == "yes":

                                    student[0] = name

                                if ask_family == "yes":

                                    student[1] = family

                                if ask_age == "yes":

                                    student[2] = age

                                if ask_gender == "yes":

                                    student[3] = gender

                                if ask_class == "yes":

                                    student[4] = class_

                                if ask_national_code == "yes":

                                    student[5] = national_code

                                if ask_student_id == "yes":

                                    student[6] = student_id

                                if ask_csharp == "yes":

                                    student[7] = csharp

                                if ask_java == "yes":

                                    student[8] = java

                                if ask_python == "yes":

                                    student[9] = python

                                if ask_php == "yes":

                                    student[10] = php

                                check_exist = True

                        if check_exist:

                            print("\nDone")
                            input()
                            temp = False

                        else:

                            print(national_code, " Does Not Exist")
                            input()

            # endregion

        # endregion

        # region Edit Menu 2 = Student id

            # region Check National Code

            elif edit_menu_input == "2":

                temp = True

                while temp:
                    system("cls")

                    student_id = input("\n\nStudent id : ")

                    if student_id == "":
                        print("Error")
                        input()

                    else:

                        check_exist = False

                        for student in student_list:
                            if student[6] == student_id:

                                old_nationalcode = student[5]
                                old_studentid = student[6]
                                system("cls")

            # endregion

            # region Check Info

                                # region Check Name

                                ask_name = input(
                                    "\n\nDo You Want To Edit ? ( Name ) :  ")

                                if ask_name == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        name = input("\n\nName : ")

                                        if name == "":

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Family

                                ask_family = input(
                                    "\n\nDo You Want To Edit ? ( Family ) :  ")

                                if ask_family == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        family = input("\n\nFamily : ")

                                        if family == "":

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Age

                                ask_age = input(
                                    "\n\nDo You Want To Edit ? ( Age ) :  ")

                                if ask_age == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        age = int(input("\n\nAge : "))

                                        if age not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Gender

                                ask_gender = input(
                                    "\n\nDo You Want To Edit ? ( Gender ) :  ")

                                if ask_gender == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        gender = input("\n\nGender : ")

                                        if gender == "":

                                            print("Error!!!")
                                            input()

                                        elif gender not in ("male", "female", "other"):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Class

                                ask_class = input(
                                    "\n\nDo You Want To Edit ? ( Class ) :  ")

                                if ask_class == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        class_ = input("\n\nClass  (a,b,c) : ")

                                        if class_ == "":

                                            print("Error!!!")
                                            input()

                                        elif class_ not in ("a", "b", "c"):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check National Code

                                ask_national_code = input(
                                    "\n\nDo You Want To Edit ?  ( National Code ) :  ")

                                if ask_national_code == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        national_code = input(
                                            "\n\nNational Code : ")

                                        if old_nationalcode == national_code:

                                            ask_temp = False

                                        elif national_code == "":

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_check_exist = False

                                            for check_student in student_list:
                                                if check_student[5] == national_code:

                                                    ask_check_exist = True

                                            if ask_check_exist:

                                                print(
                                                    "This National Code Exist")
                                                input()

                                            else:

                                                ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Std_Id

                                ask_student_id = input(
                                    "\n\nDo You Want To Edit ?  ( Student id ) :  ")

                                if ask_student_id == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        student_id = input("\n\nStudent id : ")

                                        if old_studentid == student_id:

                                            ask_temp = False

                                        elif student_id == "":

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_check_exist = False

                                            for check_student in student_list:
                                                if check_student[6] == student_id:

                                                    ask_check_exist = True

                                            if ask_check_exist:

                                                print("This Student id Exist")
                                                input()

                                            else:

                                                ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Csharp

                                ask_csharp = input(
                                    "\n\nDo You Want To edit ? ( Csharp ) :  ")

                                if ask_csharp == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        csharp = int(input("\n\nCsharp : "))

                                        if csharp not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Java

                                ask_java = input(
                                    "\n\nDo You Want To edit ? ( Java ) :  ")

                                if ask_java == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        java = int(input("\n\nJava : "))

                                        if java not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Python

                                ask_python = input(
                                    "\n\nDo You Want To edit ? ( Python ) :  ")

                                if ask_python == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        python = int(input("\n\nPython : "))

                                        if python not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

                                # region Check Php

                                ask_php = input(
                                    "\n\nDo You Want To edit ? ( Php ) :  ")

                                if ask_csharp == "yes":

                                    ask_temp = True

                                    while ask_temp:
                                        system("cls")

                                        php = int(input("\n\nPhp : "))

                                        if php not in range(1, 121):

                                            print("Error!!!")
                                            input()

                                        else:

                                            ask_temp = False

                                system("cls")

                                # endregion

            # endregion

            # region Edit Info

                                if ask_name == "yes":

                                    student[0] = name

                                if ask_family == "yes":

                                    student[1] = family

                                if ask_age == "yes":

                                    student[2] = age

                                if ask_gender == "yes":

                                    student[3] = gender

                                if ask_class == "yes":

                                    student[4] = class_

                                if ask_national_code == "yes":

                                    student[5] = national_code

                                if ask_student_id == "yes":

                                    student[6] = student_id

                                if ask_csharp == "yes":

                                    student[7] = csharp

                                if ask_java == "yes":

                                    student[8] = java

                                if ask_python == "yes":

                                    student[9] = python

                                if ask_php == "yes":

                                    student[10] = php

                                check_exist = True

                        if check_exist:

                            print("\nDone")
                            input()
                            temp = False

                        else:

                            print(student_id, " Does Not Exist")
                            input()

            # endregion

        # endregion

        # region Edit Menu 3  = Exit

            elif edit_menu_input == "3":

                edit_flag = False

            else:

                print("Error")
                input()

        # endregion

    # endregion

    # region Menu 6 =  Best Student...

    elif menu == "6":

        print("\t\t Best Student")
        print("--------------------------------------------------")

        max_ = 0

        for student in student_list:

            avg = (student[7] + student[8] + student[9] + student[10]) / 4
            if avg >= max_:

                max_ = avg

        print("\n\nBest Average : ", max_, "\n\n")

        for student in student_list:

            avg = (student[7] + student[8] + student[9] + student[10]) / 4

            if avg == max_:

                print(student[0], end=" ")
                print(student[1], end=", ")
                print(student[2], end=", ")
                print(student[3], end=", ")
                print("Class:", student[4], sep="", end=", ")
                print("Nationalcode:", student[5], sep="", end=", ")
                print("Stdid:", student[6], sep="", end=", ")
                print("Csharp:", student[7], sep="", end=", ")
                print("Java:", student[8], sep="", end=", ")
                print("Python:", student[9], sep="", end=", ")
                print("Php:", student[10], sep="")

        input()

    # endregion

    # region Menu 7 =  Best Score ...

    elif menu == "7":

        # region Show Menu :

        score_flag = True
        while score_flag:
            system("cls")

            print("\t\tBest Score")
            print("--------------------------------------------------")
            print("\n\n1\ C# ")
            print("2\ Java  ")
            print("3\ Python  ")
            print("4\ Php  ")
            print("5\ Exit  ")

            score_menu_input = input("\n\nMenu : ")
            system("cls")

        # endregion

        # region Best Score Menu 1 = C#

            if score_menu_input == "1":

                print("\t\tBest Score C#")
                print("--------------------------------------------------")

                max_ = 0

                for student in student_list:

                    if student[7] >= max_:
                        max_ = student[7]

                print("\n\nBest C# Score : ", max_, "\n\n")

                for student in student_list:

                    if student[7] == max_:

                        print(student[0], end=" ")
                        print(student[1], end=", ")
                        print(student[2], end=", ")
                        print(student[3], end=", ")
                        print("Class:", student[4], sep="", end=", ")
                        print("Nationalcode:", student[5], sep="", end=", ")
                        print("Stdid:", student[6], sep="", end=", ")
                        print("Csharp:", student[7], sep="", end=", ")
                        print("Java:", student[8], sep="", end=", ")
                        print("Python:", student[9], sep="", end=", ")
                        print("Php:", student[10], sep="")

                input()

        # endregion

        # region Best Score Menu 2 = Java

            elif score_menu_input == "2":

                print("\t\tBest Score Java")
                print("--------------------------------------------------")

                max_ = 0

                for student in student_list:

                    if student[8] >= max_:
                        max_ = student[8]

                print("\n\nBest Java Score : ", max_, "\n\n")

                for student in student_list:

                    if student[8] == max_:

                        print(student[0], end=" ")
                        print(student[1], end=", ")
                        print(student[2], end=", ")
                        print(student[3], end=", ")
                        print("Class:", student[4], sep="", end=", ")
                        print("Nationalcode:", student[5], sep="", end=", ")
                        print("Stdid:", student[6], sep="", end=", ")
                        print("Csharp:", student[7], sep="", end=", ")
                        print("Java:", student[8], sep="", end=", ")
                        print("Python:", student[9], sep="", end=", ")
                        print("Php:", student[10], sep="")

                input()

        # endregion

        # region Best Score Menu 3 = Python

            elif score_menu_input == "3":

                print("\t\tBest Score Python")
                print("--------------------------------------------------")

                max_ = 0

                for student in student_list:

                    if student[9] >= max_:
                        max_ = student[9]

                print("\n\nBest Python Score : ", max_, "\n\n")

                for student in student_list:

                    if student[8] == max_:

                        print(student[0], end=" ")
                        print(student[1], end=", ")
                        print(student[2], end=", ")
                        print(student[3], end=", ")
                        print("Class:", student[4], sep="", end=", ")
                        print("Nationalcode:", student[5], sep="", end=", ")
                        print("Stdid:", student[6], sep="", end=", ")
                        print("Csharp:", student[7], sep="", end=", ")
                        print("Java:", student[8], sep="", end=", ")
                        print("Python:", student[9], sep="", end=", ")
                        print("Php:", student[10], sep="")

                input()

        # endregion

        # region Best Score Menu 4 = Php

            elif score_menu_input == "4":

                print("\t\tBest Score Php")
                print("--------------------------------------------------")

                max_ = 0

                for student in student_list:

                    if student[10] >= max_:
                        max_ = student[10]

                print("\n\nBest Php Score : ", max_, "\n\n")

                for student in student_list:

                    if student[10] == max_:

                        print(student[0], end=" ")
                        print(student[1], end=", ")
                        print(student[2], end=", ")
                        print(student[3], end=", ")
                        print("Class:", student[4], sep="", end=", ")
                        print("Nationalcode:", student[5], sep="", end=", ")
                        print("Stdid:", student[6], sep="", end=", ")
                        print("Csharp:", student[7], sep="", end=", ")
                        print("Java:", student[8], sep="", end=", ")
                        print("Python:", student[9], sep="", end=", ")
                        print("Php:", student[10], sep="")

                input()

        # endregion

        # region Best Score Menu 5 = Exit

            elif score_menu_input == "5":

                score_flag = False

            else:

                print("Error")
                input()

        # endregion

    # endregion

    # region Menu 8 =  Exit

    elif menu == "8":

        flag = False

    else:

        print("Error...")
        input()

    # endregion


print("\n\nGood Luck...")
input()
