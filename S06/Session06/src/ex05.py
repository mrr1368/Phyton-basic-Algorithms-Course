    

# 1

data = [5,6,7,8,9,10,11,12,13,14,15,]

max_ = min_ = data[0]
sum_ = 0

for item in data :
    sum_ += item 

    if item > max_ :
        max_ = item

    elif item < min_ :
        min_ = item 

avg = sum_ / len(data)

print("max :", max_)
print("min :", min_)
print("avg :", avg)

# ---------------------------------------

# 2

data = [5,6,7,8,9,10,11,12,13,14,15,]

max_ = min_ = sum_ = data[0]


for index in range (1, len(data)) :

    num = data[index] 
    sum_ += num 

    if num <= min_:
        min_ = num

    elif num >= max_:
        max_ = num

print("min : ", min_)    
print("max : ", max_)    
print("avg : ", sum_ / len(data))    
