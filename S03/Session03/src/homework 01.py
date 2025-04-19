


number = float(input("num is : "))

i = 1

print(number, end = " : ")

while i <= number :
    
    if number % i == 0 :
        print(i, end = " ")

    i += 1
    
input()



num = int(input("num :"))

i = 1
count = 0

while i <= num :

    if num % i == 0 :
        count += 1
    
    i += 1

print(count)
    
