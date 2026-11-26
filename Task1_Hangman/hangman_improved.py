import random

secret = ["apple", "cabbage", "basket", "bouquet", "python"]
MAX_MISTAKES = 6

# One picture for each number of wrong guesses (0 to 6)
STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def show_game(display, mistakes, wrong_letters):
    """Print the gallows, the word with blanks, and the wrong letters."""
    print(STAGES[mistakes])
    print("\nWord:", " ".join(display))
    print("Wrong letters:", " ".join(sorted(wrong_letters)) or "-")
    print(f"Tries left: {MAX_MISTAKES - mistakes}\n")


def play():
    word = random.choice(secret)
    display = ["_"] * len(word)
    guessed = set()         # every letter the player has tried
    wrong_letters = set()   # only the wrong ones (for showing on screen)
    mistakes = 0

    while True:
        show_game(display, mistakes, wrong_letters)

        letter = input("Please enter a letter: ").lower()

        # 1) Check the input is exactly one letter
        if not (len(letter) == 1 and letter.isalpha()):
            print("Your input is not valid.")
            continue

        # 2) Repeated letter: tell the player, but NO penalty
        if letter in guessed:
            print(f"You already guessed '{letter}'. Try another letter.")
            continue

        guessed.add(letter)

        # 3) Correct guess
        if letter in word:
            for position in range(len(word)):
                if word[position] == letter:
                    display[position] = letter

            if "_" not in display:
                print("\n*****************************")
                print("*   YOU WIN! Congratulations! *")
                print("*****************************")
                print("The word was:", word)
                break

        # 4) Wrong guess
        else:
            mistakes += 1
            wrong_letters.add(letter)

            if mistakes == MAX_MISTAKES:
                show_game(display, mistakes, wrong_letters)
                print("*****************************")
                print("*   GAME OVER - You lost!   *")
                print("*****************************")
                print("The word was:", word)
                break


play()
