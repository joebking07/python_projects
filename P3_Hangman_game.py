from random import choice
import time

mystery_words = ["python", "javascript", "fullstack", "function", "variable", ""]
tepo_f = time.time()


def hangman_game(attempt):

    step = [
        """
           -------
           |     |
                 |
                 |
                 |
                 |
            ============
        """,
        """
           -------
           |     |
           O     |
                 |
                 |
                 |
            ============
        
        """,
        """
           -------
           |     |
           O     |
           |     |
                 |
                 |
            ============
        
        """,
        """
           -------
           |     |
           O     |
          /|     |
                 |
                 |
            ============
        
        """,
        """
           -------
           |     |
           O     |
          /|\\   |
                 |
                 |
            ============
        
        """,
        """
           -------
           |     |
           O     |
          /|\\   |
          / \\   |
                 |
            ===========
        
        """,
    ]

    print(step[attempt])


dice_choice = choice(mystery_words)
hidden_word = ["*"] * len(dice_choice)
health = 6
already_gess = set()
print(f" hidden word: {"".join(hidden_word)}")
max_error = 0
attempt = 0

while health > max_error:
    health -= 1

    tempo = time.time()
    print(f"your health number:  {health}")
    hangman_game(attempt)

    word_input = input("Guess letters of mystery Word: ").lower()
    already_gess.add(word_input)
    if len(word_input) != 1 or not word_input.isalpha():
        print("Error: your entry cannot exceed 1 letter")

    elif word_input in dice_choice and "*" in hidden_word:

        for i, letter in enumerate(dice_choice):

            if letter == word_input:
                print("Well done! you are find one letter")
                hidden_word[i] = word_input
                print("".join(hidden_word))

    elif word_input not in dice_choice:
        print("".join(already_gess))
        print(f"Oups! you are lose . health: {health}")
        attempt += 1
        if attempt == len(dice_choice):
            print(f"you are loose the mystery word is :{dice_choice}")
            break
