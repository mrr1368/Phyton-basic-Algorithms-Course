


day = int(input("days :"))

if day not in range(1, 367):
    print("error!!!")

else:
    
    if day in range(1, 32):
        print("farvardin", day)

    elif day in range(32, 63):
        print("ordibehesht", day - 31)

    elif day in range(63, 94):
        print("khordad", day - 62)

    elif day in range(94, 125):
        print("tir", day - 93)

    elif day in range(125, 156):
        print("mordad", day - 124)

    elif day in range(156, 187):
        print("shahrivar", day - 155)

    elif day in range(187, 217):
        print("mehr", day - 186)

    elif day in range(217, 247):
        print("aban", day - 216)

    elif day in range(247, 277):
        print("azar", day - 246)

    elif day in range(277, 307):
        print("dey", day - 276)

    elif day in range(307, 337):
        print("bahman", day - 306)

    else:
        print("esfand", day - 336)
