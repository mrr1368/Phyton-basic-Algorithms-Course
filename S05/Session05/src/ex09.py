

num1 = int(input("num 1 :"))
num2 = int(input("num 2 :"))

if num1 >= num2:
    num1, num2 = num2, num1

for i in range(num1, num2+1):
    print(i)
