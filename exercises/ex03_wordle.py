"""Structured wordle."""

__author__ = "730487901"


def contains_char(word: str, char: str) -> bool:
    """Search for character match inside of word."""
    assert len(char) == 1
    # character ,must have length of one
    word_idx = 0
    playing = False
    while word_idx < len(word) and playing is False:
        # checking for match inside of word
        if word[word_idx] == char:
            playing = True
            # if there is a match return True
        else:
            word_idx = word_idx + 1
    return playing
    # if there is no match return false


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis."""  
    assert len(guess) == len(secret)
    # length of the guess must match the length of the secret word
    check_idx = 0
    result: str = ""
    while check_idx < len(secret):
        # runs while the index being checked in less than the length of the secret word
        if guess[check_idx] == secret[check_idx]:
            result = (result + GREEN_BOX)
            # concatenates green box if there is a match in the correct index
            check_idx = check_idx + 1
        else:
            if contains_char(secret, guess[check_idx]) is False:
                result = (result + WHITE_BOX)
                # if there is no match concatenate white box
            if contains_char(secret, guess[check_idx]) is True:
                result = (result + YELLOW_BOX)
                # if there is no match concatenate yellow box
            check_idx = check_idx + 1
            # move on to next index
    return result


def input_guess(int_guess: int) -> str:
    """Prompts user for a guess and checks length."""
    word = input(f"Enter a {int_guess} character word: ")
    # prompt user for guess and print f string with correct length
    while len(word) != int_guess:
        word = input(f"That wasn't {int_guess} chars! Try again: ")
        # if guess was not correct amount of chars, prompt for another guess
    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    turns = 1
    playing_wordle = True
    # defining necessary variables
    while turns <= 6 and playing_wordle is True:
        # gives 6 turns and allows loop to finish when won
        print(f"=== Turn {turns}/6 ===")
        word: str = (input_guess(len(secret)))
        # calling input_guess and assigning it to the variable 'word'
        if len(word) == len(secret):
            print(emojified(word, secret))
        # calling emojified with the stored variabke from input_guess
        if word == secret:
            playing_wordle = False
            # user has won
        else: 
            # user has not won
            turns = turns + 1
    if playing_wordle is True:
        print("X/6 - Sorry, try again tomorrow! ")
    if playing_wordle is False:
        print(f"You won in {turns}/6 turns! ")


if __name__ == "__main__":
    main()