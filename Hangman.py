import random
list=["monday","january","important"]


print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=random.choice(list)
# print(word_list)

word_length=len(word_list)


placeholder=""
game_over=False
lives=6

for character in range(word_length):
    placeholder+="_"
print("YOU HAVE TO GUESS",word_length,"LETTERS")    
print(placeholder)    
choosen_word=[]


while not game_over:

    guess=input("Guess a letter: ")
    display=""

    for letter in word_list:
        if letter==guess:
            display+=letter
            choosen_word.append(guess)
        
        elif letter in choosen_word:
            display+=letter
            
        else:
            display+="_"
        
    print(display) 
    
    if guess not in word_list:
        lives-=1
        print("YOU HAVE CHOOSEN",guess,"WHICH IS NOT IN THE LIST YOU HAVE",lives,"LIVES LEFT")
        if lives==0:
            game_over=True
            print("####--------------------------You loose----------------------------####")      
    
    if "_" not in display:
        game_over=True
        print("####-----------------------YOU WIN--------------------------####")     
    print(stages[lives])    
        