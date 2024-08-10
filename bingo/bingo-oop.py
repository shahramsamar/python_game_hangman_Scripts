from random import randint

class Bingo:
    def __init__(self,name):
        self.name = name
        self.random_number = randint(1, 10)
        self.guess_round = 5
        self.current_round = 0
   
    def check_guess(self, guessed_number):
        self.current_round += 1
        if guessed_number == self.random_number:
            return True        
        return False
    
    def check_gameOver(self):
            if self.current_round > self.guess_round:
                return True
            return False

user_list = []
user_list.append(Bingo('ali'))
user_list.append(Bingo('mohammad'))

bingo = Bingo("ali")
while True:
    guess_input = int(input("Enter your guess: "))
    if bingo.check_guess(guess_input):
        print("Bingo, you won the game!")
        break
    else:
        print("You have guessed wrong") 
        if guess_input < bingo.random_number:
            print("Guess higher")
        else:
            print("Guess lower") 
    if bingo.check_gameOver():
        print("You have failed to guess, so you have lost the game")
        break
