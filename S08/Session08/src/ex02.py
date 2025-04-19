

def devisore(num) :

    res = []

    for i in range (1, num//2+1) :
        if num % i == 0 :
            res.append(i)     

    res.append(num)

    return res

for num in range(2, 101):
    print(num, " : ",devisore(num))
    