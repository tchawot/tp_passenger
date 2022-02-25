bus = {
    "identifiant": "",
    "nombrePlaceMax": 0,
    "nombrePlaceDisponible" : 0,
    "poidsMax": 0,
    "poidsDisponible": 0,
    "listePassager": []
}

def creerBus():
    newBus = bus.copy()
    identifiant = input("Entrez l'identifiant du bus: ")
    nombrePlaceMax = int(input("Entrez le nombre de place du bus: "))
    poidsMax = int(input("Entrez le poids Max des bagages du bus: "))
    newBus["identifiant"] = identifiant
    newBus["nombrePlaceMax"] = nombrePlaceMax
    newBus["nombrePlaceDisponible"] = nombrePlaceMax
    newBus["poidsMax"] = poidsMax
    newBus["poidsDosponible"] = poidsMax
    return newBus

def ajouterPassagerBus(bus,passager):
    if bus["nombrePlaceDisponible"] > 0:
        bus["listePassager"].append(passager)
        bus["nombrePlaceDisponible"] -= 1
        bus["poidsDisponible"] -= passager["poidsBagage"]
        return True
    else:
        return False

def retirerPassagerBus(bus,passager):
    if bus["listePassager"].count(passager):
        bus["listePassage"].remove(passager)
        bus["nombrePlaceDisponible"] += 1
        bus["poidsDisponible"] += passager["PoidsBagage"]
        return True
    else:
        return False

def afficherListePassagerBus(bus):
    print("Le noms des passagers  bus d'idenfifint {}".format(bus["identifiant"]))
    for item in bus["listePassager"]:
        print(item["nom"]+"\n")
