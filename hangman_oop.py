import random
import my_list

class Hangman:
  def  __init__(self) :
       self.guess_char = []
       self.guess_left = 0
       self.name = input("Enter your name : ")
       self.random_word = random.choice(my_list.words_list)
       self.guess_word = "".join(['*'if char != " " else " " for char in self.random_word])
       self.count_char = len(self.guess_word)

  @property
  def check_words(self) :
      if self.random_word == self.guess_word :
          return True
      else :
          return False

  @property
  def game_controller(self) :
       while(self.guess_left < 7) :
              answer_input = str(input(f"{self.name} , please type your guess : "))
              if answer_input in self.guess_char :
                 print('You have guessed this character !')
                 print('plase type agin character .')
                 continue
              else :
                  self.guess_char.append(answer_input)
                  change = 0

              for index,char in enumerate(self.random_word) :
                 if str(char) == answer_input :
                     self.guess_word = self.guess_word[ : index ] + answer_input + self.guess_word[ index + 1 : ]
                     change += 1
                     print("Good job is in the word woow")
              if change == 0 :
                 print("\n",'wrong guess !')      
                 print(f"\n try to run {self.guess_left} more ")  
                 self.guess_left += 1
                 drawing(self.guess_left -1)
                 print('words:',self.guess_word)
                 continue
              else :
                 print(self.guess_word)
       else :
              print(f"You lost ! \t \t  The word was : {self.random_word}")

def drawing(wrong):
    print(my_list.stages[wrong])

user = Hangman()
user.game_controller

