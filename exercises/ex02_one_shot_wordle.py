"""One attempt to guess the secret word"""

__author__: "730487901"

secret: str = "python"
guess: str = input("What is your guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

playing: bool = False
guess_idx: int = 0
alt_idx: int = 0
result: str = ""

while len(guess) != len(secret):
     guess = input(f"That was not {len(secret)} letters! Try again: ")
#while loop that allows the user to continue guessing until they reach the specified number of letters

while guess_idx < len(guess):
        #checking each index of the guess against for a match in the secret word
    if secret[guess_idx] == guess[guess_idx]:
        result = (result + GREEN_BOX)
    else:
        while playing is False and alt_idx < len(secret):
                #no match in first check
                #checking for letter match in wrong index
         if secret[alt_idx] == guess[guess_idx]:
              playing = True
              #match in wrong index
         else:
               alt_idx = alt_idx + 1
               #no match, increment variable
        if playing is True:
                result = (result + YELLOW_BOX)
                #match, concatenate
        else:
                result = (result + WHITE_BOX)
                #no match, concatenate
        alt_idx = 0
        playing = False
        #reset variables to run through again
    guess_idx = guess_idx + 1
    #increment variable
print(result)
    
if secret == guess:
        print("Woo! You got it! ")
if secret != guess:
        print("Not quite. Play again soon! ")
        















    
    


