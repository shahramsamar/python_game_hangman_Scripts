from random import randint

class Bingo:
    
    def __init__(self, name):
        self.name = name
        self.random_number = randint(1, 10)
        self.guess_round = 5
        self.current_round = 1
        self.won = False
    
    def check_guess(self, guessed_number):
        self.current_round += 1
        if guessed_number == self.random_number:
            self.won = True
            return True
        return False
    
    def check_game_over(self):
        if self.current_round > self.guess_round:
            return True
        return False
    
    def __str__(self):
        return f"{self.name}: {'won' if self.won else 'player is game_over'} , Rounds: {self.current_round} AS {self.guess_round}"


class Game:
    
    def __init__(self, players):
        self.players = [Bingo(name) for name in players]
                
    
    def play(self):
        while True:
            all_done = True
            for player in self.players:
                if player.won or player.check_game_over():
                    continue
                
                all_done = False
                guess_input = int(input(f'{player.name}, enter your guess:'))
                
                if player.check_guess(guess_input):
                    print(f'{player.name}, Bingo! You won the game!')
                else:
                    print('You have guessed wrong')
                    
                    if guess_input < player.random_number:
                        print('Guess higher')
                    else:
                        print('Guess lower')    
                
                if player.check_game_over() and not player.won:
                    print(f"{player.name}, you have failed to guess.You lost the game .")        
            
            if all_done:
                break    
            
        self.display_results()
        
    def display_results(self):
     print('\nGame over. Results:')
     sorted_players = sorted(self.players, key=lambda p: p.current_round)
     for player in sorted_players:
        print(player)


# Example of creating a game with multiple players
player_names = ['Ali', 'Mohammad', 'Sara']
game = Game(player_names)
game.play()                