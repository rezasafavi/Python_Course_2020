import random 
# generate a random number between 1 to 10
secret_number = random.randint(1,10)
# get a number guess from the player 
while True:
    guess = int(input("guess a number between 1 to 10: "))
    if guess == secret_number:
        print("You got it! my number was {}".format(secret_number))
        break
    else:
        print("That's not it!")

# compare guess the secret number
if secret_number == player_number:
    print("Your hit game")
else:
    print("your miss game")
# print hit/miss
