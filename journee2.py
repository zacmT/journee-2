import re

def analyser_heure(entree):
    try:
        # Nettoyage de l'entrée
        entree = entree.strip().lower()

        # On récupère uniquement les chiffres de début (ex: "17:59" → 17, "17h30" → 17)
        match = re.match(r"(\d{1,2})", entree)
        if not match:
            return "Entrée non valide"

        heure = int(match.group(1))

        # Vérification si l'heure est valide
        if heure < 0 or heure > 23:
            return "Heure invalide"

        # Analyse de la période de la journée
        if heure == 12:
            return "midi"
        elif 13 <= heure <= 17:
            return "après-midi"
        elif 18 <= heure <= 23:
            return "soir"
        elif 0 <= heure <= 11:
            return "matin"
        else:
            return "inconnu"
    except ValueError:
        return "Entrée non valide"


# Boucle interactive
while True:
    heure = input("Entrez une heure (ou 'exit' pour quitter) : ")
    if heure.lower() == "exit":
        print("Programme terminé ✅")
        break
    print(analyser_heure(heure))
