"""Ask user for number, give hints about number if wrong"""

SECRET: int = 12
guess: int = int(input("Guess a number "))
playing: bool = True

while playing:
    if guess == SECRET:
        print("Good job! You did it! Believe in your dreams")
        playing = False
    else:
        if guess % 2 == 1:
            print("Your guess is odd. The answer is even. ")
        if guess < SECRET:
            print("Too low ")
        else:
            print("Too high ")
        guess = int(input("Wrong guess bitch. Fuck you. Try again! "))

