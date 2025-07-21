import random

def Guess(x):
    random_num = random.randint(1, x)
    guess = 0
    attempts = 0

    while guess != random_num:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            attempts += 1

            if guess < random_num:
                print("Sorry, guess again. Too low.")
            elif guess > random_num:
                print("Sorry, guess again. Too high.")
        except ValueError:
            print(" Please enter a valid number.")
            continue

    print(f"Congrats! You guessed the number {random_num} in {attempts} tries.\n")

while True:
    print("Welcome to the Number Guessing Game!")
    try:
        max_num = int(input("Enter the maximum number to guess up to: "))
        Guess(max_num)
    except ValueError:
        print("Enter a valid integer.")
        continue

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
