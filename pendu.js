var mots = ["javascript", "pendu", "informatique", "programmation", "html", "css", "groupe"];
var motATrouver = choisirMot();
var lettresTrouvees = [];
var lettresDites = [];
var essaisMax = 7;
var essais = 0;

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
    var lettre = lettreInput.value.toLowerCase();

    
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
        afficherMessage("Bien joué !");
    } else {
        essais++;
        afficherMessage("Raté... Essayez encore.");
        document.getElementsByClassName("hangman").src = "hangman" + essais;
    }

    afficherMotCache();
    afficherLettresDites();

    if (lettresTrouvees.length === motATrouver.length) {
        afficherMessage("Félicitations ! Vous avez trouvé le mot : " + motATrouver);
    }

    if (essais === essaisMax) {
        afficherMessage("Dommage ! Vous avez épuisé tous vos essais. Le mot était : " + motATrouver);
    }

    lettreInput.value = "";  
}

function recommencerPartie() {
    motATrouver = choisirMot();
    lettresTrouvees = [];
    lettresDites = [];
    essaisMax = 7;
    essais = 0;
    document.getElementById("hangman-image").src = "hangman0.png";
    afficherMessage("");
    afficherMotCache();
    afficherLettresDites();
    document.getElementById("letter-input").value = "";
}


afficherMotCache();
afficherLettresDites();
