import random
from hangman_art import stages
from hangman_words import words
from hangman_art import logo
print(logo)
chosen_word = random.choice(words)
end_of_the_game = False
lives = 6

display = []

for i in range(len(chosen_word)):
    display += '_'
print(''.join(display))
while end_of_the_game == False:
    guessed_letter = input('Please guess a letter: ').lower()


    for i in range(len(chosen_word)):
        if guessed_letter == chosen_word[i]:
            display[i] = guessed_letter


    if not guessed_letter in chosen_word:
        lives -= 1

    if lives == 0:
        end_of_the_game = True
        print('You lose! The word was', chosen_word)

    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_the_game = True
        print('You win!')
    print(stages[lives])


