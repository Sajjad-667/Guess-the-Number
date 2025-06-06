# 🎲 Number Guessing Game

A simple Python command-line game where you try to guess a randomly generated number between 1 and 10.

## 📋 Description

This program generates a random number between 1 and 10 and prompts the user to guess the number. After each guess, the program gives feedback:

- "Too low!" if the guess is less than the secret number.
- "Too high!" if the guess is more than the secret number.
- "🎉 Correct! You guessed it!" when the guess is correct.

The game continues until the correct number is guessed.

## 🧑‍💻 How to Run

1. Make sure you have Python installed (Python 3 recommended).
2. Save the code in a file, for example: `main.py`
3. Run the script using the terminal:

```bash
python main.py
```

## 🔧 Requirements

- Python 3.x

No additional libraries are required.

## 📦 Sample Code

```python
import random

secret_number = random.randint(1, 10)
guess = None

print("Guess the number between 1 and 10.")

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
```

## 🚀 Features

- Input validation for non-integer inputs
- Friendly user prompts
- Random number generation

## 📜 License

This project is licensed under the MIT License.
