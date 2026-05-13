import random

words = ["apple", "tiger", "chair", "robot", "table"]
word = random.choice(words)

guessed = []
attempts = 6

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if "_" not in display:
        print("You Won!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("You Lost! Word was:", word)
