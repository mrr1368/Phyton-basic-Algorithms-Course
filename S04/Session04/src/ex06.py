


num = float(input("num is : "))

count = 1

i = 1

while i <= num // 2 :
    
    if num % i == 0 :
        
        count += 1

    i += 1

if count == 2 :

    print(num, " is prime")    

else:

    print(num, " is not prime")    


