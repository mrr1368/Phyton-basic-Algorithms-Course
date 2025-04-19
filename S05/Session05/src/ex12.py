

max_ = min_ = float(input("num : "))

for _ in range(19):
    num = float(input("num : "))

    if num > max_:
        max_ = num
    
    elif num < min_:
        min_ = num 

print(max_)
print(min_)
