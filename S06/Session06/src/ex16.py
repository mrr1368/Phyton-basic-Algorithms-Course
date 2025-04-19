

from os import system

car_list = []

for i in range(4) :

    name = input("name :")
    speed = int(input("speed :"))
    year = int(input("year :"))
    code = input("code :")

    car = []
    car.append(name)  
    car.append(speed)  
    car.append(year)  
    car.append(code)  

    car_list.append(car)

    system("cls")

print("name\t\tspeed\t\tyear\t\tcode\t\t")
print("----------------------------------------")

for car in car_list :
    for item in car :
       print(item, end = "\t\t")
    print()

input()
