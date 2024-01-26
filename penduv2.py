import random 

correct_char =  ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
"O" ,"P", "Q", "R", "S", "T", "U", "V", "W" ,"X", "Y", "Z"]

word_list = ["AVANT", "BEBE", "OU", "ABANDON"]


def blanks(word_to_guess):
  blanks = list(word_to_guess)
  for i in range(len(word_to_guess)):
    blanks[i] = "_"
  return ''.join(blanks)


def guess_a_letter():
  while True:
    guessed_letter = input("Guess a letter: ")
    if guessed_letter in correct_char:
      break
    else:
      print("Your letter is not correct, enter a valid one please")
  return guessed_letter


def replace_letter(blanks, word):
  tries = 10
  blank_list = list(blanks)
  while (''.join(blank_list)) != word or tries != 0:
    in_the_word = False
    x = guess_a_letter()
    for i in range(len(word)):
      if x == word[i]:
        blank_list[i] = x 
        in_the_word = True
    if in_the_word:
      tries -= 1
      print(f"Well done, you guessed a letter, you have {tries} tries left")
    if not in_the_word: 
      tries -= 1
      print(f"Sorry, {x} is not in the word, you have {tries} tries left")
  
    print(''.join(blank_list))
  print("Congratulations, you guessed the word!")


def regle_jeux_du_pendu():
  print(
      "Hello, thank you for activating our programm of the hangman game\n Here is the rules for the game :\n -you have 10 tries to find the word\n -You need to write the letters in capital letter \n -There is no ponctuation or accent \n Good luck"
  )


word_to_guess = random.choice(word_list)
word_with_blanks = word_to_guess
print(word_to_guess)
print(blanks(word_to_guess))

replace_letter(blanks(word_to_guess), word_to_guess)

