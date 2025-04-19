

# nested list 

#  ["miesam", "ilka", 0936, "mehrsa", "bokaei", 0912 , "mokhtar", "jafari", 0911]

data = [
    ["miesam", "ilka", "0936"],
    ["mehrsa", "bokaei", "0912"],
    ["mokhtar", "jafari", "0911"],
]

res = data[0]   #["miesam", "ilka", "0936"]
res = data[1]   #["mehrsa", "bokaei", "0912"]
res = data[2]   #["mokhtar", "jafari", "0911"]


res = data[0][0] #"miesam"

print(data[0][0])

# --------------------------------------

contact_list =[]

for _ in range (3) :   # (0, 3)
    contact = []
    contact.append(input("name"))
    contact.append(input("family"))
    contact.append(input("phone"))
    contact_list.append(contact)


    for contact in contact_list :
        for item in contact :
            print(item , end = "\t\t")

        print()

input()
