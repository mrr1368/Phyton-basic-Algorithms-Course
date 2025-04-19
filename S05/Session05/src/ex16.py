

for num in range(2, 101):
    print(num, end=": ")

    for i in range(1, ((num//2) + 1)):
        count = 1
        if num % i == 0:
            count += 1

    print(count, end = "  ---  ")
