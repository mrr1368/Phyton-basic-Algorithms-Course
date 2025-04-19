
# 1

data = [5,6,7,8,9,10,11,12,13,14,15]

sum_ = 0

for item in data :
    sum_ += item

print("sum : ", sum_)    

# -----------------------------------------

# 2

data = [5,6,7,8,9,10,11,12,13,14,15]

sum_ = 0

for index in range (0, len(data)) :
    sum_ += data[index]

print("sum : ", sum_)    

# ------------------------------------------ 

data = [5,6,7,8,9,10,11,12,13,14,15]

sum_ = 0
index = 0

while index < len(data) :
    sum_ += data[index]

print("sum : ", sum_)    
