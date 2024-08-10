from random import randint


rand_number = randint(1, 10)
guess_rand = 5
current_round = 0
def check_guess(guessed_number):
    if guessed_number == rand_number:
        return True
    return False

while True:
    current_round += 1
    guess_input = int(input("enter your guess: "))

    # guess if right or wrong
    if check_guess(guess_input):
        print("Bingo, you won the game")
        break
    else:
        print("You have guessed wrong")
        if guess_input < rand_number:
            print("guess higher")
        else:
            print("guess lower")    
            
 # check for round counts
    if current_round > guess_rand:
        print("You have failed to guess, so you have lost the game") 
        break       