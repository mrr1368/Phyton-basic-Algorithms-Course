

# 1
data = ["meisam", "ilka", 31, True, 3.14 ] 

# index = andis       0, len-1

res = data[0] 
res = data[1]
res = data[2]
res = data[3]
res = data[4]
# res = data[5]    error out of range    index error

# --------------------------------------------

# 2
data = ["meisam", "ilka", 31, True, 3.14]

index = 0

while index < len(data):
    print(data[index])
    index += 1

print("\n")

# -------------------------------------------

# 3
data = ["meisam", "ilka", 31, True, 3.14]

for index in range (0, len(data)) :
    print(data[index])

print("\n")
 
#    get
# --------------------------------------------

# 4 for eterevery

data = ["meisam", "ilka", 31, True, 3.14]

for item in ["meisam", "ilka", 31, True, 3.14] :
    print(item)

print("\n")


# -----------------------------------------------

# 5

data = ["meisam", "ilka", 31, True, 3.14]

for item in data :
    print(item)

print("\n")

# ------------------------------------------------

# 3 way to get
data = ["meisam", "ilka", 31, True, 3.14]

index = 0

while index < len(data):
    print(data[index])
    index += 1

for index in range(0, len(data)):
    print(data[index])


for item in data:
    print(item)
 