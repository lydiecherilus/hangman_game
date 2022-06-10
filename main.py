import random
from drawing import life_stages
from word_list import words
from hangman_logo import art_work

print(art_work)
user_life = len(life_stages) - 1
is_end_of_game = False
word_canvas = []

# a word is randomly chosen from list of words
chosen_word = random.choice(words)
print("Hint - It's an animal")

# print space to add player guesses
for letter in chosen_word:
  word_canvas.append("__")
print(f"{' '.join(word_canvas)}")
print("")

# loop to check if letter chosen by the player is in the word
while not is_end_of_game:
  guess = input("Guess a letter: ").lower()

  # give the player feedback if their guess is a letter previously guessed
  if guess in word_canvas:
    print(f" You already guessed this letter {guess}")

  # place guessed letter in right position in the word
  for i in range(len(chosen_word)):
    letter = chosen_word[i]
    if letter == guess:
      word_canvas[i] = letter
  print(f"{' '.join(word_canvas)}")

  # if letter guessed is not in the world, let palyer know their are losing
  if guess not in chosen_word:  
    print(f"You guessed {guess}, this is not a letter in the word, you lose a chance.")
    user_life -= 1
    if user_life == 0:
      is_end_of_game = True
      print("You lose.")
      print(f"The word is {chosen_word}")
    print(life_stages[user_life])

  if "__" not in word_canvas:
    is_end_of_game = True
    print("you win!") 