

from os import system
count = 3

contact_list = [""] * (count * 3)

for i in range(0, count) :
    contact_list[i * 3] = input("first name :")  
    contact_list[(i * 3) + 1] = input("last name :")  
    contact_list[(i * 3) + 2] = input("phone :")  
    system("cls")

# print(contact_list)

# --------
print("name\t\tfamily\t\tphone\t\t")
print("----------------------------------------")

for i in range (0, len(contact_list)) :
    if i % 3 == 0 :
       print()

    print(contact_list[i], end = "\t\t")

input()


