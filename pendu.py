import random

correct_char = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

word_list = ["avant", "bebe", "ou", "abandon"]


def afficher(dico):
  keys = dico.keys()
  chain = ""
  for key in keys:
    chain = chain + " " + dico[key]
  print(chain)


def take_a_word():
  word_to_guess = random.choice(word_list)
  return word_to_guess


def guess_a_letter():
  while True:
    guessed_letter = input("Guess a letter: ")
    if guessed_letter in correct_char:
      break
    else:
      print("Your letter is not correct, enter a valid one please")
  return guessed_letter


def word_with_blanks(word_to_guess):
  dico = {}
  for i in range(len(word_to_guess)):
    dico[i] = "_"
  return dico


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





print(regle_jeux_du_pendu())
print(take_a_word())
afficher(word_with_blanks(take_a_word()))
