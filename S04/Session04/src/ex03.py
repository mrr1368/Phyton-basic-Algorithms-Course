


# 1+ 1/3 + 1/5 + ... + 1/n

num = int(input("num : "))

if num % 2 == 0 :
    print("error")

else:
          
    sum_ = 0

    i = 1

    while i <= num :

       sum_ += 1/i

       i += 2
