from random import choice
import time

mystery_words = ["python", "javascript", "fullstack", "function", "variable", "algorithm", "data", "structure", "object", "oriented"]



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


# main function
def main():
    start_time = time.time()
    print("{:=^70}".format("WELCOME TO HANGMAN GAME "))
    dice_choice = choice(mystery_words)
    hidden_word = ["*"] * len(dice_choice)
    health = 6
    already_gess = set()
    attempt = 0

    while health > 0:

        print(f" Hidden word: {"".join(hidden_word)}")
        print(f"Health left:  {health}")
        print(
            f"Already guessed :{",".join(sorted(already_gess)) if already_gess else "None"}"
        )
        hangman_game(attempt)

        guess = input("Guess letters of mystery Word: ").lower()

        if len(guess) != 1 or not guess.isalpha():

            print("Error: you must enter exactly 1 letter")
            continue

        if guess in already_gess:
            print("You already guess this letter")
            continue

        already_gess.add(guess)

        # win condition
        if guess in dice_choice:
            print("well done!! you are  find one letter")
            for i, letter in enumerate(dice_choice):
                if guess == letter:
                    hidden_word[i] = guess

        else:
            print("Oups!! Wrong gess")
            attempt += 1
            health -= 1

        if "*" not in hidden_word:
            elapsed_time = time.time() - start_time
            print(f"Well done!! you are win in {elapsed_time:.2f} second")
            print(f"the secret word is: {dice_choice}")
            break

        if health == 0:
            elapsed_time = time.time() - start_time
            print(f"Oups!! you lost the time taken is {elapsed_time:.2f} second")
            print(f"the secret word is: {dice_choice}")
            break


if __name__ == "__main__":
    main()
