"""Create your own adventure sytle game."""

__author__ = "730487901"

from random import randint


option: int = ()
player: str = ()
points: int = 0
cowboy: str = "\U0001F920"
horse: str = "\U0001F40E"


def greet() -> None:
    """Greeting."""
    global player
    global points
    print(f"Howdy partner! {cowboy} Welcome to your journey through the Wild West. Your goal is to leave this town a rich man.")
    player = input("What should we call you around here?: ")
    print(f"Well it's nice to meet you {player}, lets start you off with 100 coins. {horse}")
    points += 100


def main() -> None:
    """Main function."""
    global points
    global player
    points = 0
    playing: bool = True
    greet()
    while playing is True:
        menu()
        option = int(input("(1, 2, or 3): "))
        if option == 1:
            option_one()
        if option == 2:
            option_two(points)
        if option == 3: 
        
            print(f"Well {player}, we're sorry to see you go.")
            print(f"We wish you the best of health and luck on your travels. {horse}")
            print()
            print(f"You leave with {points} coins.")
            print()
            print("Game Over.")
            print()
            playing = False


def menu() -> None:
    """Menu."""
    global option
    global points
    print()
    print(f"You have {points} coins.")
    print()
    print(f"Where would you like to go next {player}? ")
    print("Here are your options... ")
    print(f"1. Visit the sherriff's office. {cowboy}")
    print(f"2. Visit the casino. {cowboy}")
    print(f"3. Say your goodbyes. {cowboy} {horse}")
   
    
def option_one() -> None:
    """First menu option."""
    global points
    print()
    print("Sherriff Bill has been gone for a few weeks now, looks like we've got an opening.")
    print(f"So {player}, do you think you have what it takes to keep this town safe?")
    answer: str = input("(Yes or No): ")
    if answer == "Yes":
        print()
        print(f"Well sir, I guess we now call you Sherrif {player}! {cowboy}")
        print("This role comes with a salary of 100 coins, don't spend it all in one place!")
        points += 100
        print()
        print(f"You have {points} coins.")
    if answer == "No": 
        print()
        print("Welp, another sacred city boy. You wont last two weeks out here.")
        print(f"Here's 50 coins anyways. Good luck out there. {horse}")
        points += 50
        print(f"You have {points} coins.")
      
    print()
    print("Let's go back into town and check out the general store.")
    store()
    

def store() -> None:
    """Store procedure."""
    global points
    print()
    print(f"Good afternoon {player}.")
    print()
    print("We just got a new delivery, let's see if anything catches your eye.")
    print("Store Inventory: ")
    print("1. Black Cowboy Hat: $45")
    print("2. Brown Leather Boots: $30")
    print("3. Oats: $5")
    print("4. Cigars: $10")
    print("5. No selection")
    cashier: str = "Nice choice, let's ring you up."
  
    selection = input("(1, 2, 3, 4 or 5): ")
    selection = int(str(selection))

    if selection == 1:
        print(cashier)
        points -= 45
        print(f"You now have {points} coins.")
       
    if selection == 2:
        print(cashier)
        points -= 30
        print(f"You now have {points} coins.")
     
    if selection == 3:
        print(cashier)
        points -= 5
        print(f"You now have {points} coins.")
       
    if selection == 4:
        print(cashier)
        points -= 10
        print(f"You now have {points} coins.")
         
    if selection == 5:
        print("That's too bad, maybe next time.")
        print(f"You now have {points} coins.")


def option_two(wager: int) -> int:
    """Menu option two."""
    global points
    answer: str = ""
    print()
    print(f"Welcome to Cowboy Casino, lets see if you've got some skill! {cowboy}")
    print("We're going to play the good ole' game 'Guess that number'")
    print()
    print("Here are the rules. You will guess a number between 1 and 100.")
    print("If your guess is within 25 numbers, you win 25 coins. ")
    print("If your guess is within 10 numbers, you win 50 coins. ")
    print("If your guess is within 5 numbers, you win 75 coins.")
    print("If you guess the secret number exactly, you win 1000 coins")
    print("If your guess is larger than the number you lose.")
    print("it costs 10 coins to play.")
    print()
    print(f"Your coin balance is {wager}")
    print()
    print("Would you like to play?")
    answer: str = input("(Yes or No): ")
    playing: bool = True

    if answer == "No":
        print()
        print("Not a gambling man I see, let's go back to the menu.")
        playing = False
    if answer == "Yes":   
        print()
        print("Alright, let's begin!")

    while playing is True:
        secret = randint(1, 100)
        guess = int(input("What is your guess?: "))
        print()

        if points < 10:
            print("You don't have enough coins to play, here's 20 to get you back on track.")
            points += 20 
        if secret == guess:
            print(f"Wow, Great job {player}. You got it! You win 1000 coins. ")
            points += 990
            print(f"You now have {points} coins. ")
    
        if secret - guess <= 25 and secret > guess and secret - guess >= 10:
            print("Not too bad, that's within 25. You win 25 coins.")
            points += 15
            print(f"You now have {points} coins. ")

        if secret - guess <= 10 and secret > guess and secret - guess >= 5:
            print("Very close, you are within 10! You win 50 coins.")
            points += 40
            print(f"You now have {points} coins. ")
    
        if secret - guess <= 5 and secret > guess and secret - guess >= 0:
            print("Almost got it! Great guess. You win 75 coins")
            points += 65
            print(f"You now have {points} coins. ")
    
        if secret - guess > 25 or guess > secret:
            print("Sorry, you lose!")
            points -= 10
            print(f"You now have {points} coins")
     
        print()
        print(f"The secret number was {secret}.")
        print()
        print("Would you like to play again? ")
        answer2 = input("(Yes or No): ")
        if answer2 == "No":
            print("Good effort, let's go back to the menu.")
            playing = False
    return points


if __name__ == "__main__":
    main()