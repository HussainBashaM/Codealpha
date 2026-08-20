import random

words = ["python", "computer", "program", "school", "keyboard"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Guess one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Incorrect guess.")

else:
    print("\nGame over!")
    print("The word was:", secret_word)
