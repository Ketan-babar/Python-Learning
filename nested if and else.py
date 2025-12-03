#Nested IF and ELSE statement in Python

x = 10
y = 20

if x > y:
    print("x is greater than y")
else:
    if x == y:
        print("x is equal to y")
    else:
        print("x is less than y")

#example 2
age = 18
if age < 18:
    print("You are a minor.")
else:
    if age == 18:
        print("You are just an adult.")
    else:
        print("You are an adult.")