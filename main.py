import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guess_log = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in guess_log:
      guess_log.append(guess)
      #print(f"Guess log {guess_log}")
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
          print(f"You guessed {guess}, that's not in the word. You lose a life.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")
  

      print(hangman_art.stages[lives])
    else:
      print(f'''You've already guessed {guess}''')
      print(f"{' '.join(display)}")
      print(hangman_art.stages[lives])