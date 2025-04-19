

from os import system

count = 4

car_list = []

for i in range(0, count) :
    car_list.append(input("name :"))  
    car_list.append(int(input("speed :")))  
    car_list.append(int(input("year :")))  
    car_list.append(input("code :"))  
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
