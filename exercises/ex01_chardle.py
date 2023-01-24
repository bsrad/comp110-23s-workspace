"""EX01 - Chardle - A step towards Wordle."""

__author__ = "730487901"

word: str = input("Enter a 5 character word: ")
if (len(word) != 5): 
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if (len(letter) != 1): 
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)

count: int = (0)

if (word[0] == letter):
    print(letter + " found at index 0")
    count = count + 1
if (word[1] == letter):
    print(letter + " found at index 1")
    count = count + 1
if (word[2] == letter):
    print(letter + " found at index 2")   
    count = count + 1
if (word[3] == letter):
    print(letter + " found at index 3")
    count = count + 1
if (word[4] == letter):
    print(letter + " found at index 4")
    count = count + 1

if (count > 1):
    print(str(count) + " instances of " + letter + " found in " + word)
if (count == 1):
    print("1 instance of " + letter + " found in " + word)
if (count == 0):
    print("No instances of " + letter + " found in " + word)