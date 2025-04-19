

# set kardan

from os import system 
score_list = [0] * 3

for index in range (0, len(score_list)) :
    score_list[index] = float(input("score :"))
    system("cls")

min_ = max_ = score_list[0] 

# get kardan 

for index in range (1, len(score_list)) :
    num = score_list[index]

    if num < min_ :
        min_ = num

    elif num > max_ :
        max_ = num

print(min_)
print(max_)


for score in score_list :
    print(score , end = "   ")

input()