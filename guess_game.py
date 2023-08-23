import random

number = random.randint(1, 10)
guess = None
count = 0

while guess != number:
    number = random.randint(1, 10)
    guess = int(input("Guess number between 1 and 10: "))
    if guess == number:
        print("True guess man!")
        print(f"The count of guessing number: {count}")
        break
    else:
        print("Try again! Number was {}".format(number))
    count += 1

