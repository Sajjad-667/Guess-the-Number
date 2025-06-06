import random

secret_number = random.randint(1, 10)
guess = None

print("Guess the number between 1 and 10.")

# Keep asking until the guess is correct
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("🎉 Correct! You guessed it!")