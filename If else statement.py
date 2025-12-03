#example 1

x = 7
if x > 10:
    print("x is greater than 10")
elif x >5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is not greater than 5")

#example 2

x = 15
if x > 10:
    print("x is greater than 10")
else:
    if x > 5:
        print("x is greater than 5 but less than or equal to 10")
    else:
        print("x is not greater than 5")


#example 3

number = [1,2,3,4,5]

for num in number:
    if num == 6:
        print("Number found:", num)
        break
    else:
        print("Number not found:", num)