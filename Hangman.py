#Daniel Pingrey
#10/9/19
#Hangman

#imports
import random

#constants
hangman = ("""
======
| /         |
|
|
|
|
|
|
|          
|\        
=======
""",
"""
======
| /         |
|           O
|
|
|
|
|
|          
|\        
=======
""",
"""
======
| /         |
|           O
|           +
|            |
|            |
|
|
|          
|\        
=======
""",
"""
======
| /         |
|           O
|        - + 
|       /   |
|            |
|           
|          
|          
|\        
=======
""",
"""
======
| /         |
|           O
|        - + -
|       /   |   \\
|            |
|           
|          
|          
|\        
=======
""",
"""
======
| /         |
|           O
|        - + -
|       /   |   \\
|            |
|           /
|          /
|          
|\        
=======
""",
"""
======
| /         |
|           O
|        - + -
|       /   |   \\
|            |
|           /\\
|          /  \\
|          
|\        
=======
""")

maxWrong = len(hangman) - 1

words = ("Mountain", "Beagle", "Citris", "Trombone", "Confetti", "Covfefe", "Fedora", "Socialism", "Communism")


#initialize variables
word = random.choice(words)
so_far = "-" * len(word)
wrong = 0
used = []

print("Welcome to Hangman. Good luck, you'll need it.")

while wrong < maxWrong and so_far != word:
    print(hangman[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed that letter", guess)
        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()

    used.append(guess)
    if guess in word:
        print("\nCorrect", guess, "is in the word")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nMy apologies", guess, "isn't in the word.")
        wrong += 1

if wrong == maxWrong:
    print(hangman[wrong])
    print("\nYou've been hanged. Get a better vocab, buddy.")
else:
    print("\nYou were saved.")
print("\nThe word was", word)
input("\n\Press the enter key to exit.")

