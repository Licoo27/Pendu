var mots = [];

async function recupMots() {
  return await fetch("pli07.txt")
    .then((res) => res.text())
    .then((text) => {
      mots = text.split("\n");
      motATrouver = choisirMot();
      afficherMotCache();
      afficherLettresDites();
    })
    .catch((e) => console.error(e));
}

recupMots();

console.log(mots);


var motATrouver = ""
var lettresTrouvees = [];
var nblettresTrouvees = 0;
var lettresDites = [];
var essaisMax = 9;
var essais = 0;
var max_segment = 9;
var hangman = document.getElementsByClassName("hangman");
var hangmanDiv = []
for (var i = 1; i < max_segment + 1; i++) {
  hangmanDiv.push(document.getElementsByClassName("hangman" + i)[0]);
}

for (var i = 0; i < hangmanDiv.length; i++) {
  hangmanDiv[i].classList.add("hidden-div");
}

var tab = []


function choisirMot() {
  return mots[Math.floor(Math.random() * mots.length)];
}

function afficherMotCache() {
  var motCache = "";
  for (var i = 0; i < motATrouver.length; i++) {
    if (lettresTrouvees.includes(motATrouver[i])) {
      motCache += motATrouver[i];
    } else {
      motCache += "_";
    }
  }
  document.getElementById("word").textContent = motCache + " ( " + motATrouver.length + " lettres )";
}

function afficherLettresDites() {
  document.getElementById("letters").textContent = lettresDites.join(", ");
}

function afficherMessage(message) {
  var essaisRestants = essaisMax - essais;
  document.getElementById("message").textContent = message + " Essais restants : " + essaisRestants;
}

function jouerTour() {
  var lettreInput = document.getElementById("letter-input");
  var lettre = lettreInput.value.toUpperCase();



  if (!/^[a-zA-Z]$/.test(lettre)) {
    afficherMessage("Veuillez entrer une lettre valide.");
    lettreInput.value = "";
    return;
  }

  if (lettresDites.includes(lettre)) {
    afficherMessage("Vous avez déjà dit cette lettre. Essayez une autre.");
    return;
  }

  lettresDites.push(lettre);

  if (motATrouver.includes(lettre)) {
    lettresTrouvees.push(lettre);
    nblettresTrouvees += motATrouver.split(lettre).length - 1;
    afficherMessage("Bien joué !");
  } else {
    essais++;
    afficherMessage("Raté... Essayez encore.");
    document.getElementsByClassName("hangman").src = "hangman" + essais;
    hangmanDiv[essais - 1].classList.remove("hidden-div");
  }

  afficherMotCache();
  afficherLettresDites();

  if (nblettresTrouvees === motATrouver.length) {
    afficherMessage("Félicitations ! Vous avez trouvé le mot : " + motATrouver);
  }

  if (essais === essaisMax) {
    afficherMessage("PENDU! Le mot était : " + motATrouver);
  }

  lettreInput.value = "";
}


afficherMotCache();
afficherLettresDites();
