passager = {
    "identifiant": 0,
    "nom": " ",
    "poidsBagage": 0.0
}

def creerPassager():
    newPassager = passager.copy()
    identifiant = input("Entrez l'identifiant du passager: ")
    nom = input("Entrez le nom du passager: ")
    poidsBagage = int(input("Entrez le poids des bagages des Bagages du passager: "))
    newPassager[identifiant] = identifiant
    newPassager["nom"] = nom
    newPassager["poidsBagage"] = poidsBagage
    return newPassager

