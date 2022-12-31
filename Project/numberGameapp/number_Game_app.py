import random 
# generate a random number between 1 to 10
secret_number = random.randint(1,10)
# get a number guess from the player 
while True:
    guess = int(input("guess a number between 1 to 10: "))
# compare guess the secret number
    if guess == secret_number:
        print("You got it! my number was {}".format(secret_number))
        break
    else:
        print("That's not it!")
