# guessing game

from random import randint
from IPython.display import clear_output
guessed = False
number = randint(0,100)
guessed = 0
while not guessed:
    ans = input("Try to guess the number I am thinking of! ")
    # use tab to indent
    guessed += 1
    clear_output()
    if int(ans) == number:
        print("Congrats! Ypu guessed it correctly.")
        # use tab twice to indent twice
        print("It took you { } guesses!".format(guessed))
        break
    elif int(ans) > number:
        print("The number is lower than what you guessed.")
    elif int(ans) < number:
        print("The number is greater than what you guessed")
