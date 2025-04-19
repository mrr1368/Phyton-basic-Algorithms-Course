

data = ["meisam", "ilka", 31, "meisam", "meisam"]

data.append("male")

data.remove("meisam")
# data.remove("meisam01")   ValueError

val = "hi"

if val in data :
    data.remove(val)



val = "meisam"

while val in data :
    data.remove(val)


print(data)
