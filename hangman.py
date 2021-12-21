# import the necessary data created in another python file for better readablity
import random
from hangman_art import stages, logo
from hangman_words import word_list
# printing the logo for more visual pleasantness!
# defining the number of lives and a boolean to check if the game has ended later in our loop
print(logo)
game_is_finished = False
lives = len(stages) - 1
# creating a random word from the list we imported earlier and ckeck the length of the word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# iterate through each letter of the word and make a list of it to be used in our while loop
display = []
for _ in range(word_length):
    display += "_"
# check to see if each of the letters exist within the actual chosen word with this while loop
while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #You can use a clear() function here to clear the output between guesses so that it becomes easier to follow the game

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
