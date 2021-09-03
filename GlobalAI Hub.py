stop_number = int(input("Please enter a stop number: "))

result = 0
for i in range(0, stop_number):
    result = result + i
    print(result)
print(result)

start_number = int(input("Please enter a start number: "))
stop_number = int(input("Please enter a stop number: "))

result = 0
for i in range(start_number, stop_number):
    result += i

print(result)

start_number = int(input("Please enter a start number: "))

if 0 <= start_number <= 100:
    stop_number = int(input("Please enter a stop number: "))

    if start_number <= stop_number <= 100:

        result = 0
        for i in range(start_number, stop_number):
            result += i
        print(result)
    else:
        print("Invalid stop number")


else:
    print("Invalid start number")

import random as rnd

secret = rnd.randint(1, 100)

check = False

# guess = int(input("Please enter you guess: "))

for x in range(5):
    guess = int(input("Please enter you guess: "))
    if guess == secret:
        print("Congrats!!")
        check = True
        break
    elif guess < secret:
        print("Please enter a greater number!!")
    else:
        print("Please enter a smaller number!!")

if not check:
    print("You are a Looseer..The number was: ", secret);


tupl = (1,2,3,4,5)
print(tupl)
print(type(tupl))
