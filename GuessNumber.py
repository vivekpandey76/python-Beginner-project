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

# guess(10)

def computer_guess(y):
    low=1
    high=y
    feedback=''
    while feedback !='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} is correct (c) or low (l) or high (h)')
        if feedback == 'l':
            guess=low+1
        elif feedback == "h":
            guess=high-1

    print("Yay congrats you won")

computer_guess(10)