


num1 = float(input("enter num1 : "))
num2 = float(input("enter num2 : "))
num3 = float(input("enter num3 : "))

if num2 >= num1 :
    num1, num2 = num2, num1

if num3 >= num1 :
    num3, num1 = num1, num3

if num3 >= num2 :
    num3, num2 = num2, num3

print(num1, num2, num3, sep=" > ")

