import random
import hangman_art
import hangman_words
from replit import clear

#from hangman_art import logo, stages
#we can just print(stages)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

already_guessed = []
    
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess not in chosen_word and guess not in already_guessed:
        print(f"{guess} is not in the hangman word")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    if guess in already_guessed:
        print(f"You already guessed the letter: {guess}")
    else:
        already_guessed.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
    