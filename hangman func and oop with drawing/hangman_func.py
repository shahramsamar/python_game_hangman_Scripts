import random
import my_list

random_word = random.choice(my_list.words_list)
guess_word ="".join(['*' if char != " " else " " for char in random_word])
guess_left = 0
guess_char =[]
name = None
le=len(random_word)

def drawing(wrong):
    print(my_list.stages[wrong])

def Won():
    print(f"{name} , You Win ! \t \t  The word was : {random_word}")

def Lost ():
    print(f"{name} , You lost ! \t \t  The word was : {random_word}")

def check_words(random_word,guess_word):
    if random_word == guess_word :
        return True
    else :
        return False


name = input('type your name please : ')
print('guess_word :',guess_word,'.','lenght :',le,'character','.','guess_left :',7,'.')
while (guess_left < 7) :
    # if check_words(random_word,guess_word):
    #     #  print(f"you ran out of gueess !\n answer was :{random_word}")
    #     #  Won()
    #      print(f"You Win ! \t \t  The word was : {random_word}")
    #      break
    # else:
    #      pass
    answer_input = str(input(f"{name} , please type your guess : "))
    # answer_result = check_words(random_word,answer_input)
    if answer_input in guess_char :
         print(f'{name} , You have guessed this character !')
         print(f'{name} , plase type agin character .')
         continue
    else:
         guess_char.append(answer_input)
         change = 0
    for index,char in enumerate(random_word) :
        if str(char) == answer_input :
            guess_word = guess_word[:index] + answer_input + guess_word[index+1:]
            change +=1
            print(f"{name} , Good job is in the word woow")
    if change == 0:
         print("\n",f'{name} ,wrong guess !')      
         print(f"\n {name} ,try to run {guess_left} more ")  
         guess_left += 1
         drawing(guess_left-1)
         print('words:',guess_word)

         continue
    else:
          print(guess_word)
else:
    #  Lost() 
     print(f"You lost ! \t \t  The word was : {random_word}")
       


# print('random_word :',random_word)
# print('lenght :',le)
# print('guess_word :',guess_word)
# print('guess_left :',guess_left)   
# print('random_word :',random_word,'lenght :',le,'guess_word :',guess_word,'guess_left :',guess_left)
 