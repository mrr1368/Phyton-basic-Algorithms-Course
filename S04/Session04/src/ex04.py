


# 1 - 1/2 + 1/3 - 1/4 + ... + 1/n

num = int(input("num : "))

sum_ = 0

i = 1

while i <= num :
    
    if i % 2 == 1 :

       sum_ += 1/i

    else:
          
       sum_ -= 1/i
    i += 1

print(sum_)
