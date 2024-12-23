
import random

def hangman():
    # List of words to choose from
    words = ["python", "hangman", "programming", "development", "challenge"]
    # Select a random word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)  # Create a list to hold the guessed letters
    guessed_letters = []  # List to hold all guessed letters
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Set the limit for incorrect guesses

    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")
    
    while incorrect_guesses < max_incorrect_guesses and "_" in guessed_word:
        print("\nCurrent word:", " ".join(guessed_word))
        print("Guessed letters:", " ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            # Update the guessed_word list with the correct letter
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess! You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")

    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nSorry, you've run out of guesses. The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()