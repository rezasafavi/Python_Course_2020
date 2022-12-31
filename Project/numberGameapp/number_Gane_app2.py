import random 
# generate a random number between 1 to 10
secret_number = random.randint(1,10)
# get a number guess from the player 
def run_game():
    guesses = []
    guesses = 0

    while len(guesses)<5:
        # safely make an int 
        try:
            guess = int(input("guess a number between 1 to 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
    # compare guess the secret number
            if guess == secret_number:
                print("You got it! my number was {}".format(secret_number))
                break
            elif guess < secret_number: 
                print("my number is higher than {}".format(guess))
            elif guess > secret_number: 
                print("my number is lower than {}".format(guess))
            else:
                print("That's not it!")
            guesses.append(guess)
    else:
        print("you didn't get it ! my number was {}".format(secret_number))  

    play_again =input("Do You Want to play again? [Y/n]")     
    if play_again.lower() != 'n':
        run_game
    else:
        print("Bye!")


                
run_game()

