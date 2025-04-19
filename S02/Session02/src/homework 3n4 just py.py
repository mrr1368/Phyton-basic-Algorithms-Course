


num1 = float(input("enter num1 : "))
num2 = float(input("enter num2 : "))

if num1 <= num2 :
    num1, num2 = num2, num1

print (num1, num2, sep=" > ")