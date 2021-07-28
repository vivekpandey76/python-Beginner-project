import random

def guess(x):
    random__number=random.randint(1,x)
    guess__number=0
    while guess__number !=random__number:
        guess__number=int(input(f"Enter a number between 1 to {x}: "))
        if guess__number > random__number:
            print("The value is very high")
        elif guess__number < random__number:
            print("The value is too low")

    print("You won")


guess(10)