

from os import system

contact_list = [
    ["reza", "rajab", "0935", "parand"],
    ["tohid", "rajab", "0936", "parand"],
    ["majid", "rajab", "0937", "parand"],
]

flag = True

while flag :
    system("cls")

    # region show menu

    print("\t\t\twelcom")
    print("------------------------------------------------------")
    print("\n\n1/  add contact")
    print("2/  show contact ")
    print("3/  remove contact")
    print("4/  edit contact")
    print("5/  search")
    print("6/  exit")

    menu = (input("\nmenu : "))
    system("cls")

    # endregion
    
    # region menu = 1 add contact

    if menu == "1" :

        print("add contact")
        print("-------------------")
        
        # region name check

        temp = True
        while temp :  

            name = (input("name : "))
            

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
            

            if family == "":
                print("family is empty")
                input()

            else:
                temp = False

        # endregion

        # region phone check

        temp = True
        while temp :  

            phone = (input("phone : "))
            

            if phone == "" :
                print("phone number is empty")


            else:

                check_exist = False

                for contact in contact_list :
                    if contact[2] == phone :
                        check_exist = True
                
                if check_exist :
                    print(phone, "exist")

                else :
                    
                    temp = False

        # endregion

        address = input("address :")
        print("done")
        input()

        contact = [name, family, phone, address]
        contact_list.append(contact)
        system("cls")

    # endregion

    # region menu = 2 show contact
    elif menu == "2" :
                
        print("show student")
        print("--------------------")
        print("\n\nname\t\tfamily\t\tphone\t\taddress")
        print("-------------------------------------------------------------------")
        print("\n")

        for contact in contact_list:
            for item in contact:
                print(item, end = "\t\t")
            
            print()
        input()

    # endregion

    # region menu = 3 remove contact

    elif menu == "3" :

        print("remove contact")
        print("--------------------")

        remove_contact = input("phone number :")

        if remove_contact == "" :
            print("phone number is empty")
        
        else :
            check_remove = False

            for contact in contact_list:
                if remove_contact == contact[2] :
                    contact_list.remove(contact)
                    check_remove = True
            
            if check_remove:
                print("done")
                input()
            
            else :
                print(" phone number not exist")

    # endregion

    # region menu = 4 edit contact

    elif menu == "4" :

        print("edit contact")
        print("--------------------")

        edit_contact = input("phone number :")
        system("cls")
        
        check_edit = False

        for contact in contact_list:
            if edit_contact == contact[2] :
                # region name check

                temp = True
                while temp :  

                    name = (input("name : "))
                    

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
                    

                    if family == "":
                        print("family is empty")
                        input()

                    else:
                        temp = False

                # endregion

                address = input("address :")
                system("cls")

                contact[0] = name
                contact[1] = family
                contact[3] = address

                check_edit = True
        
        if check_edit:
            print("done")
        
        else :
            print(" phone number not exist")




    # endregion
   
    # region menu = 5 serch contact
    elif menu == "5" :

        print("search contact")
        print("--------------------")

        search_contact = input("phone number :")

        if search_contact == "" :
            print("phone number is empty")
            input()
        
        else :
            check_search = False

            for contact in contact_list:
                if contact[2] == search_contact :
                    print("fullname : ", contact[0] , contact[1], ",  phone number : ", contact[2] , ",  address : ", contact[3])
                    
                    check_search = True
            
            if check_search:
                print("\n\ndone")
                input()
            
            else :
                print(" phone number not exist")
                input()



    # endregion

    # region menu = 6 exit

    elif menu == "6" :
        flag = False 

    else:
        print("error")
        input()

    # endregion


print("good bye")
input()
