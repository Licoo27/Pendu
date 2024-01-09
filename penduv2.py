import random

correct_char = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

word_list = ["avant", "bebe", "ou", "abandon"]


def word_with_blanks(word_to_guess):
  blanks = list(word_to_guess)
  for i in range(len(word_to_guess)):
    blanks[i] = "__"
  print(' '.join(blanks))


def guess_a_letter():
  while True:
    guessed_letter = input("Guess a letter: ")
    if guessed_letter in correct_char:
      break
    else:
      print("Your letter is not correct, enter a valid one please")
  return guessed_letter


def replace_letter():
  for char in guess_a_letter:
    if dico[char] == "_":
      if char == guessed_letter:
        dico[char] = guessed_letter
  return dico


def regle_jeux_du_pendu():
  print(
      "Hello, thank you for activating our programm of the hangman game\n Here is the rules for the game :\n -you have 1à tries to find the word\n -You need to write the letters in capital letter \n -There is no ponctuation or accent \n Good luck"
  )


word_to_guess = random.choice(word_list)
print(word_to_guess)
word_with_blanks(word_to_guess)
