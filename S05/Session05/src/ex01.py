

row = 1 

while row <= 9 :
    column = 1

    while column <= 9 :
        print(row, "*", column, "=", row*column, end = "\t")
        column += 1
        
    print()
    row += 1