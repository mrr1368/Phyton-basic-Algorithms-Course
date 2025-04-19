

count = 3

std_info = [""] * (count * 2)

for i in range(0, len(std_info)) :
    std_info[i * 2] = input("first name :")  
    std_info[(i * 2) + 1] = input("last name :")  

print(std_info)


# 0 > 0,1
# 1 > 2,3
# 2 > 4,5
# 3 > 6,7   