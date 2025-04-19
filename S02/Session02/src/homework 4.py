


month = int(input("month :"))

if month not in range (1,13) :
    print("error!!!")

else:
    day = int(input("days :"))

    if (month in range (1,7) and day not in range (1,32) or \
         month in range (7,13) and day not in range (1,31)) :
        print("error!!!")

    else:

        if month in range (1,7) :
            res = ((month - 1) * 31) + day
            
        else:
            res = ((month - 1) * 30) + day + 6
        
        print (res)
        
        
        

# day = int(input("day :"))
# month = int(input("month :"))

# if month not in range (1, 13) and day not in range (1, 32) :
#      print("eroor")

# else:
#      i = 1
#      p1 = 0
#      while (i < 7 and i <= (month - 1 )):
#                p1 += 31
#                i += 1      
     
#      i = 7
#      p2 = 0
#      while (i <= 13 and i <= (month - 1 )):
#                p2 += 30
#                i += 1

# total = p1 + p2 + day
# print (total)


