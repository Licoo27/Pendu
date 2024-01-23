import random

mots = ["python", "pendu", "programmation", "informatique", "algorithme", "ordinateur", "developpeur"]

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

def validite_lettre(val):
    return val.isalpha() and len(val) == 1

def afficher_lettres_dites(lettres_dites):
    print("Lettres déjà dites :", ", ".join(lettres_dites))

  
def jouer_au_pendu():

  mot_a_trouver = random.choice(mots)
  lettres_trouvees = []
  lettres_dites = []
  essais_max = 7
  essais = 0

  print("\nBienvenue au jeu du Pendu!\n\n")
  
  while essais < essais_max:
      mot_cache = afficher_mot_cache(mot_a_trouver, lettres_trouvees)
      print("Mot actuel: ", mot_cache)
  
      afficher_lettres_dites(lettres_dites)
  
      if mot_cache == mot_a_trouver:
          print("Félicitations ! Vous avez trouvé le mot :", mot_a_trouver)
          break
  
      lettre = input("\nEntrez une lettre : ").lower()
  
      if not validite_lettre(lettre):
          print("\nVeuillez entrer une seule lettre valide.")
          continue
  
      if lettre in lettres_dites:
          print("Vous avez déjà dit cette lettre. Essayez une autre.")
      elif lettre in mot_a_trouver:
          print("\nBien joué!")
          lettres_trouvees.append(lettre)
      else:
          print("\nRaté...Essayez encore.")
          essais += 1
  
      lettres_dites.append(lettre)
      print("Il vous reste {} essais.".format(essais_max - essais))
  
      if essais == essais_max:
          print("Dommage ! Vous avez épuisé tous vos essais. Le mot était :", mot_a_trouver)



jouer_au_pendu()
if input("\nVoulez-vous rejouer ? (oui/non)   ") == "oui":
  jouer_au_pendu()
else:
  (print("Merci d'avoir joué !"))
