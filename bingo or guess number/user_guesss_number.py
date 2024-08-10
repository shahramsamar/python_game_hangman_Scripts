import random



def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess =int(input(f"Guess a number Between 1 and {x}: "))
        if guess < random_number:
            print('Sorry,guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again.Too high')
    print(f'Yes,congrats. You have guessed the number: {random_number} correctly!!')        
# this is location your range number    
guess(10)    
        
        