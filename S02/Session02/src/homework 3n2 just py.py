


num1 = float(input("enter num1 : "))
num2 = float(input("enter num2 : "))
num3 = float(input("enter num3 : "))

if num1 >= num2 >= num3 :
    print(num1, num2, num3, sep=" > ")

elif num1 >=  num3 >= num2 :
    print(num1, num3, num2, sep=" > ")

elif num2 >= num1 >= num3 :
    print(num2, num1, num3, sep=" > ")

elif num2 >= num3 >= num1 :
    print(num2, num3, num1, sep=" > ")

elif num3 >= num1 >= num2 :
    print(num3, num1, num2, sep=" > ")

else:
    print(num3, num2, num1, sep=" > ")

