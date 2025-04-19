

from os import system
count = 3

car_list = [""] * (count * 4)

for i in range(0, count) :
    car_list[i * 4] = input("name :")  
    car_list[(i * 4) + 1] = int(input("speed :"))  
    car_list[(i * 4) + 2] = int(input("year :"))  
    car_list[(i * 4) + 3] = input("code :")  

    system("cls")

# print(contact_list)

# --------
print("name\t\tspeed\t\tyear\t\tcode\t\t")
print("----------------------------------------")

for i in range (0, len(car_list)) :
    if i % 4 == 0 :
       print()

    print(car_list[i], end = "\t\t")

input()
