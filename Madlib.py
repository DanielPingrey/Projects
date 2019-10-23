#Daniel Pingrey
#9/9/19
#MadLib

#Values
name = input("Enter your name: ")
word1 = input("Enter an adj: ")
word2 = input("Enter a noun: ")
word3 = input("Enter a verb: ")
word4 = input("Enter another adj: ")
word5 = input("Enter yet another adj: ")
word6 = input("Enter something: ")
sound = input("Enter a sound: ")
noise = input("Enter a noise: ")

#Text
text = str.format("""The {0} Pacer Test is a multistage aerobic capacity 
test that progressively gets more {1} as it continues.
The 20 meter {2} test will begin in 30 seconds.
Line up at the start.
The running speed starts {2}, but gets faster each minute after you hear this signal. {8} 
A single lap should be completed each time you hear this sound. {7} 
Remember to {2} in a {4} line and run as long possible.
The second time you fail to complete a lap before the sound, your test is {5}.
Your test will begin on the word {6}.""", name, word1, word2, word3, word4, word5, word6, sound, noise)

#Prints text and opens and closes the program
print(text)
input()
